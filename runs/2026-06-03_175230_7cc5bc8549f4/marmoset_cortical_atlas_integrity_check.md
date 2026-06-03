# Integrity Check: marmoset-cortical-atlas

**File:** marmoset_MTG_Jorstad2023.h5ad  
**SHA256:** `8646351428616ac95df965cd1b0075faa637841c8297b40ea0a21bb265290bd3`  
**Size:** 486 MB  
**Downloaded:** 2026-06-03 17:51 UTC

## Source
- **Paper:** Jorstad NL, Song JHT, Exposito-Alonso D, Suresh H, Castro-Pacheco N, **Krienen FM** et al. "Comparative transcriptomics reveals human-specific cortical features." *Science* 382, 1318–1323 (2023). DOI: [10.1126/science.ade9516](https://doi.org/10.1126/science.ade9516)
- **CellxGene Collection:** https://cellxgene.cziscience.com/collections/4dca242c-d302-4dba-a68f-4c61e7bad553
- **License:** CC BY 4.0

## Matrix
- **Cells:** 75,861  (Callithrix jacchus; 3 donors; all from middle temporal gyrus / MTG)
- **Genes:** 12,897  (human gene symbols via marmoset gene orthologs)
- **dtype:** float32 (normalized + log1p; CellxGene curation)
- **Mean genes/cell:** ~3,917

## Cell-type taxonomy  
Three levels: `Cluster` (103) → `Subclass` (24) → `cell_type` (18 CL-ontology terms)  
Also has `CrossSpeciesCluster` (57) for cross-species comparison.

### First 10 Cluster labels
```
L2/3 IT_1, L2/3 IT_2, L2/3 IT_3, L2/3 IT_4, L2/3 IT_5,
L4 IT_1, L4 IT_2, L5 ET_1, L5 ET_2, L5 IT_1
```

### All 24 Subclass labels (n cells)
| Subclass | Cells |
|----------|-------|
| L2/3 IT | 21,231 |
| L4 IT | 9,683 |
| Astro | 6,771 |
| L5 IT | 5,998 |
| Oligo | 3,870 |
| Sst | 3,393 |
| L6 IT | 3,018 |
| OPC | 2,868 |
| Vip | 2,661 |
| Micro-PVM | 2,473 |
| Pvalb | 2,440 |
| L6 IT Car3 | 2,382 |
| L6 CT | 2,047 |
| L6b | 1,283 |
| Sncg | 948 |
| Lamp5 | 900 |
| L5/6 NP | 791 |
| L5 ET | 693 |
| VLMC | 624 |
| Chandelier | 530 |
| Endo | 508 |
| Lamp5_Lhx6 | 422 |
| Pax6 | 246 |
| Sst Chodl | 81 |

## Candidate comparison (why this dataset was chosen)
| Candidate | Paper | Cells | Region | Files | Notes |
|-----------|-------|-------|--------|-------|-------|
| **Jorstad+Krienen 2023** (chosen) | Science 2023 | 75,861 | MTG | 1 h5ad | Allen Institute taxonomy, CC BY 4.0 |
| Bakken 2021 M1 | Nature 2021 | ~21,712 | Motor cortex | 3 h5ads | Smaller, split by neuron type |
| Ma+Sestan 2023 dlPFC | Science 2023 | 149,467 | dlPFC | 1 h5ad | Larger but no Allen-style cluster labels |
