# Run `7cc5bc8549f4` — download

**When (UTC):** 2026-06-03 17:52:30
**Datasets:** _none_

## Request

> [bench:download-marmoset-atlas] Find and register a marmoset cortical cell-type single-cell atlas comparable to Tasic 2018 (mouse). Good candidates include the Krienen et al. 2023 Nature marmoset cortex dataset and the Bakken et al. 2021 primate PFC/cortex dataset; pick the one with the cleanest cell-type taxonomy + accessible counts + cell-type label metadata. Register it under id 'marmoset-cortical-atlas'. Required for the registry entry: id, name, description, source_url, license, formats (list), tags, access_snippet (Python that loads at /data/marmoset-cortical-atlas/...). Save QC notes + an integrity check (e.g. shape of the counts matrix, first 10 cell-type labels) to /work.

## Summary

Everything is live. Here's the full report:

---

## Summary
I registered `marmoset-cortical-atlas` — a 75,861-cell snRNA-seq atlas of marmoset (*Callithrix jacchus*) middle temporal gyrus from Jorstad, Krienen et al. 2023 *Science*. It has a clean 3-level Allen Institute taxonomy (103 clusters → 24 subclasses → 18 CL-ontology cell types) with the same subclass naming scheme as Tasic 2018 (L2/3 IT, Pvalb, Sst, Vip, Lamp5…), making direct comparisons straightforward. The dataset loads from `/data/marmoset-cortical-atlas/marmoset_MTG_Jorstad2023.h5ad`.

## What I did
- **Evaluated 3 candidates** via CellxGene API: Bakken 2021 M1 (~21k cells, 3 files), Ma/Sestan 2023 dlPFC (149k cells, less structured), and **Jorstad+Krienen 2023 MTG (75k cells, single clean h5ad)** — chose the last
- **Confirmed paper + license:** DOI `10.1126/science.ade9516`; license CC BY 4.0 (CellxGene curation standard)
- **Downloaded** `marmoset_MTG_Jorstad2023.h5ad` (486 MB; SHA256: `8646351...`)
- **Sanity-checked** in sandbox: 75,861 × 12,897, float32 counts, gene symbols, 3 donors, 24 subclasses verified, UMAP present
- **Saved** `/work/marmoset_cortical_atlas_qc.json` and `/work/marmoset_cortical_atlas_integrity_check.md`
- **Registered** under id `marmoset-cortical-atlas`; dataset is live for all future jobs

## Caveats / next steps
- **Gene IDs are human symbols** (marmoset→human orthologs), not marmoset Ensembl IDs — harmless for most analyses but be aware for cross-species alignment
- **No raw counts** in this CellxGene release — X is log1p-normalized float32; for differential expression requiring raw counts, fetch from NeMO (`https://assets.nemoarchive.org/dat-net1412`)
- **Single region (MTG only)** — for multi-region marmoset cortex work, the Ma/Sestan 2023 dlPFC (149k cells) would complement this
- The Bakken 2021 M1 data (collection `367d95c0`) remains unregistered but could be added if motor cortex comparisons are needed

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
- [`code/_cell_0015.py`](./code/_cell_0015.py)
- [`code/_cell_0016.py`](./code/_cell_0016.py)
- [`code/_cell_0017.py`](./code/_cell_0017.py)
- [`marmoset_cortical_atlas_integrity_check.md`](./marmoset_cortical_atlas_integrity_check.md)
- [`summary.md`](./summary.md)
- [`tables/.kernel.json`](./tables/.kernel.json)
- [`tables/marmoset_cortical_atlas_qc.json`](./tables/marmoset_cortical_atlas_qc.json)
