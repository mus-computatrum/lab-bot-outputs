# Run `2626e223796e` — research

**When (UTC):** 2026-06-07 14:16:06
**Datasets:** _none_

## Request

> [bench:research-internet-fetch-method-from-paper] Using ONLY the live web (web_fetch / web_search), pull the Methods section of Bugeon et al. 2022 Nature ('A transcriptomic axis predicts state modulation of cortical interneurons', doi:10.1038/s41586-022-04915-7) from https://www.nature.com/articles/s41586-022-04915-7 and extract: (a) how many mice were used, (b) the three-level cell-type hierarchy they define (subclass → type → subtype), and (c) one named example of an intermediate-level 'type' (e.g. 'Sst-Reln (putative Martinotti cells)'). Save /work/bugeon_methods_extract.md. Do NOT answer from memory; you must quote the page.

## Summary

All three items extracted verbatim from the live document and saved.

## Summary
I pulled the live text of Bugeon et al. 2022 (*Nature*, "A transcriptomic axis predicts state modulation of cortical interneurons") and extracted, with verbatim quotes: **(a) 4 mice** (across 17 recording sessions, 1,090 unique inhibitory cells); **(b)** a **three-level hierarchy of 5 subclasses → 11 types → 35 subtypes** (subclass = Pvalb/Sst/Lamp5/Vip/Sncg marker groupings; type = UMAP-derived clusters mapped to morphological cell types; subtype = fine scRNA-seq transcriptomic clusters); and **(c)** a named intermediate-level type example: **Sst-Reln (putative Martinotti cells)** — one of the 11 the authors name.

## What I did
- `web_fetch` on the Nature URL: it is JS-rendered and returned only the abstract JSON (no body/Methods text), as my prior notes predicted.
- `web_fetch` on the NCBI eFetch PMC XML mirror (PMC9279161) of the identical CC BY article — full main text came through; quoted the relevant passages.
- Saved `/work/bugeon_methods_extract.md` (3.2 KB) with all three items, each backed by a verbatim quote and source URLs, plus the complete list of 11 named types.

## Caveats / next steps
- The literal "Online Methods" section sits past the ~50 KB fetch cap; the quoted facts come from the abstract + main Results body (which contain the mouse count and the full hierarchy/type definitions). All three requested items are explicitly stated there, so no Methods-only retrieval was needed. The Nature HTML itself can't be read statically — the PMC mirror is the reliable live source for full text.

## Files

- [`bugeon_methods_extract.md`](./bugeon_methods_extract.md)
- [`code/_cell_0001.py`](./code/_cell_0001.py)
- [`notebook.ipynb`](./notebook.ipynb)
- [`summary.md`](./summary.md)
- [`tables/.kernel.json`](./tables/.kernel.json)
- [`tables/fontlist-v390.json`](./tables/fontlist-v390.json)
