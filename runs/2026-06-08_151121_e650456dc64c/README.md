# Run `e650456dc64c` — search-lit

**When (UTC):** 2026-06-08 15:11:21
**Datasets:** _none_

## Request

> Papers on optimizing MERFISH protocol

## Summary

## Summary
The single most on-point paper is **"Protocol optimization improves the performance of multiplexed RNA imaging"** (Sci Rep, 2025; PMID 40887478), which systematically tests probe design, hybridization, buffer storage, and buffer composition to identify performance-improving modifications in both cell culture and tissue. Several adjacent papers optimize specific MERFISH bottlenecks (thick tissue, 3D processing, segmentation, autofluorescence).

## What I did
Searched PubMed (MERFISH protocol optimization / sensitivity / genome-scale imaging). Most relevant hits:

- **PMID 40887478** — *Protocol optimization improves the performance of multiplexed RNA imaging.* Sci Rep (2025). **The direct answer**: systematic sweep of probe design, hybridization, buffer storage/composition; offers empirical design guidance.
- **PMID 39727221** — *Three-dimensional single-cell transcriptome imaging of thick tissues.* eLife (2024). 3D MERFISH up to 200 µm via confocal optical sectioning + deep learning; sample-prep/imaging protocol optimized for thick samples.
- **PMID 41279966** — *GPU-accelerated, self-optimizing processing for 3D iterative RNA-FISH (merfish3d-analysis).* bioRxiv (2025). Reprocessing pipeline + a multi-step autofluorescence-quenching protocol for in situ spatial transcriptomics.
- **PMID 34650268** — *Cell segmentation in imaging-based spatial transcriptomics (Baysor).* Nat Biotechnol (2022). Optimizes cell boundaries; relevant to downstream MERFISH accuracy.
- **PMID 32822575** — *Genome-Scale Imaging of 3D chromatin (MERFISH-based).* Cell (2020). Methodological extension, for context.

## Caveats / next steps
Search-lit mode — I quoted abstracts as returned, didn't fetch full texts or verify DOIs. PMID 41279966 is a preprint (not peer-reviewed). For a deeper dive I'd pull the 40887478 full methods table and search bioRxiv/Semantic Scholar for very recent (2026) protocol papers and Vizgen MERSCOPE app notes.

## Files

- [`result.md`](./result.md)
