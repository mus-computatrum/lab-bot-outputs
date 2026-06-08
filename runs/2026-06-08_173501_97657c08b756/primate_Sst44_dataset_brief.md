# Primate cortical datasets for testing whether mouse "Sst44" cells exist in other species

**Source of Sst44.** Green J, Bruno CA, Traunmüller L, Ding J, Hrvatin S, et al. (2023)
*A cell-type-specific error-correction signal in the posterior parietal cortex.* Nature 620:366-373.
doi:10.1038/s41586-023-06357-1. Sst44 is a rare, molecularly defined subset of somatostatin (Sst)
GABAergic interneurons in mouse posterior parietal cortex (PPC), accessed via a Sst-subset-specific
**enhancer-AAV** (enhancer toolkit lineage: Hrvatin et al. 2019 eLife, doi:10.7554/eLife.48089), that
forms a **gap-junction-coupled self-excitation circuit** carrying a navigation error-correction signal.

## What a dataset needs to answer "does Sst44 exist in primates?"
1. **Fine Sst resolution** — deep snRNA-seq or interneuron-enriched sampling so a rare Sst subtype is resolvable.
2. **Cross-species framework** — already maps mouse <-> primate types (consensus taxonomy / label transfer).
3. **Chromatin/multiome** — to test whether the *cis-regulatory enhancer* defining Sst44 is conserved and
   accessible in the homologous primate Sst type (the basis for re-deriving viral access in NHP/human).
4. **Spatial transcriptomics** — to localize a putative homolog to the PPC/intraparietal homolog and check the
   clustered/gap-junction spatial signature (connexin/Gjd2 co-expression).

## Recommended datasets (full table: primate_Sst44_datasets.csv)

### A. Cross-species snRNA-seq with interneuron resolution (best for direct mapping)
- **Krienen et al. 2020 Nature** — *Innovations present in the primate interneuron repertoire* (marmoset, macaque,
  human, ferret, mouse). Interneuron-focused; **top priority** for orthology of a fine Sst type.
- **Bakken et al. 2021 Nature** — BICCN M1, human/marmoset/mouse, **multimodal (RNA+ATAC+methyl+Patch-seq)**.
- **Jorstad et al. 2023 Science** — five-primate MTG (human, chimp, gorilla, macaque, marmoset) consensus taxonomy + MERFISH.
- **Ma et al. 2022 Science** — DLPFC across four primates, snRNA + spatial.
- **Hodge et al. 2019 Nature** — human MTG taxonomy vs mouse (foundational reference).
- **Siletti et al. 2023 Science** — ~3M-nucleus adult human brain atlas, many neocortical areas incl. parietal (power to detect rare types).
- **Krienen et al. 2023 Sci Adv** — marmoset brain-wide cell census (tractable NHP model).

### B. Spatial transcriptomics (localize the homolog)
- **Chen et al. 2023 Cell** — macaque whole-cortex Stereo-seq (143 areas incl. parietal/PPC homolog). Key for PPC localization.
- **Fang et al. 2022 Science** — human + mouse cortical MERFISH (cross-species spatial template).
- **Qian et al. 2025 Nature** — human cortical layer/area spatial specification.
- **Lei et al. 2025 Cell** — macaque claustrum spatial+connectivity (secondary).

### C. Multi-omics / chromatin (test enhancer conservation)
- **Li et al. 2023 Science** — human brain single-cell ATAC cCRE atlas (~1.1M nuclei). Test conservation/accessibility of the Sst44 enhancer.
- **Bakken et al. 2021 (ATAC/methyl arm)** — cross-species chromatin in homologous GABAergic types.

## Suggested workflow
1. Define Sst44's transcriptomic signature from the Green/Hrvatin mouse data (markers + the enhancer locus).
2. Label-transfer / MetaNeighbor against Krienen 2020 + Jorstad 2023 + Bakken 2021 to find a reciprocal-best primate match.
3. Confirm chromatin: is the orthologous enhancer present + accessible in that primate Sst type (Li 2023 / Bakken ATAC)?
4. Spatially validate in macaque (Chen 2023) / human (Fang 2022, Qian 2025): does the candidate localize to the PPC homolog and co-express gap-junction genes (e.g., GJD2)?

*All DOIs verified live against PubMed/NCBI E-utilities on 2026-06-08.*
