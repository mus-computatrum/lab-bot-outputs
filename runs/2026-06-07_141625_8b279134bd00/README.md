# Run `8b279134bd00` — research

**When (UTC):** 2026-06-07 14:16:25
**Datasets:** _none_

## Request

> [bench:research-internet-general-bugeon-hierarchy] In Bugeon et al. 2022 (Nature, doi:10.1038/s41586-022-04915-7), what three-level cell-type hierarchy do the authors define? Save the answer to /work/bugeon_hierarchy.md with a verbatim quote that names the levels.

## Summary

The file is saved and verified against the live open-access full text. This matches my prior cross-job notes (no new lab note needed).

## Summary
In Bugeon et al. 2022 (*Nature*), inhibitory neurons in mouse primary visual cortex (V1, layers 1–3) are organized into a **three-level cell-type hierarchy**: **5 subclasses → 11 types → 35 subtypes**. The top level (subclass) is the *Pvalb / Sst / Lamp5 / Vip / Sncg* grouping; the intermediate level (type) is a set of UMAP-derived clusters mapped to putative morphological cell types; and the lowest level (subtype) is the fine transcriptomic clusters defined in earlier scRNA-seq work.

## What I did
- Fetched the open-access full text from NCBI PMC (PMC9279161) to obtain verbatim text.
- Wrote `/work/bugeon_hierarchy.md` containing the hierarchy summary plus verbatim quotes from the Abstract and Results that explicitly name all three levels (subclass, type, subtype), and the verbatim list of the 11 intermediate-level types.

## Caveats / next steps
- Quotes are transcribed from the PMC XML rendering; em-dashes/Greek letters (α7 → "alpha7") were normalized for plain-text safety but wording is otherwise verbatim. This was a lighter-tier (single fetch + file write) task; the deep research tier was not really needed.

## Files

- [`bugeon_hierarchy.md`](./bugeon_hierarchy.md)
- [`code/_cell_0001.py`](./code/_cell_0001.py)
- [`notebook.ipynb`](./notebook.ipynb)
- [`summary.md`](./summary.md)
- [`tables/.kernel.json`](./tables/.kernel.json)
- [`tables/fontlist-v390.json`](./tables/fontlist-v390.json)
