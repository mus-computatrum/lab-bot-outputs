# research-easy-tasic-celltype-counts

**Mode**: research  ·  **Effort**: standard

## Request

> Count cells per cell type (use the 'cluster' field) in the Tasic 2018 V1 dataset. Produce: /work/celltype_counts.csv (two columns: cell_type, n_cells, sorted descending), and /work/celltype_counts_bar.png (horizontal bar plot of the top 30 types). Use the V1-only object pointed at by the dataset's access snippet.

## Final summary

All clean. Note: one cluster at the bottom is named "L6 CT ALM Cpa6" but with only 1 cell — this is normal; Tasic cluster names encode the predominant region, and a handful of cross-area types appear in both the VISp and ALM collections.

---

## Summary
Counted cells across all 118 transcriptomic clusters in the Tasic 2018 VISp (V1) dataset (13,586 cells total, from `v1_all_proc.h5ad`). The most abundant type is **L4 IT VISp Rspo1** (1,350 cells), and the rarest types have just 1 cell. A horizontal bar chart of the top 30 types has been saved.

## What I did
- Loaded `/data/tasic2018-v1/v1_all_proc.h5ad` (13,586 cells × 27,505 genes — the dataset's canonical V1-only object)
- Counted cells per `cell_cluster`, sorted descending → **118 unique types**
- Saved **`/work/celltype_counts.csv`** — 2 columns (`cell_type`, `n_cells`), 118 rows, sum verified = 13,586
- Saved **`/work/celltype_counts_bar.png`** — horizontal bar chart of top 30 cell types with count labels

## Caveats / next steps
- One cluster at the bottom (`L6 CT ALM Cpa6`, n=1) has "ALM" in its name — this reflects the Tasic cluster naming convention (named after majority-region), not a filtering error; the cells are confirmed VISp.
- The V1 object has 13,586 cells vs. 23,822 in the full taxonomy; the difference is ALM cells excluded here.
- `v1_all_proc.h5ad` includes all cell classes (excitatory, inhibitory, non-neuronal); use `cell_class` to subset further if needed.
