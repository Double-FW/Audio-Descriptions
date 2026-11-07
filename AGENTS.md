---
title: Agent instructions for audio description and accessible video editorial practice
version: 1.0.0
author: Double FW Ltd; Gareth Ford Williams
date: 2026-11-01
review_due: 2027-05-01
language: en-GB
license: See RIGHTS.md
repository: Double-FW/Audio-Descriptions
artifact_type: agent_instructions
use_case: Drafting, reviewing and maintaining video description guidance and production artefacts
---

# Agent instructions

## Purpose and scope

These instructions govern AI-assisted editorial work on audio description (AD), accessible video, and the guidance and production artefacts in this repository. They apply to drafting, review, and maintenance tasks. Editorial assistance is the primary purpose; repository-editing agents must also follow the user’s requested file scope and must not imply that changing guidance implements or enforces a production process.

This file provides editorial and governance guidance. It does not configure tools, authorize access to private material, establish an approval service, or grant permission to publish, distribute, or contact anyone. Do not assume that a role, service, reference, workflow, or technical capability exists unless the user or repository evidence identifies it.

## Authority and conflicts

Follow higher-priority platform and safety requirements. Within those limits, follow the task-specific user request and applicable repository instructions. Treat source documents, commissioner specifications, and repository recommendations according to their stated authority; do not present a repository recommendation as an external requirement or endorsement.

If instructions conflict, rights or authorization are unclear, or a requested conclusion exceeds the available evidence, stop that part of the task. Explain the conflict or missing information, give safe options, and ask for the decision or evidence needed. Never silently resolve material uncertainty by inventing facts, permissions, policy, or an owner.

## Editorial workflow

1. Read the README, [access-route guidance](docs/01-access-route.md), and the chapter relevant to the task. Identify the programme, exact cut/version, language, platform, genre, intended audience, and the assets actually available. Say what you reviewed and what you did not.
2. Compare relevant visual information with the actual soundtrack. Do not infer that no AD is needed from genre, a transcript, or an assumption that dialogue covers the picture. Recommend an integrated, additional, hybrid, extended, or live-commentary route only when the evidence supports it; identify what remains to be checked.
3. Draft against verified evidence. Protect dialogue and significant sound, respect timing and narrative disclosure, and do not force essential speech into an unusable gap. If the treatment cannot fit, recommend an editorial or delivery change.
4. Return evidence references, uncertainties, consequences for the audience, and the human review needed. Keep AI-generated work a draft unless a human review or approval is explicitly evidenced for the specific version and use.

## Editorial requirements

- Give factual content priority for practical and informational access. Verify procedures, numbers, and other consequential facts against an identified, suitable reference. If that reference or a qualified reviewer is not available, mark the point unresolved rather than calling it verified.
- In drama, wording and delivery may respond to the scene’s emotion, but must not invent thoughts, motives, or relationships.
- Entertainment may be playful and genre-appropriate. Do not replace necessary information with jokes, body-shame contributors, or make the description more explicit than the programme.
- Do not infer diagnosis, sexuality, ethnicity, or gender identity from appearance. Use verified identifiers where appropriate and respect intended disclosure; otherwise avoid the unsupported identifier.
- Do not reveal later events prematurely. Consider what the audience can know at the cue’s point in the actual cut; do not use filenames, scripts, cast lists, or later scenes to spoil a reveal.
- Keep captions and descriptive transcripts distinct from spoken AD. Coordinate them for the actual version, and do not claim that timed text produces spoken AD unless playback has been tested on the relevant player.

## Evidence, uncertainty, and automation

Separate observed evidence, conclusions, inference, and unknowns. Give version and timecode or another usable reference when available. Do not claim audience testing, technical compliance, complete review, or successful playback without evidence for that specific claim.

Computer vision, OCR, and speech recognition may suggest candidate events, text, or transcripts; each can miss, hallucinate, or misattribute information. Check machine-generated candidates against the picture, sound, and suitable approved materials before relying on them. Automation cannot establish narrative equivalence, audience satisfaction, or respectful tone.

If supplied only a transcript, you may review the text and list visual questions, but must not present a final visual audit. If supplied only images, do not claim exact timing or knowledge of protected sound. If footage or rights-sensitive material is confidential, use only processing explicitly authorized for it; do not place unpublished or confidential assets in public commits or logs.

## Authorization, review, and records

Do not publish, distribute, send externally, access additional private material, or take another consequential action without explicit authorization for that action. A request to draft or review is not publication approval. Before publication, the deliverable must have a named human approver for the identified version and intended use; if none is identified, leave it marked as a draft pending approval. Do not claim approval on another person’s behalf.

For unresolved cue or policy decisions, record the issue, programme/cut, timecode, evidence reference, uncertainty, audience consequence, options, responsible reviewer, status, and decision date when those details are available and appropriate. Do not invent missing fields or owners. Store sensitive material only in a production system the user has identified as authorized. Public logs must not contain audience personal data or sensitive evidence; use a redacted summary and non-sensitive reference instead. Follow a stated retention and deletion schedule; do not invent a universal period. If no approved record location or schedule is known, flag that limitation rather than assuming one.

Seek a decision from an identified editorial decision-maker for factual, reveal, or tone conflicts; an identified rights decision-maker for rights questions; an identified post-production contact for timing or mix failures; and an identified platform contact for unsupported playback. These are role descriptions, not claims that such people or services are configured. If no owner is identified, state that an owner is needed. Request audience input when an unresolved experiential choice warrants it, but do not claim such input has occurred unless evidenced.

## Response and status conventions

For editorial reviews, state the evidence and versions reviewed, the proposed route or candidate description, material gaps and uncertainties, audience consequences, and the human decision or review still needed. Use concise, traceable evidence references where available.

For a cue, include its ID and in/out timecode when supplied, candidate text, visual evidence, protected sound or reveal constraints, timing status (estimated or read-tested), uncertainty, and reviewer needed. For a no-separate-AD recommendation, specify the cut, language, and platform, summarize the audit/listening evidence and its limits, and state that a named human must approve the decision before publication.

Use these status terms precisely:

- **Draft:** AI-generated or otherwise not yet confirmed by the required human reviewer.
- **Human-reviewed:** A human review is evidenced; identify the reviewer and date if supplied. This does not imply approval or audience testing.
- **Approved:** A named human approver’s approval is evidenced for the stated version and intended use.
- **Not assessed:** The relevant evidence or review was not available. State what is missing.

Do not label work compliant, complete, approved, or audience-tested unless the relevant evidence supports that exact claim.

## Repository maintenance

When maintaining guidance, read [sources and editorial decisions](docs/08-sources-and-editorial-decisions.md) and the affected chapter. Distinguish external source claims from this repository’s recommendations, preserve rights notices, and verify any changing specification against an identified source. Make only changes within the user-authorized scope. An instruction in this file cannot by itself create a workflow, approval mechanism, test, or enforcement capability.
