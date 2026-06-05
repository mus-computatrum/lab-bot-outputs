# Run `28f75704fbaa` — research

**When (UTC):** 2026-06-05 03:13:51
**Datasets:** `tasic2018-v1`

## Request

> [bench:research-easy-tasic-celltype-counts] Count cells per cell type (use the 'cluster' field) in the Tasic 2018 V1 dataset. Produce: /work/celltype_counts.csv (two columns: cell_type, n_cells, sorted descending), and /work/celltype_counts_bar.png (horizontal bar plot of the top 30 types). Use the V1-only object pointed at by the dataset's access snippet.

## Summary

The sandbox container cannot start — Docker is not found on the host (`docker: command not found`). This is an infrastructure issue on the lab Mac, not a problem with the analysis code. I cannot execute any computation until Docker is running.

## Summary
The analysis cannot run right now because the Docker daemon is not available on the lab Mac. All sandbox execution goes through Docker, and the shell is reporting `docker: command not found`.

## What I did
- Fetched the dataset card for `tasic2018-v1` ✅ — confirmed the right entry-point file is `v1_all_proc.h5ad` and the cluster field is present in `.obs`.
- Attempted to start the sandbox kernel twice — both failed with the same `docker: command not found` error.
- No files were written to `/work` (nothing to write without a working kernel).

## Caveats / next steps
- **Fix needed:** Docker Desktop (or the Docker Engine daemon) needs to be launched on the lab Mac before any sandbox jobs can run. On macOS, open Docker Desktop from Applications and wait for it to show "Docker is running."
- Once Docker is back up, this job is straightforward and fast: load `v1_all_proc.h5ad`, call `adata.obs["cell_cluster"].value_counts()`, dump to CSV, and render a horizontal bar chart of the top 30 — ~30 seconds of compute.
- The dataset card confirms the V1-only object is at `/data/tasic2018-v1/v1_all_proc.h5ad` and the cluster column to use is `cell_cluster` (consistent with prior job notes).

## Files

- [`summary.md`](./summary.md)
