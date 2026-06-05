# research-easy-tasic-celltype-counts

**Mode**: research  ·  **Effort**: standard

## Request

> Count cells per cell type (use the 'cluster' field) in the Tasic 2018 V1 dataset. Produce: /work/celltype_counts.csv (two columns: cell_type, n_cells, sorted descending), and /work/celltype_counts_bar.png (horizontal bar plot of the top 30 types). Use the V1-only object pointed at by the dataset's access snippet.

## Final summary

The sandbox container can't start — the host Mac is reporting `docker: command not found`. This means Docker Desktop is not running (or not in the PATH the bot uses).

**What you need to do:**
1. Open Docker Desktop on the lab Mac and make sure it's fully started (the whale icon in the menu bar should be steady, not animated).
2. Once Docker is up, re-send this request and I'll run the analysis automatically.

The analysis itself is straightforward and ready to go — I'll:
- Load `/data/tasic2018-v1/v1_all_proc.h5ad` (the V1-only object from the dataset card)
- Count cells per `cluster` (or whatever the cluster-label column is named in that object)
- Write `/work/celltype_counts.csv` (sorted descending)
- Plot a horizontal bar of the top 30 types → `/work/celltype_counts_bar.png`

## Summary
The sandbox container failed to start because Docker is not running on the lab Mac. No data was read and no outputs were produced.

## What I did
- Fetched the Tasic 2018 dataset card — confirmed the V1-only entry point is `/data/tasic2018-v1/v1_all_proc.h5ad`.
- Attempted to launch the IPython kernel; received `docker: command not found` on both tries.

## Caveats / next steps
- **Start Docker Desktop** on the lab Mac, then re-submit this request.
- Once Docker is up, the full analysis (CSV + bar plot) will run end-to-end in under a minute.
- The cluster label column name in `v1_all_proc.h5ad` needs a quick `adata.obs.columns` check (my prior jobs used `cell_cluster` on the full object; the V1 proc object may use the same or a slightly different name — I'll verify on first run).
