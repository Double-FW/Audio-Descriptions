# Audio Descriptions: human-managed content creation and production activities and prompts

**Prepared:** 8 November 2026 · **Source revision:** `8c0041e26c4410a7d5c5b2881c394168d9be5c87`  
**Source:** [Double-FW/Audio-Descriptions](https://github.com/Double-FW/Audio-Descriptions/tree/8c0041e26c4410a7d5c5b2881c394168d9be5c87)  
**Audience:** authors, editors, designers, publishers, communication teams, producers, commissioners, access-service practitioners and technical/quality partners.

## Where the repository is useful

Use this repository to decide and deliver meaningful access through sound: integrated radio-led scripting, commentary, separate AD, extended versions and associated text routes. Its workflow, editorial and genre guidance, recording/delivery distinctions, QA methods, examples and templates support producers, writers, describers, directors and sound teams.

Not every production needs a separate AD track, but a no-separate-AD decision needs a positive, bounded visual-information audit and final-cut verification. Templates and invented examples are not completed production evidence. Preserve factual information, emotional tone, timing and intended audience knowledge without inventing psychology or identity. RIGHTS.md says no public reuse licence was selected while a root LICENSE is present; retain both notices and leave that inconsistency for the rights owner rather than declaring a new licence.

The activities below are an editorial application of the repository, not a claim that it already contains a complete organisational process. AI can organise material, draft options and scripts, identify inconsistencies and prepare specifications or evidence summaries. Authors and editors preserve factual meaning and editorial intent. Designers and technical practitioners implement and verify delivered formats. Qualified access-service specialists review their work, and affected audiences inform the experience. Accountable publishers/producers retain creative, acceptance, rights and release decisions. Assign these responsibilities to actual people locally; the examples do not establish a new team or approval body.

## How to use the prompts

1. Attach [RAG_Reference.md](RAG_Reference.md). For selective retrieval, use the source routes below and [Source_Coverage.md](Source_Coverage.md).
2. Replace bracketed inputs with the actual project brief, artefacts and evidence. Supply the target task, audience, platform/setting, constraints and intended decision. Treat missing information as unknown.
3. Use either example prompt for the activity. Both refer to this folder’s reference. Supply only appropriate project information; use anonymised research findings where possible.
4. Require source ID, filename and original section citations; distinguish source guidance, local proposal, observed result and uncertainty. Ask for evidence requests where an artefact cannot be inspected.
5. Review the result with the named human roles and record decisions. A prompt output is a draft editorial/production aid, not implementation or evidence that a test ran. Do not defer disabled people’s involvement until final testing.

**Reusable response contract:** “Use the attached RAG_Reference.md as the knowledge source. Cite source IDs, files and sections. Distinguish source statements, project evidence, recommendations and unknowns. Preserve applicable source identifiers. Do not invent research, capability, approvals or test results. Give a concrete content/production artefact, trade-offs, evidence requests and decisions for the human team.”

## Activity map

| Activity | Production stage | Expected output |
| --- | --- | --- |
| 1. Audit visual information and select an access route | Commissioning and access treatment | A visual-information audit and candidate route decision. |
| 2. Write and rehearse audio-first scripts and commentary | Script development and pre-production | An audio-first script/treatment and rehearsal questions. |
| 3. Spot and draft accurate expressive description | AD authoring and editorial development | A candidate cue sheet and editorial decision log. |
| 4. Match genre, information and performance tone | Creative treatment and editorial review | A genre/tone treatment with alternative cue/performance options. |
| 5. Record and mix the intended listening experience | Recording and sound post-production | A recording/mix brief and asset-role manifest. |
| 6. Coordinate described versions with text and captions | Accessible versioning and language coordination | An audio/text/translation dependency matrix. |
| 7. Evaluate understanding, effort and enjoyment | Editorial/technical QA and audience evaluation | A QA/evaluation plan and version-specific findings record. |
| 8. Release, publish and maintain versioned sound access | Production control and publication | A release-decision draft, delivery manifest and change-impact plan. |

## 1. Audit visual information and select an access route

**Production stage:** Commissioning and access treatment

**Retrieve:** [S001 — docs/01-access-route.md](RAG_Reference.md#s001); [S017 — templates/visual-information-audit.csv](RAG_Reference.md#s017); [S015 — templates/commissioning-brief.md](RAG_Reference.md#s015).

**Relevant source sections:** Access-route decision table and audit; commissioning brief.

### Tasks the repository can support

- Compare important visual meaning with the actual soundtrack.
- Choose integrated audio, AD, extended or alternative versions as appropriate.
- Record what a no-separate-AD decision covers and when it needs review.

**Expected output:** A visual-information audit and candidate route decision.

**Human review:** The producer and competent editor/access practitioner decide from actual evidence, including final-cut review.

### Example prompt 1

> Use the attached RAG to assess the access route for [script, visual treatment and available soundtrack evidence]. Audit significant visual information, actions, text, reactions and intended emotion against sound. Propose integrated explanation, separate AD or another appropriate version using the decision table. Do not infer no AD from genre or an unseen cut.

### Example prompt 2

> Challenge [no-separate-AD or AD treatment decision] against the RAG. Identify essential visual gaps, assumptions about the soundtrack and conditions that change after editing. Return a bounded decision record and verification tasks.

## 2. Write and rehearse audio-first scripts and commentary

**Production stage:** Script development and pre-production

**Retrieve:** [S006 — docs/03-radio-led-scripting.md](RAG_Reference.md#s006); [S005 — docs/02-production-workflow.md](RAG_Reference.md#s005); [S001 — docs/01-access-route.md](RAG_Reference.md#s001).

**Relevant source sections:** Radio-led scripting; production workflow.

### Tasks the repository can support

- Make reports, presentations and discussions understandable by listening.
- Name relevant speakers, actions and practical information naturally.
- Leave room for meaningful sound, pace and editorial emphasis.

**Expected output:** An audio-first script/treatment and rehearsal questions.

**Human review:** The writer/director and producer verify facts and delivery; the finished visuals are still audited.

### Example prompt 1

> Using the RAG’s radio-led scripting guidance, adapt [presentation, reportage, panel or commentary script] to work through listening. Include relevant names, roles, actions, demonstrations and visual evidence naturally, protect meaningful sound and avoid unnecessary repetition. Preserve supplied facts and mark what needs a visual or production check.

### Example prompt 2

> Review [audio-first script] against the RAG. Identify unexplained visual references, panel reactions that alter meaning and commentary crowded by nonessential detail. Propose a rehearsable revision and a post-edit audit plan.

## 3. Spot and draft accurate expressive description

**Production stage:** AD authoring and editorial development

**Retrieve:** [S007 — docs/04-ad-editorial-principles.md](RAG_Reference.md#s007); [S012 — examples/editorial-examples.md](RAG_Reference.md#s012); [S013 — templates/ad-cue-sheet.csv](RAG_Reference.md#s013).

**Relevant source sections:** Editorial principles; worked examples.

### Tasks the repository can support

- Plan cues against audience knowledge, picture and protected sound.
- Prioritise consequential visual meaning over exhaustive detail.
- Preserve identity disclosure, uncertainty and translation intent.

**Expected output:** A candidate cue sheet and editorial decision log.

**Human review:** A competent describer/editor verifies the full cut, details and timing; no cue is final from an unavailable image or transcript alone.

### Example prompt 1

> Use the RAG to draft candidate AD for [approved visual evidence, cut/timecodes and soundtrack windows]. Prioritise information by consequence, preserve reveal timing and ambiguous meaning, verify names/text/numbers and use specific active language. Mark uncertain visual details for review; do not infer diagnosis, identity or hidden psychology. Populate relevant cue-sheet fields.

### Example prompt 2

> Challenge [AD script] using the RAG. Identify unsupported emotional conclusions, premature identity reveals, inaccurate text/translation and detail crowding out the action. Propose source-grounded revisions and evidence questions.

## 4. Match genre, information and performance tone

**Production stage:** Creative treatment and editorial review

**Retrieve:** [S008 — docs/05-genre-and-tone.md](RAG_Reference.md#s008); [S007 — docs/04-ad-editorial-principles.md](RAG_Reference.md#s007); [S012 — examples/editorial-examples.md](RAG_Reference.md#s012).

**Relevant source sections:** Genre and tone; emotion without invented psychology.

### Tasks the repository can support

- Preserve practical information in factual material.
- Use emotional rhythm, humour and atmosphere appropriate to the scene.
- Review sensitive material respectfully without flattening creative intention.

**Expected output:** A genre/tone treatment with alternative cue/performance options.

**Human review:** The director, describer and editor review tone in context; relevant audience evidence informs unfamiliar or experimental treatments.

### Example prompt 1

> Using the RAG, develop an AD tone treatment for [genre and scene evidence]. State essential information, emotional rhythm, protected jokes/sound and respectful language. Offer cue/performance options grounded in what the scene actually shows. Use entertainment examples as illustrations, not permission to copy another programme’s voice or make participants the joke.

### Example prompt 2

> Review [genre-specific AD treatment] against the RAG. Identify factual instructions sacrificed to flourish, comedy revealing the payoff early and emotion invented beyond the scene. Propose alternatives and audience questions.

## 5. Record and mix the intended listening experience

**Production stage:** Recording and sound post-production

**Retrieve:** [S009 — docs/06-recording-and-delivery.md](RAG_Reference.md#s009); [S007 — docs/04-ad-editorial-principles.md](RAG_Reference.md#s007).

**Relevant source sections:** Recording/delivery: before recording, performance, mix and asset roles.

### Tasks the repository can support

- Confirm cue versions, pronunciation and protected windows.
- Test the recorded read and revise overfull cues.
- Keep narration stems, complete mixes and player-mixed assets distinct.

**Expected output:** A recording/mix brief and asset-role manifest.

**Human review:** The narrator/director and sound specialists verify the actual performance, measurements and destination requirements.

### Example prompt 1

> Use the RAG to brief recording and mixing for [cut, script and destination]. Confirm pronunciation, timecode, cues, protected dialogue/sound/silence, pickups and listening conditions. Distinguish narration stem, complete AD mix and player-mixed assets. Request current destination loudness/channel specifications instead of inventing universal mix targets.

### Example prompt 2

> Challenge [recording/mix review] with the RAG. Identify word rate used as proof of natural delivery, narrator loudness erasing scene clues and an AD stem labelled as a complete experience. Return concrete checks and revision scope.

## 6. Coordinate described versions with text and captions

**Production stage:** Accessible versioning and language coordination

**Retrieve:** [S009 — docs/06-recording-and-delivery.md](RAG_Reference.md#s009); [S007 — docs/04-ad-editorial-principles.md](RAG_Reference.md#s007); [S016 — templates/release-and-decision-record.md](RAG_Reference.md#s016).

**Relevant source sections:** Recording/delivery: Caption and transcript coordination; editorial text/translation.

### Tasks the repository can support

- Include added narration in appropriate matching text routes.
- Resolve spoken translations, dialogue and AD collisions.
- Keep extended cuts and associated assets correctly retimed.

**Expected output:** An audio/text/translation dependency matrix.

**Human review:** AD, caption, localisation and production owners verify exact version relationships and language access.

### Example prompt 1

> Using the RAG, coordinate [integrated or separately described version] with captions, descriptive transcript and translations. State which narration belongs in which text track, speaker distinctions, timing impacts and platform support to verify. Preserve deliberately untranslated speech and essential visible subtitles according to the production’s intended audience knowledge.

### Example prompt 2

> Review [described-version delivery plan] against the RAG. Find added AD absent from text, a transcript used as a substitute for required synchronised description and captions left on an earlier cut. Produce corrected dependencies and specialist decisions.

## 7. Evaluate understanding, effort and enjoyment

**Production stage:** Editorial/technical QA and audience evaluation

**Retrieve:** [S010 — docs/07-evaluation-and-qa.md](RAG_Reference.md#s010); [S014 — templates/audience-evaluation.md](RAG_Reference.md#s014); [S016 — templates/release-and-decision-record.md](RAG_Reference.md#s016).

**Relevant source sections:** Evaluation and QA: three complementary reviews.

### Tasks the repository can support

- Review every cue against actual picture and sound.
- Keep technical, editorial and audience evidence distinct.
- Assess cumulative comprehension, listening effort and enjoyment.

**Expected output:** A QA/evaluation plan and version-specific findings record.

**Human review:** Editors and technical practitioners review each release; blind/partially sighted audience evidence is planned proportionately and honestly reported.

### Example prompt 1

> Use the RAG to plan review of [AD treatment and production version]. Separate editorial QA, technical checks and audience evaluation; cover all essential cues, protected sound, accuracy and matching assets. Plan relevant varied participants, usual access methods, understanding, effort, orientation and enjoyment without inventing a universal pass percentage.

### Example prompt 2

> Challenge [AD acceptance evidence] with the RAG. Identify specialist review called audience validation, prior programme knowledge concealing omissions and a mean satisfaction score hiding serious confusion. Produce bounded conclusions and corrective/retest actions.

## 8. Release, publish and maintain versioned sound access

**Production stage:** Production control and publication

**Retrieve:** [S005 — docs/02-production-workflow.md](RAG_Reference.md#s005); [S009 — docs/06-recording-and-delivery.md](RAG_Reference.md#s009); [S016 — templates/release-and-decision-record.md](RAG_Reference.md#s016); [S004 — RIGHTS.md](RAG_Reference.md#s004).

**Relevant source sections:** Production workflow; delivery/publication; release record.

### Tasks the repository can support

- Link access decisions, rights, source cuts and delivery roles.
- Verify real discovery and playback after transcode/publication.
- Control re-edits, live-to-on-demand changes and archive relationships.

**Expected output:** A release-decision draft, delivery manifest and change-impact plan.

**Human review:** The accountable producer and rights owner decide release/reuse; actual playback evidence remains separate from file acceptance.

### Example prompt 1

> Using the RAG, prepare a release record for [access version and evidence]. Link cut/runtime/timecode, language, asset roles, captions/transcript, specification, rights references, QA and unresolved findings. Plan authorised discovery/selection/seek/resume checks in the published path and identify what remains outstanding.

### Example prompt 2

> Review [re-edit, live recording or redelivery proposal] against the RAG. Identify stale cues, mismatched text assets, unsupported receiver mixing and rights assumed from picture ownership alone. Produce affected-asset checks and decisions without publishing or asserting a resolved licence.

## Editorial and production decision record

For each adopted result, record the project/task, source revision and sections used, observed editorial/production issue, barrier or opportunity, chosen option and rejected alternatives, expected outcome, evidence available, assumptions, unresolved constraints, accountable person, next check and review trigger. Use actual names and dates when agreed; leave them unassigned when unknown. Record acceptance and residual risk only when the accountable person has made the decision.

Revisit the reference when repository sources change, a new platform or context is introduced, implementation changes invalidate assumptions, or user feedback exposes a barrier. Compare changed sources rather than silently replacing the basis of existing decisions.
