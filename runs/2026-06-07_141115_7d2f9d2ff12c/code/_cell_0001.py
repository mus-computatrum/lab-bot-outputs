content = '''# Bugeon et al. 2022 — Three-level cell-type hierarchy

**Paper:** Bugeon, S. et al. "A transcriptomic axis predicts state modulation of cortical interneurons." *Nature* 607, 330–338 (2022). doi:10.1038/s41586-022-04915-7 (PMC9279161; PMID 35794483).

## The three levels
The authors classify cortical inhibitory neurons (in V1 layers 1–3) into a **three-level hierarchy**:

1. **Subclass** (top level) — 5 groups
2. **Type** (intermediate level) — 11 types
3. **Subtype** (lowest level) — 35 subtypes

## Verbatim quotes (from the open-access PMC full text)

> "We classified inhibitory neurons imaged in layers 1–3 into a three-level hierarchy of 5 subclasses, 11 types and 35 subtypes using previously defined transcriptomic clusters." (Abstract)

> "We classified these inhibitory cells using a three-level hierarchy (Fig. 1f). The lowest hierarchical level ('subtype') comprised the fine transcriptomic clusters defined previously, and the top level ('subclass') was the Pvalb, Sst, Lamp5, Vip and Sncg groupings that were defined in the same previous report. An intermediate level ('type') was suggested by uniform manifold approximation and projection (UMAP) analysis of scRNA-seq data, which revealed collections of clusters that we could putatively associate to morphological cell types." (Results, "Identifying recorded inhibitory subtypes")

## Names of the levels
- **5 subclasses:** Pvalb, Sst, Lamp5, Vip, Sncg
- **11 types:** Pvalb-Tac1 (putative Pvalb basket cells); Pvalb-Vipr2 (putative chandelier cells); Sst-Reln (putative Martinotti cells); Sst-Tac1 (putative non-Martinotti Sst cells); Lamp5-Npy (putative neurogliaform cells); Lamp5-Tmem182 (putative canopy cells); Lamp5-Chrna7 (putative layer-1 alpha7 cells); Vip-Reln (putative layer-1 Vip cells); Vip-Cp (other Vip cells); Sncg-Pdzrn3 (putative large Cck cells); Sncg-Vip (putative small Cck/Vip cells)
- **35 subtypes:** the fine scRNA-seq transcriptomic clusters (from Tasic et al. 2018, ref 3) that fell in the superficial imaged layers.

*Source: NCBI eFetch PMC full-text XML for PMC9279161, retrieved 2026-06-07.*
'''
with open('/work/bugeon_hierarchy.md','w') as f:
    f.write(content)
print(content)
