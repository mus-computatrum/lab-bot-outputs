# Run `7d2f9d2ff12c` — research

**When (UTC):** 2026-06-07 14:11:15
**Datasets:** _none_

## Request

> [bench:research-internet-general-bugeon-hierarchy] In Bugeon et al. 2022 (Nature, doi:10.1038/s41586-022-04915-7), what three-level cell-type hierarchy do the authors define? Save the answer to /work/bugeon_hierarchy.md with a verbatim quote that names the levels.

## Summary

Done. The answer was confirmed against the live open-access full text.

## Summary
Bugeon et al. 2022 classify cortical inhibitory neurons (in mouse V1, layers 1–3) into a **three-level hierarchy: 5 subclasses → 11 types → 35 subtypes**. The top level (subclass) is the Pvalb/Sst/Lamp5/Vip/Sncg grouping; the intermediate level (type) is UMAP-derived groups putatively mapped to morphological cell types; the lowest level (subtype) is the fine scRNA-seq transcriptomic clusters.

## What I did
- Fetched the open-access full text via NCBI eFetch PMC XML (PMC9279161) — the Nature page itself is JS-rendered.
- Extracted the verbatim sentences naming all three levels (Abstract + Results).
- Saved the answer with verbatim quotes and the full list of level names to `/work/bugeon_hierarchy.md`.

## Caveats / next steps
The 35 subtypes are the previously defined Tasic et al. 2018 (ref 3) clusters; 109 clusters existed total but only 35 superficial inhibitory ones were imaged. This is a lighter-tier factual lookup — a "fast" tier would have sufficed. Already in my lab notes, so no new note added.

## Files

- [`bugeon_hierarchy.md`](./bugeon_hierarchy.md)
- [`code/_cell_0001.py`](./code/_cell_0001.py)
- [`notebook.ipynb`](./notebook.ipynb)
- [`summary.md`](./summary.md)
- [`tables/.kernel.json`](./tables/.kernel.json)
- [`tables/fontlist-v390.json`](./tables/fontlist-v390.json)
