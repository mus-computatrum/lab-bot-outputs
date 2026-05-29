# Run `3d55d7fdae1f` — code

**When (UTC):** 2026-05-29 11:54:31
**Datasets:** _none_

## Request

> Visualize the proportions of different cell-types in VISp vs. ALM using bar plots.

## Summary

All outputs are in good shape. Here's the full picture:

---

## Summary
I used the **Tasic et al. 2018** scRNA-seq dataset (23 k cells from VISp and ALM) to compute and plot the proportions of every cell-type subclass in each region. After filtering out low-quality and unclassified cells (n = 13,825 VISp; 8,288 ALM), I produced two bar-chart figures highlighting striking regional differences — most notably that **L5 IT glutamatergic neurons** dominate ALM (~26 %) but are rare in VISp (~6 %), while **L4 neurons** are abundant in VISp (~10 %) and nearly absent in ALM.

## What I did
- Loaded `/data/tasic2018-v1/tasic2018_full_counts.h5ad` and extracted `dissected_region`, `cell_subclass`, and `cell_class` metadata.
- Dropped "Low Quality" and "No Class" cells; kept 21 subclasses present at ≥ 0.3 % mean proportion.
- Computed within-region proportions for each subclass.
- **`/work/celltype_proportions_VISp_ALM.png`** — two stacked panels (VISp on top, ALM below), bars coloured by cell class (orange = Glutamatergic, blue = GABAergic, green = Non-Neuronal, purple = Endothelial).
- **`/work/celltype_proportions_VISp_ALM_sidebyside.png`** — all subclasses side-by-side with VISp (solid) and ALM (hatched) bars for direct comparison.
- **`/work/celltype_proportions.csv`** — numeric proportion table for downstream use.

## Caveats / next steps
- Proportions reflect **sampled cells**, which depends on the Cre-line targeting strategy used in each region; some subclasses may be over- or under-represented relative to true biology.
- Statistical significance of regional differences (e.g., chi-squared or permutation test) was **not** computed — consider adding that next.
- The `High Intronic` and `Serpinf1` subclasses were excluded (< 0.3 % mean); they can be re-included by lowering the threshold in the script.

## Files

- [`figures/celltype_proportions_VISp_ALM.png`](./figures/celltype_proportions_VISp_ALM.png)
- [`figures/celltype_proportions_VISp_ALM_sidebyside.png`](./figures/celltype_proportions_VISp_ALM_sidebyside.png)
- [`tables/celltype_proportions.csv`](./tables/celltype_proportions.csv)

_Job cost: $0.1997_