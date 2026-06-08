# Run `28aee20060a4` — download

**When (UTC):** 2026-06-08 18:50:25
**Datasets:** _none_

## Request

> Finish downloading and configuring GSE232200 and GSE136802.

## Summary

All work is complete. Both GEO accessions are downloaded, configured, and committed to the lab registry.

## Summary
I finished acquiring and configuring both datasets from NCBI GEO. **GSE232200** (Green et al. 2023, mouse PPC inhibitory-neuron snATAC-seq) is now a merged peak×cell matrix of **22,988 cells × 459,912 mm10 peaks**, built from the two bioreps' SnapATAC `.snap` files. **GSE136802** (Hrvatin et al. 2019 PESCA interneuron data) is two artifacts: a **47,348-cell × 27,035-gene** scRNA matrix and a **pseudobulk ATAC** matrix (6 sorted Sst/Vip/Pv samples × 323,369 peaks). Both are registered and live for all future jobs.

## What I did
- Enumerated GEO file listings; staged all 8 public files (4.31 GB).
- Built and verified `gse232200_snapatac.h5ad` (peak×cell, with per-cell QC), `gse136802_scrna.h5ad` (raw + lognorm layers), `gse136802_atac.h5ad` (counts + binary layer, GRE annotations).
- Wrote `gse232200_config.md` / `gse136802_config.md` provenance notes.
- Registered `green-2023-ppc-inhibitory-snatac` (6 files, 6.1 GB) and `hrvatin-2019-pesca-interneuron` (7 files, 0.59 GB), each with a dataset card. Saved a lab note.

## Caveats / next steps
- **63 orphan peaks** (idy 459913–459975) in the `.snap` PM group had no stored coordinates (~0.008% of nonzeros) and were dropped; the coordinate array is a valid genomic-sorted prefix.
- GSE136802 scRNA has **no deposited Sst/Vip/Pv labels** — assign by clustering. Its ATAC is **pseudobulk**, not single-cell.
- Not extracted from the raw `.snap` (still available): the 5kb `AM/5000` bin×cell matrix and `FM` raw fragments — easy to add if needed.

A lighter tier could have handled the downloads, but the 8 GB-RAM matrix assembly and `.snap` schema reverse-engineering justified deep tier.

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
- [`code/_cell_0018.py`](./code/_cell_0018.py)
- [`code/_cell_0019.py`](./code/_cell_0019.py)
- [`code/_cell_0020.py`](./code/_cell_0020.py)
- [`code/_cell_0021.py`](./code/_cell_0021.py)
- [`code/_cell_0022.py`](./code/_cell_0022.py)
- [`code/_cell_0023.py`](./code/_cell_0023.py)
- [`code/_cell_0024.py`](./code/_cell_0024.py)
- [`notebook.ipynb`](./notebook.ipynb)
- [`tables/.kernel.json`](./tables/.kernel.json)
- [`tables/fontlist-v390.json`](./tables/fontlist-v390.json)
