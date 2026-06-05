# research-wide-subagent-marker-fanout

**Mode**: research  ·  **Effort**: wide

## Request

> Find robust marker genes for FOUR Sst sub-classes in mouse V1 using the Tasic 2018 v1_neurons_proc.h5ad: (i) Sst_Calb2_Pdlim5, (ii) Sst_Hpse_Cbln4, (iii) Sst_Myh8, (iv) Sst_Chrna2. FAN OUT one sub-agent per sub-class — each computes 5 differential markers vs. the other Sst cells using scanpy.tl.rank_genes_groups (method='wilcoxon'). Aggregate into a single /work/sst_subclass_markers.csv (subclass, gene, score, pval_adj) and a single /work/sst_subclass_dotplot.png across the union of top markers. The sub-agents run in parallel — that's the point.

## Final summary

## Summary
The parallel fan-out fired all 4 agents simultaneously into the same shared 8 GB sandbox container; the combined RAM draw of four 12 k × 27 k h5ad loads killed the container before most agents could complete. Only **Sst_Calb2_Pdlim5** returned clean markers (Olfm3, Cbln4, Mrap2, Calb2, Ptprd — all p_adj < 10⁻⁴⁵).

## What I did
- Described dataset → confirmed `v1_neurons_proc.h5ad` exists, identified SST cluster names (21 clusters, 1,567 cells)
- Mapped user's 4 sub-class names to exact cluster strings in the data
- Launched 4 parallel sub-agents (one per sub-class); all shared the same Docker container → OOM after first agent's success
- Attempted recovery via a cleanup agent and three sandbox restarts — all blocked by `container is not running`
- **Recovered result for Sst_Calb2_Pdlim5:** Olfm3 (z=16.6), Cbln4 (z=15.7), Mrap2 (z=14.9), Calb2 (z=14.8), Ptprd (z=14.8)

## Caveats / next steps
- **Sandbox container must be restarted** (Docker Desktop on the lab Mac, or `docker start <id>` from the host) before any further analysis can run
- Once restarted, re-trigger this task — I will run all 4 subclasses **sequentially** with `backed='r'` (loads only 1,567 SST cells into RAM instead of the full 12 k, keeping peak RAM < 2 GB) to avoid the OOM
- The parallel fan-out design worked for orchestration but is not safe for this container size with large h5ad files; future multi-subclass tasks should chain sequentially or pre-extract subsets to disk first
