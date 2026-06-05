# research-easy-tasic-celltype-counts

**Mode**: research  ·  **Effort**: standard

## Request

> Count cells per cell type (use the 'cluster' field) in the Tasic 2018 V1 dataset. Produce: /work/celltype_counts.csv (two columns: cell_type, n_cells, sorted descending), and /work/celltype_counts_bar.png (horizontal bar plot of the top 30 types). Use the V1-only object pointed at by the dataset's access snippet.

## Final summary

Both outputs are clean and correct. Here's the wrap-up:

## Summary
Loaded the V1-only Tasic 2018 object (`v1_all_proc.h5ad`, 13,586 cells) and counted cells across all 118 `cell_cluster` types. The most abundant type is **L4 IT VISp Rspo1** (1,350 cells), and the rarest types have just 1 cell each (mostly ALM contamination cells). Both output files are saved to `/work`.

## What I did
- Loaded `/data/tasic2018-v1/v1_all_proc.h5ad` — 13,586 V1 cells × 27,505 genes, 118 unique clusters
- Used `cell_cluster` obs column (confirmed as the correct "cluster" field per the dataset card)
- **`/work/celltype_counts.csv`** — 118 rows, columns `cell_type` + `n_cells`, sorted descending (max=1,350, min=1)
- **`/work/celltype_counts_bar.png`** — horizontal bar chart of top 30 types, bars colored by cell class (red=GABAergic, blue=Glutamatergic, green=Non-neuronal), count labels on each bar

## Caveats / next steps
- A handful of low-count types (n=1–4) appear to be **ALM-origin** cells that slipped into the V1 object (e.g. `L6 IT ALM Tgfb1`). The V1 object is not 100% VISp-pure — worth filtering to `dissected_region == 'VISp'` if strict V1-only counts are needed (would drop ~130 cells).
- The `cell_cluster` field uses the full Tasic taxonomy names; if you need t-type short names for a figure, the `cell_subclass` column is available as a coarser grouping.
