# Run `746c882a7ade` — research

**When (UTC):** 2026-06-07 14:07:16
**Datasets:** _none_

## Request

> [bench:research-internet-general-bugeon-hierarchy] In Bugeon et al. 2022 (Nature, doi:10.1038/s41586-022-04915-7), what three-level cell-type hierarchy do the authors define? Save the answer to /work/bugeon_hierarchy.md with a verbatim quote that names the levels.

## Summary

Saved. The hierarchy is already in my cross-job notes, so no new lab note needed.

## Summary
Bugeon et al. 2022 (*Nature*, doi:10.1038/s41586-022-04915-7) classify mouse V1 inhibitory interneurons into a **three-level hierarchy**: **subclass** (5: Pvalb, Sst, Lamp5, Vip, Sncg) → **type** (11, UMAP-derived intermediate groups, e.g. Sst-Reln putative Martinotti cells) → **subtype** (35 recorded, the fine scRNA-seq transcriptomic clusters). The verbatim defining sentence is: *"We classified inhibitory neurons imaged in layers 1–3 into a three-level hierarchy of 5 subclasses, 11 types and 35 subtypes using previously defined transcriptomic clusters."*

## What I did
- Fetched the live PMC full text (PMC9279161 via NCBI eFetch) and located the hierarchy definitions in the Abstract, Results ("Identifying recorded inhibitory subtypes"), and Fig. 1f caption.
- Saved `/work/bugeon_hierarchy.md` with the plain-language answer plus three verbatim quotes naming the levels (subclass / type / subtype) and the source URL.

## Caveats / next steps
- The "35 subtypes" refers to the subtypes actually recorded in vivo (superficial layers); the underlying scRNA-seq reference defines 60 inhibitory subtypes / 109 total clusters — worth noting if subtype counts are compared across papers.
- This was a single-source fact-extraction task; a lighter (shallow) tier would have sufficed.

## Files

- [`bugeon_hierarchy.md`](./bugeon_hierarchy.md)
- [`code/_cell_0001.py`](./code/_cell_0001.py)
- [`notebook.ipynb`](./notebook.ipynb)
- [`summary.md`](./summary.md)
- [`tables/.kernel.json`](./tables/.kernel.json)
- [`tables/fontlist-v390.json`](./tables/fontlist-v390.json)
