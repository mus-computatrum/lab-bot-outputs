# Run `d7948d75a854` — research

**When (UTC):** 2026-06-08 17:45:22
**Datasets:** _none_

## Request

> Read the papers from Green and Hrvatin and identify which datasets are publicly available.

## Summary

I verified both papers' Data Availability statements against the journals and GEO records.

## Summary
The two relevant papers from this group — **Green et al. 2023 Nature** (the Sst44 self-exciting/error-correction PPC paper, the senior author Hrvatin) and the platform paper **Hrvatin et al. 2019 eLife** — each have one publicly deposited dataset in GEO. The 2023 paper's only public data is its single-nucleus ATAC-seq (**GSE232200**); its calcium-imaging, photostimulation and electrophysiology data and analysis code are "available on request" and are **not** in a public repository. The 2019 PESCA paper is fully public, including processed tables (**GSE136802**).

## What I did
- Fetched the journal pages and GEO records (no web tool wired this job, so I used the sandbox's internet) and extracted the Data Availability sections and accession metadata.
- Confirmed: **GSE232200** = 10x snATAC-seq of Gad2-Cre;Sun1-GFP cortical inhibitory neurons, 2 bioreps (GSM7317753/4; `.snap.gz` + `singlecell.csv.gz`), public since 11 May 2023.
- Confirmed: **GSE136802** (BioProject PRJNA563701, SRA SRP220190) = Sst/Vip/Pv INTACT ATAC-seq + scRNA-seq with processed peak/count CSVs, fully public.
- Saved a catalog to `/work/green_hrvatin_datasets.csv` and recorded a lab note.

## Caveats / next steps
- "Papers from Green and Hrvatin" most naturally maps to these two; if you meant additional Hrvatin papers (e.g., Hrvatin 2018 Nat Neurosci torpor/visual-cortex work), I can pull those accessions too.
- The 2023 behavioral/imaging data and code are gated behind "on request" — not downloadable; I did not contact the authors. Next step would be to download GSE232200/GSE136802 supplementary files into `/data` for analysis.

## Files

- [`code/_cell_0001.py`](./code/_cell_0001.py)
- [`code/_cell_0002.py`](./code/_cell_0002.py)
- [`code/_cell_0003.py`](./code/_cell_0003.py)
- [`code/_cell_0004.py`](./code/_cell_0004.py)
- [`code/_cell_0005.py`](./code/_cell_0005.py)
- [`code/_cell_0006.py`](./code/_cell_0006.py)
- [`notebook.ipynb`](./notebook.ipynb)
- [`tables/.kernel.json`](./tables/.kernel.json)
- [`tables/fontlist-v390.json`](./tables/fontlist-v390.json)
- [`tables/green_hrvatin_datasets.csv`](./tables/green_hrvatin_datasets.csv)
