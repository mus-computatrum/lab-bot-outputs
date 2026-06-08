All artifacts saved. Here's the summary.

## Summary
"Sst44" comes from Green, Hrvatin et al. 2023 *Nature* — it's a **rare, gap-junction–coupled, self-exciting subtype of somatostatin (Sst) interneuron** in mouse posterior parietal cortex (PPC), originally accessed via a Sst-subset–specific enhancer-AAV. To ask whether a homolog exists in primates you need datasets with (1) fine Sst resolution, (2) a cross-species mapping framework, (3) chromatin/multiome data to test conservation of the defining enhancer, and (4) spatial data to localize a candidate to the PPC homolog. I found and verified 13 datasets that collectively cover all four needs.

## What I did
- Confirmed the Sst44 source paper and its biology via live PubMed/NCBI E-utilities (no host web tool was wired this job, so I queried from the sandbox).
- Searched for and verified (DOIs/years/venues) the key primate cortical resources, grouped by usefulness:
  - **Cross-species snRNA-seq (interneuron resolution):** Krienen 2020 *Nature* (top — interneuron-focused, 5 species), Bakken 2021 *Nature* M1 multiome, Jorstad 2023 *Science* (5-primate MTG), Ma 2022 *Science* DLPFC, Hodge 2019, Siletti 2023 (~3M-nuc human atlas), Krienen 2023 marmoset census.
  - **Spatial:** Chen 2023 *Cell* (macaque whole-cortex Stereo-seq, incl. PPC homolog), Fang 2022 *Science* MERFISH, Qian 2025 *Nature*, Lei 2025 *Cell*.
  - **Chromatin/enhancer conservation:** Li 2023 *Science* human ATAC cCRE atlas; Bakken 2021 ATAC/methyl arm.
- Saved `/work/primate_Sst44_datasets.csv` (full table) and `/work/primate_Sst44_dataset_brief.md` (rationale + a 4-step mapping workflow). Added a lab note.

## Caveats / next steps
- I cataloged datasets and DOIs but did not download or re-analyze them; whether Sst44 truly has a primate homolog requires running the mapping (label-transfer/MetaNeighbor of the mouse Sst44 signature → Krienen/Jorstad/Bakken, then ATAC enhancer check, then spatial validation in macaque).
- I could not find a dedicated macaque *cortical* MERFISH paper; Chen 2023 (Stereo-seq) is the best macaque cortical spatial option. With more time I'd pull the exact Sst44 marker set from the Green/Hrvatin supplement to seed the mapping.