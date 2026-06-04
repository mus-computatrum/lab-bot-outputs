# Run `79a2487bf55e` — research

**When (UTC):** 2026-06-04 04:52:12
**Datasets:** `v1dd`

## Request

> [bench:research-v1dd-connectivity-top-cells] Using the v1dd connectivity extension at /data/v1dd/extensions/, load synapses_from_axon_proofread.parquet + neurons_soma_model.parquet + proofreading_status_and_strategy.parquet. For the 10 axon-proofread cells with the most outgoing synapses, save /work/v1dd_top_axon_proofread.csv (columns: pre_pt_root_id, n_outgoing_syn, soma_x, soma_y, soma_z) and a horizontal bar plot at /work/v1dd_top_synapse_counts.png.

## Summary

All done! Both artifacts are saved and validated.

## Summary
From the V1DD EM connectome, I identified the 1,273 axon-proofread cells (`status_axon = True`), counted their outgoing synapses in the 3.5M-row synapse table, and extracted soma coordinates for the top 10. The busiest cell (`864691132668098833`) drives **15,494 outgoing synapses**, and the top 10 all exceed 13,000 — a fairly tight band suggesting these are all large, highly connected neurons (likely excitatory pyramidal cells given their high output degree).

## What I did
- Loaded `synapses_from_axon_proofread.parquet` (3,506,153 rows), `neurons_soma_model.parquet` (88,030 rows), `proofreading_status_and_strategy.parquet` (3,335 rows)
- Filtered to `status_axon = True` → 1,273 proofread cells, accounting for ~3.1M of the 3.5M synapses
- Counted outgoing synapses per `pre_pt_root_id`, ranked, and took the top 10
- Joined with soma `pt_position` [x, y, z] — all 10 had matches in the soma model
- **`/work/v1dd_top_axon_proofread.csv`** — 10 rows × 5 columns (`pre_pt_root_id`, `n_outgoing_syn`, `soma_x`, `soma_y`, `soma_z`)
- **`/work/v1dd_top_synapse_counts.png`** — horizontal bar chart, color-coded by count

## Caveats / next steps
- Soma coordinates are in **voxel units** (not nm); multiply by the dataset voxel resolution (typically 8×8×30 nm for V1DD) to get physical distances
- The synapse table includes all valid synapses (`valid` column not filtered) — applying a `valid == True` filter would reduce counts slightly
- Cell type labels were not assigned here; cross-referencing `cell_type_multifeature_v1.parquet` could reveal whether these are L2/3 PCs, L5 PCs, etc.
- `strategy_axon` values (`axon_fully_extended` vs `axon_partially_extended`) are mixed in the top 10, so synapse counts are not fully comparable across cells

## Files

- [`code/_cell_0001.py`](./code/_cell_0001.py)
- [`code/_cell_0002.py`](./code/_cell_0002.py)
- [`code/_cell_0003.py`](./code/_cell_0003.py)
- [`code/_cell_0004.py`](./code/_cell_0004.py)
- [`code/_cell_0005.py`](./code/_cell_0005.py)
- [`code/_cell_0006.py`](./code/_cell_0006.py)
- [`code/_cell_0007.py`](./code/_cell_0007.py)
- [`code/_cell_0008.py`](./code/_cell_0008.py)
- [`figures/v1dd_top_synapse_counts.png`](./figures/v1dd_top_synapse_counts.png)
- [`summary.md`](./summary.md)
- [`tables/.kernel.json`](./tables/.kernel.json)
- [`tables/v1dd_top_axon_proofread.csv`](./tables/v1dd_top_axon_proofread.csv)
