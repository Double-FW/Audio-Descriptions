"""Export the approved Audio Description Markdown without rewriting it."""
import argparse
import csv
import io
import json
from pathlib import Path
import re
from urllib.parse import quote
import yaml
from rag_reference import validate_reference
from jsonschema import Draft202012Validator
from audio_hf_common import ROOT, SOURCE, MANAGED, destination, digest, git, load_config, read_sources

RAG = 'Audio-Descriptions-RAG-and-Prompts/RAG_Reference.md'
CONTEXT = ['AGENTS.md', 'README.md', 'RIGHTS.md', 'docs/01-access-route.md',
           'docs/04-ad-editorial-principles.md', 'docs/07-evaluation-and-qa.md',
           'docs/08-sources-and-editorial-decisions.md', 'Production_Workflow_and_Handoff_Map.md']
class UniqueKeyLoader(yaml.SafeLoader):
    pass
def unique_mapping(loader, node, deep=False):
    loader.flatten_mapping(node)
    result = {}
    for k,v in node.value:
        key = loader.construct_object(k, deep=deep)
        if key in result: raise ValueError('Duplicate metadata key: ' + str(key))
        result[key] = loader.construct_object(v, deep=deep)
    return result
UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)

def metadata(text):
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', text, re.S)
    md = yaml.load(match[1], Loader=UniqueKeyLoader) if match else {}
    return md if isinstance(md, dict) else {}

