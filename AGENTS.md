---
title: Agent instructions for audio description and accessible video editorial practice
version: 1.0.0
author: Double FW Ltd; Gareth Ford Williams
date: 2026-11-01
review_due: 2027-05-01
language: en-GB
license: See RIGHTS.md
repository: Audio-Description-and-Accessible-Video-Editorial-Practice
artifact_type: agent_instructions
use_case: Drafting, reviewing and maintaining video description guidance and production artefacts
rules:
  objective: equivalent_understanding_and_enjoyment
  audit_finished_content: required
  genre_exemptions: forbidden
  separate_ad_for_every_video: forbidden
  factual_priority: practical_and_informational_access
  emotion_sensitive_delivery: permitted
  invented_motives: forbidden
  humour: accurate_respectful_and_genre_appropriate
  premature_reveals: forbidden
  unsupported_identity_inference: forbidden
  source_pdf_redistribution: requires_permission
  ai_output_status: draft_until_human_review
  publication_requires_named_approver: true
  audience_data_in_public_logs: forbidden
---

# Agent instructions

## Purpose and scope

Support editorial judgement and production work. Do not represent generated description as approved, audience-tested or technically compliant without evidence. The intended outcome is equivalent access to information, action, atmosphere and pleasure.

## Quick start

1. Read [README](README.md), [access routes](docs/01-access-route.md), and the chapter relevant to the task.
2. Identify the programme, actual cut, language, platform, genre and intended audience. State which source assets you have and have not reviewed.
3. Compare visual information with the soundtrack. Never infer that no AD is needed from genre or a transcript alone.
4. Propose integrated, additional, hybrid, extended or live commentary treatment using the decision table.
5. Draft against actual evidence, protect dialogue and significant sound, and preserve narrative disclosure.
6. Return unresolved uncertainties and review needs. Keep the asset a draft until the appropriate human reviews it.

## Editorial invariants

- Factual content gives practical and informational access priority. Verify technical procedures and numbers with approved references and the responsible specialist.
- Drama may use emotionally responsive wording and performance without inventing thoughts or motives.
- Entertainment may be playful. Do not substitute jokes for necessary information, body-shame contributors or intensify explicitness beyond the programme treatment.
- Never infer diagnosis, sexuality, ethnicity or gender identity from appearance. Verify appropriate identifiers and respect intended disclosure.
- Do not spoil events through filenames, scripts, cast lists or later scenes. The agent may know more than the audience should know at a cue's time.
- Do not force essential speech into an impossible window. Recommend an editorial or delivery change.
- Do not claim that timed text produces spoken AD in an untested player.
- Keep captions and descriptive transcripts distinct from audio description; coordinate them for the actual version.

## Evidence and automation limits

Computer vision may help identify candidate visual events, OCR may extract text, and speech recognition may create a rough transcript. Each can miss, hallucinate or misattribute content. Check candidates against the picture, sound and approved materials. No automated model can certify narrative equivalence, audience satisfaction or respectful tone.

If only a transcript is supplied, review the audio script and list visual questions; do not produce a final visual audit. If only images are supplied, do not infer exact timing or protected sound. If the footage or rights are confidential, use only approved processing services and keep unpublished assets out of public commits.

## Decision and escalation record

For each unresolved cue or policy conflict, record: issue ID, programme/cut, timecode, evidence reference, uncertainty, audience consequence, proposed options, responsible reviewer, status and decision date. Store personal details, private footage and sensitive evidence in the authorised production system. Public logs should contain only redacted summaries and non-sensitive references. Follow the project's agreed retention and deletion schedule; do not invent a universal retention period.

Escalate material factual uncertainty to the editorial lead or subject specialist; reveal and tone conflicts to the AD editor; rights to the responsible rights owner; timing/mix failures to post-production; unsupported playback to the platform owner. Request audience input for unresolved experiential choices. Do not quietly turn missing evidence into an assertion.

## Response templates

**Access-route review**

> Evidence reviewed: [assets and versions]. Relevant visual gaps: [items or unknowns]. Proposed route: [route]. Reason: [audience outcomes]. Human review: [owner]. Remaining evidence needed: [specific gap]. Status: draft / reviewed.

**Cue review**

> Cue [ID], [in–out]: [candidate text]. Visual evidence: [reference]. Protected sound/reveal: [constraint]. Timing: estimated / read-tested. Uncertainty: [detail]. Reviewer: [role].

**No-separate-AD decision draft**

> For [cut/language/platform], [audit and listening evidence] indicates the main audio communicates the relevant visual content. [Named reviewer] must confirm this decision. Re-audit after [change triggers]. This does not certify other access workstreams.

## Maintenance

Read [source decisions](docs/08-sources-and-editorial-decisions.md) before changing a rule. Separate external source claims from new recommendations. Verify changing specifications for an actual delivery. Update [CHANGELOG](CHANGELOG.md), metadata and affected examples together. Review after significant source revisions, a new destination or evidence of recurring audience barriers; the date in metadata is a maintenance target, not an automated trust guarantee.
