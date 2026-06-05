# research-easy-tasic-celltype-counts

**Mode**: research  ·  **Effort**: standard

## Request

> Count cells per cell type (use the 'cluster' field) in the Tasic 2018 V1 dataset. Produce: /work/celltype_counts.csv (two columns: cell_type, n_cells, sorted descending), and /work/celltype_counts_bar.png (horizontal bar plot of the top 30 types). Use the V1-only object pointed at by the dataset's access snippet.

## Final summary

The sandbox container can't start — the host Mac's Docker daemon is either not running or not on the shell `PATH` used by the bot. The error is:

```
kernel start failed: sandbox-kernel.sh: line 35: docker: command not found
```

This is a **host-side infrastructure issue** I cannot resolve from within the sandbox.

## Summary
The analysis couldn't run because the Docker engine backing the sandbox is unreachable on this machine right now. No code was executed and no output files were produced.

## What I did
- Fetched the dataset card for `tasic2018-v1` — confirmed the right entry point is `/data/tasic2018-v1/v1_all_proc.h5ad` (V1-only, processed); the cluster field will be in `.obs`.
- Attempted to start the sandbox kernel three times; all failed with `docker: command not found`.

## Caveats / next steps
- **Fix Docker first:** on the lab Mac, open Docker Desktop (or run `open -a Docker` in Terminal) and wait for it to fully start (whale icon stops animating). Then retry this request.
- Once Docker is running, the analysis is straightforward:
  1. `adata = ad.read_h5ad("/data/tasic2018-v1/v1_all_proc.h5ad")`
  2. Inspect `.obs.columns` to confirm the cluster column name (likely `cell_cluster` or `cluster` based on prior runs).
  3. `counts = adata.obs["<cluster_col>"].value_counts().reset_index()` → save as `celltype_counts.csv`.
  4. Plot top 30 as horizontal bar → save as `celltype_counts_bar.png`.
- Nothing about the sandbox trust boundary or data access is the blocker — it's purely a Docker availability issue.