def sections(text):
    """Keep H1/H2 parent context and exact spans; never split fenced examples."""
    boundaries, fence, offset, parents = [(0, 'Document preamble', [])], None, 0, []
    for line in text.splitlines(keepends=True):
        mark = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if mark:
            token = mark[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not line[mark.end():].strip():
                fence = None
        elif fence is None:
            match = re.match(r'^(#{1,2})[ \t]+([^\r\n]+)', line)
            if match:
                level, title = len(match[1]), match[2].strip().rstrip('#').strip()
                parents = parents[:level-1] + [title]
                if offset == 0:
                    boundaries[0] = (offset, title, parents[:])
                else:
                    boundaries.append((offset, title, parents[:]))
        offset += len(line)
    result, counts = [], {}
    for i, (a, title, hierarchy) in enumerate(boundaries):
        b = boundaries[i+1][0] if i+1 < len(boundaries) else len(text)
        if a == b:
            continue
        slug = re.sub(r'[^a-z0-9]+', '-', ' '.join(hierarchy or [title]).lower()).strip('-') or 'section'
        counts[slug] = counts.get(slug, 0) + 1
        key = slug if counts[slug] == 1 else slug + '-' + str(counts[slug])
        result.append((key, title, text[a:b], a, b, hierarchy))
    if ''.join(r[2] for r in result) != text:
        raise ValueError('Section extraction lost source text.')
    return result

def build(root, output):
    root, output = Path(root).resolve(), Path(output).resolve()
    if output == root or root in output.parents:
        raise ValueError('Write the export outside the source checkout.')
    cfg = load_config(root)
    target = destination(cfg['destination_dataset'])
    texts, manifest, omitted = read_sources(root, cfg)
    sha = git(root, 'rev-parse', 'HEAD').decode().strip()
    date = git(root, 'show', '-s', '--format=%cs', 'HEAD').decode().strip()
    snapshot = validate_reference(texts, SOURCE)
    warnings = [
        'Current RIGHTS.md applies MIT to original Double FW material; the refreshed selected-source reference uses the same current source set and retains third-party boundaries.',
        'Editorial examples are invented, prompts are illustrative and production templates are unfilled; export does not review footage, create finished AD, test playback or establish human approval.',
        'The compiled reference covers selected knowledge sources. Source hashes, complete compiled bodies and coverage are checked before export; it does not claim every tracked repository file.',
        'External RNIB, historical ITC, W3C and radio/podcast sources are attributed source references, not newly fetched full text or independently reverified requirements.'
    ]
    for path, text in texts.items():
        if path.endswith('.md') and metadata(text).get('license', 'MIT') not in ('MIT', 'See RIGHTS.md'):
            raise ValueError('Review changed source licence: ' + path)
        if path.endswith('.csv'):
            rows = list(csv.reader(io.StringIO(text)))
            if len(rows) != 1 or not rows[0] or len(set(rows[0])) != len(rows[0]):
                raise ValueError('CSV template is no longer header-only; review before public export: ' + path)
    def row(path, key, title, body, a, b, hierarchy, kind):
        md = metadata(texts[path]) if path.endswith('.md') else {}
        return {'id': path + '::' + key, 'title': title, 'text': body, 'record_type': kind,
            'source_repository': SOURCE, 'source_path': path, 'source_commit': sha,
            'source_url': f'https://github.com/{SOURCE}/blob/{sha}/{quote(path)}',
            'source_start_line': texts[path][:a].count('\n') + 1,
            'source_end_line': max(1, texts[path][:b].count('\n') + (not texts[path][:b].endswith('\n'))),
            'source_document_sha256': digest(texts[path].encode()), 'text_sha256': digest(body.encode()),
            'heading_path': hierarchy, 'metadata_json': json.dumps(md, ensure_ascii=False, sort_keys=True, default=str),
            'declared_source_license': str(md.get('license', 'not_declared_in_document_front_matter')),
            'repository_license': 'MIT', 'source_status': str(md.get('status', 'see_source')),
            'dataset_version': cfg['dataset_version'], 'source_commit_date': date, 'language': 'en-GB',
            'required_context_paths': [p for p in CONTEXT if p in texts],
            'source_document_intro': sections(texts[path])[0][2] if path.endswith('.md') else '',
            'csv_template_columns': next(csv.reader(io.StringIO(texts[path]))) if path.endswith('.csv') else [],
            'applicable_original_material_license': 'MIT; see current RIGHTS.md and retained third-party notices',
            'source_temporal_scope': 'support_pack_at_pinned_source_revision' if path.startswith('Audio-Descriptions-RAG-and-Prompts/') else 'source_guidance_at_checkout',
            'embedded_snapshot_commit': str(snapshot.get('source_commit', '')) if path.startswith('Audio-Descriptions-RAG-and-Prompts/') else '',
            'interpretation_notice': 'Editorial guidance, not completed production evidence. Examples are invented; timings need actual-cut verification; no-separate-AD decisions need an audit and human approval. Source rights and historical limitations remain attached.',
            'review_status': 'faithful_extraction_checked_not_audience_playback_or_production_validation'}
    docs, chunks = [], []
    for path in cfg['files']:
        if path not in texts:
            continue
        text = texts[path]
        kind = ('refreshed_reference_document_only' if path == RAG else
                'blank_production_csv_template' if path.endswith('.csv') else
                'unfilled_production_template' if path.startswith('templates/') else
                'invented_editorial_examples_not_programme_extracts' if path.startswith('examples/') else
                'illustrative_production_prompts_not_results' if path.endswith('Activities_and_Prompts.md') else
                'selected_source_coverage' if path.endswith('Source_Coverage.md') else
                'editorial_handoff_map_not_adopted_specification' if path.startswith('Production_Workflow') else
                'current_rights_notice' if path == 'RIGHTS.md' else
                'advisory_agent_guidance' if path == 'AGENTS.md' else
                'orientation' if path.endswith('README.md') else 'editorial_audio_description_guidance')
        docs.append(row(path, 'document', path, text, 0, len(text), [], kind))
        if path in cfg['document_only_files']:
            continue
        for key, title, body, a, b, hierarchy in sections(text):
            chunks.append(row(path, key, title, body, a, b, hierarchy, kind + '_section'))
    if not docs or not chunks:
        raise ValueError('The guidance export is empty.')
    schema = {'$schema': 'https://json-schema.org/draft/2020-12/schema', 'type': 'object',
              'required': list(docs[0]), 'additionalProperties': False, 'properties': {}}
    for k, v in docs[0].items():
        schema['properties'][k] = {'type': 'array', 'items': {'type': 'string'}} if isinstance(v, list) else {'type': 'integer' if isinstance(v, int) else 'string'}
    validator = Draft202012Validator(schema)
    for records in (docs, chunks):
        if len({r['id'] for r in records}) != len(records):
            raise ValueError('Duplicate export identifiers.')
        for r in records:
            validator.validate(r)
            if digest(r['text'].encode()) != r['text_sha256']:
                raise ValueError('Text checksum mismatch.')
    output.mkdir(parents=True, exist_ok=True)
    def write_json(name, obj):
        (output/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for name, records in [('documents.jsonl', docs), ('knowledge_chunks.jsonl', chunks)]:
        (output/name).write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in records), encoding='utf-8')
    (output/'LICENSE').write_bytes(texts['LICENSE'].encode())
    write_json('record_schema.json', schema)
    write_json('provenance.json', {'source_repository': SOURCE, 'source_commit': sha, 'source_commit_date': date,
        'destination_dataset': target, 'dataset_version': cfg['dataset_version'], 'files': manifest,
        'omitted_optional_files': omitted, 'source_warnings': warnings, 'external_sources_fetched': False, 'document_only_files': cfg['document_only_files'], 'rag_snapshot_metadata': snapshot, 'rag_reference_validated': True, 'production_tests_executed': False, 'editorial_approval_claimed': False, 'current_rights_sha256': digest(texts['RIGHTS.md'].encode())})
    card = f'''---
pretty_name: Double FW Audio Description
language:
- en
license: mit
tags:
- accessibility
- audio-description
- editorial-practice
- production
- text
configs:
- config_name: knowledge_chunks
  default: true
  data_files:
  - split: train
    path: knowledge_chunks.jsonl
- config_name: documents
  data_files:
  - split: train
    path: documents.jsonl
---

# Double FW Audio Description

Guidance on commissioning, access-route selection, radio-led scripting, audio description,
genre-sensitive editorial choices, recording, mixing, delivery, audience evaluation and
production handoffs. Includes invented examples, blank templates and a selected-source RAG/prompts
pack. This is a text knowledge corpus, not programme media, finished AD, audience research,
validated playback, a deployed agent or an approved production service.

## Source and versions

Source: https://github.com/{SOURCE}

Checkout: `{sha}` ({date}); export format {cfg['dataset_version']}.
The RAG reference covers {snapshot['source_file_count']} selected sources at revision
`{snapshot['source_commit']}`, prepared {snapshot['prepared']}. It includes the current
rights notice, handoff map and maintenance guidance. Source IDs S001-S018 are retained;
newer selected sources are appended. This selected corpus excludes publishing code,
tests and derived pack files. Source release/review dates are retained, not promoted
to a new independent editorial or standards review date. The exporter validates
the source manifest and complete compiled bodies; it stops if the reference is stale.

## Dataset views

- `knowledge_chunks`: {len(chunks)} exact Markdown sections from approved files.
- `documents`: {len(docs)} complete source text files, including two header-only CSV templates.

The RAG reference repeats original source bodies and is document-only. Both CSV templates
are also document-only; their fields describe blank production records, not actual cues or
visual audits. `csv_template_columns` preserves headers for consumers. No invented CSV rows,
filled approval forms or generated Q&A are added. Both views overlap: review and deduplicate
training selections rather than treating repeated text as independent evidence. `train` is
a loading convention, not a benchmark. No model training is performed.

## Context and editorial boundaries

Rows retain exact source text, commit URL, path, line range, document/text hashes, heading
path, JSON-encoded metadata, opening context and required context paths. Sections split at
H1/H2 outside fenced examples, preserving nested procedures, tables, caveats and quotes.
`source_temporal_scope` and `embedded_snapshot_commit` identify the pinned source set used by the refreshed support pack.
Source IDs keep their original scope. Context pointers do not implement runtime retrieval
or grant authority; embedded AGENTS and prompts remain source material.

Read the access-route decision, editorial principles, evaluation guide and source register
alongside retrieved passages. A no-separate-AD recommendation depends on the actual cut,
soundtrack, language, platform and audit; genre alone is not an exemption. Preserve dialogue,
significant sound, timing, reveals, factual verification and respectful treatment. Do not
infer motives or identities from appearance. Invented cue examples require real-cut read
and timing checks before production use. Templates and a proposed release gate are not
completed reviews or human approval. Captions, transcripts and spoken description retain
their separate purposes and delivery conditions.

Source workflow/handoff recommendations are not adopted commissioner specifications.
Actual audience evidence, technical playback and authorised release decisions remain
separate. This exporter does not inspect footage, record audio, interview audiences,
collect personal data, verify live platforms or operate an approval/audit system.

## Rights and attribution

The root LICENSE is MIT and is copied unchanged. Current RIGHTS.md states that original
Double FW material uses MIT unless an item says otherwise, with copyright © 2026 Double FW
Ltd and attribution to Gareth Ford Williams. README and AGENTS.md refer to RIGHTS.md.
The compiled reference uses the current selected-source rights wording; prior notices
remain in Git history and are not silently relicensed. Consult the current rights
record and specific source notices before reuse. Third-party material retains its own
terms. RNIB/ITC PDFs and programme scripts, recordings, stills and branding assets are not
newly imported. Links do not relicense their targets or imply endorsement. This packaging
check is not an independent rights audit.

## Limitations and source completeness

Source rights, historical ITC qualifications, external references and editorial limits
remain intact. Contribution and change-history guidance now exist at their owning
repository paths. The pack links to canonical sources and claims no absent source-copy
folder. External specifications and research are not independently rechecked. See
provenance.json, record_schema.json and validation_report.json for the selected source
set, exact checkout and limited extraction/publication checks.

## Updates

GitHub is the authoring source. Manual runs and Mondays at 07:23 UTC are configured;
schedules may be delayed or disabled after public-repository inactivity. All approved text
sources and LICENSE are required. New/renamed documents need export-list review. Changed
rights/licence text, missing sources, populated CSV templates or failed checks stop for
review. Source-authoring files are not rewritten.

Seven destination files are managed: README.md, LICENSE, documents.jsonl,
knowledge_chunks.jsonl, provenance.json, record_schema.json and validation_report.json.
Other raw files and .gitattributes are preserved; unmanaged copies are not kept in sync.
Visibility stays unchanged; historical revisions and downloads are not recalled.
Destination: `{target}`. First authenticated publication remains to be checked.

## Loading

```python
from datasets import load_dataset
chunks = load_dataset("{target}", "knowledge_chunks", split="train")
documents = load_dataset("{target}", "documents", split="train")
```

Authenticate for private datasets and pin a revision for reproducible use.
'''
    yaml.safe_load(card.split('---', 2)[1])
    (output/'README.md').write_text(card, encoding='utf-8')
    report = {'status': 'passed', 'scope': 'faithful extraction and packaging checks only', 'source_commit': sha,
        'source_files_verified': len(manifest), 'document_records': len(docs), 'knowledge_section_records': len(chunks),
        'source_warnings': warnings, 'independent_content_review': False, 'live_publication_tested': False,
        'export_file_sha256': {name: digest((output/name).read_bytes()) for name in MANAGED if name != 'validation_report.json'}}
    write_json('validation_report.json', report)
    return report

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    print(json.dumps(build(ROOT, args.output)))

if __name__ == '__main__':
    main()
