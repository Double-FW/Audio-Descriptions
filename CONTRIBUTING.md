# Contributing to Audio Descriptions

Use this repository to improve editorial guidance, practical methods and accessible production resources. Begin with the [README](README.md), [agent guidance](AGENTS.md) and [sources and editorial decisions](docs/08-sources-and-editorial-decisions.md).

## Propose a focused change

1. Identify the document, heading and audience consequence of the issue.
2. Explain the proposed correction, its evidence and any uncertainty. Separate current primary-source requirements from historical guidance, repository recommendations and invented examples.
3. Preserve meaningful sound, timing, intended disclosure and respectful representation. Do not infer identity, diagnosis, motives or audience preferences from appearance.
4. Keep programme, participant and other confidential information out of public commits. Use invented examples or material explicitly authorised for public reuse.
5. Update affected navigation and the [changelog](CHANGELOG.md). Keep any changed source's qualifications close to its claims.

## Check the result

Check local links, headings, tables and code fences. Keep CSV production templates blank. Where a source feeding the compiled RAG reference changes, regenerate that reference and its coverage record before publishing; the export checks source hashes and compiled bodies to prevent stale guidance being labelled current.

The [sync setup](huggingface/SETUP.md) describes the existing dataset workflow. Export tests concern faithful extraction and publishing safeguards; they do not review footage, validate playback, evaluate an audience or approve a production. Human editorial and release decisions remain with the actual authorised people for the specific cut and use.

## Rights and attribution

Keep the [MIT copyright and permission notice](LICENSE) and [rights boundaries](RIGHTS.md). Preserve relevant attribution and third-party notices. Do not add third-party scripts, PDFs, recordings, stills or other material without an established right to redistribute it. A public link does not grant that right.
