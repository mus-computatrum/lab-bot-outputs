## Summary
The largest cortical single-cell ATAC-seq datasets are all **human** — no non-human primate study comes close in scale. The biggest are **Xiong et al. 2025 (Cell)**, ~3.5M cells of paired epigenomic+transcriptomic data across 6 brain regions (incl. neocortex), and a **2026 Parkinson's bioRxiv preprint** with 3.1M snATAC nuclei (anterior cingulate cortex + substantia nigra, 190 donors). **Emani 2024 (Science, PsychENCODE2)** has >2.8M PFC nuclei (ATAC a subset), and **Li et al. 2023 (Science, catlas)** is the largest *dedicated snATAC-only* brain atlas at 1.1M nuclei / 42 regions. For any **non-human primate** cortex, **Zemke et al. 2023 (Nature)** — a macaque + marmoset + human + mouse M1 multiome — is effectively the only large-scale option.

## What I did
- Screened PubMed (2020–2026) for primate cortical snATAC/multiome atlases; pulled species, region, nuclei counts, and data access; verified the Zemke 2023 record via Europe PMC.
- Built a ranked table → `/work/primate_cortex_snATAC_datasets.csv` (10 datasets) and a narrative → `/work/primate_cortex_snATAC_summary.md`.
- Saved a durable lab note cataloguing the top datasets + accessions.

## Caveats / next steps
- "Cell" counts often combine snATAC + snRNA; for multiome atlases (Xiong, Emani, PD preprint) the **snATAC-only** fraction is a subset I could not always isolate from abstracts — confirm in each paper's methods. The PD preprint mixes cortex (ACC) with midbrain (SN).
- Semantic Scholar and web_search were rate-limited/empty this session, so ranking rests on PubMed; a BICAN/Allen ABC chromatin release could add NHP data I didn't capture. Accessions listed conservatively — verify GEO/Synapse IDs before downloading. With more time I'd fetch each methods section to extract exact per-modality, cortex-only nuclei counts.