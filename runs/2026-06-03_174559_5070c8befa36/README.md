# Run `5070c8befa36` — research

**When (UTC):** 2026-06-03 17:45:59
**Datasets:** `tasic2018-v1`

## Request

> [bench:research-hard-sst-v1-vs-alm-markers] Using the Tasic 2018 dataset (both V1/VISp and ALM cells), compare expression of the SST-subtype markers Calb2, Crh, Hpse, Nos1, Pdyn, and Chrna2 between V1 and ALM in SST-class interneurons. Produce: /work/sst_subtype_markers_v1_vs_alm.csv (mean log-expression per cell-type × region for each marker), and /work/sst_subtype_dotplot.png (scanpy/seaborn dot plot showing marker × region × cell-type, fraction-expressing as dot size, mean expression as color). Caveats section should name any markers that look indistinguishable between regions.

## Summary

All three outputs validated. Here's the full picture:

---

## Summary
Analysed 2,551 SST interneurons from the Tasic 2018 dataset (1,567 VISp, 984 ALM) across 21 transcriptomic subtypes. Raw counts were CPM-normalised and log1p-transformed; mean expression and fraction expressing were computed per cluster × region for all six markers. **None of the six markers is indistinguishable between VISp and ALM** — all show meaningful cluster-level differences. The markers with the strongest regional signals are **Pdyn** (max Δmean = 1.62, highest in VISp) and **Chrna2** (max Δfrac = 0.69, much lower in ALM *Sst Chrna2 Glra3*). **Hpse** is the most region-stable on average (avg Δmean = 0.031), though its defining clusters express it consistently in both regions.

## What I did
- Loaded `tasic2018_full_counts.h5ad` (23,178 cells × 45,768 genes); confirmed obs columns (`dissected_region`, `cell_subclass`, `cell_cluster`)
- Filtered to 2,551 SST (`cell_subclass == 'Sst'`); verified all 6 marker genes present
- Manual CPM normalisation + log1p on the SST subset
- Computed per-(cluster × region) mean log-expression and fraction-expressing → **`/work/sst_subtype_markers_v1_vs_alm.csv`** (41 rows × 15 cols)
- Built a two-panel dot plot (VISp | ALM), dot size = √(fraction expressing), dot colour = mean log-CPM+1 (Reds scale), open grey circles where a cluster is absent in that region → **`/work/sst_subtype_dotplot.png`**
- Ran indistinguishability test (max Δmean < 0.2 AND max Δfrac < 0.05 across 20 shared clusters) → **`/work/sst_subtype_markers_notes.md`**

## Caveats / next steps
- **No marker is indistinguishable** by the stated thresholds. However, *Hpse* has a very low *average* region difference (avg Δmean = 0.031) — it may read as "similar" if one averages across clusters; the max is just above threshold at 0.217.
- *Sst Tac1 Tacr3* is VISp-only (48 cells); shown as open circles in the ALM panel. No ALM-exclusive clusters exist.
- Indistinguishability thresholds (0.2 mean, 0.05 frac) are the ones agreed in the plan; if you want stricter or looser criteria, the CSV contains the full per-cluster numbers to re-threshold by hand.
- Dot plot Y-axis ordering is by VISp Calb2 mean (descending); could alternatively be ordered by dendrogram/hierarchy for a cleaner taxonomy view.

## Files

- [`code/_cell_0001.py`](./code/_cell_0001.py)
- [`code/_cell_0002.py`](./code/_cell_0002.py)
- [`code/_cell_0003.py`](./code/_cell_0003.py)
- [`code/_cell_0004.py`](./code/_cell_0004.py)
- [`code/_cell_0005.py`](./code/_cell_0005.py)
- [`code/_cell_0006.py`](./code/_cell_0006.py)
- [`code/_cell_0007.py`](./code/_cell_0007.py)
- [`code/_cell_0008.py`](./code/_cell_0008.py)
- [`code/_cell_0009.py`](./code/_cell_0009.py)
- [`code/_cell_0010.py`](./code/_cell_0010.py)
- [`code/_cell_0011.py`](./code/_cell_0011.py)
- [`code/_cell_0012.py`](./code/_cell_0012.py)
- [`code/_cell_0013.py`](./code/_cell_0013.py)
- [`code/_cell_0014.py`](./code/_cell_0014.py)
- [`figures/sst_subtype_dotplot.png`](./figures/sst_subtype_dotplot.png)
- [`sst_subtype_markers_notes.md`](./sst_subtype_markers_notes.md)
- [`summary.md`](./summary.md)
- [`tables/.kernel.json`](./tables/.kernel.json)
- [`tables/sst_subtype_markers_v1_vs_alm.csv`](./tables/sst_subtype_markers_v1_vs_alm.csv)
