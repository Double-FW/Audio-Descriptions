# Weekly Audio Description dataset updates

Source: https://github.com/Double-FW/Audio-Descriptions

Destination: https://huggingface.co/datasets/GarethFW/Audio_Description

The destination is fixed in export-config.json. No HF_DATASET_ID variable is needed.
Save a destination-scoped Hugging Face token as repository secret HF_TOKEN, then
create .github/workflows/huggingface-sync.yml using WORKFLOW_TO_COPY.txt from the
setup download. Run it manually once and check the result. Weekly runs are
Mondays at 07:23 UTC. Never commit credentials; copy tokens with the copy button.

The RAG reference remains a dated snapshot. Weekly sync does not regenerate it.
Blank CSV templates are document-only; adding production rows requires review.
All approved sources are required; new/renamed sources and changed rights notices
need configuration review. Export checks do not establish editorial approval,
audience evidence or a working playback/production service.
