# Run `75159bf7c7b5` — research

**When (UTC):** 2026-06-07 13:55:32
**Datasets:** _none_

## Request

> [bench:research-internet-fetch-method-from-paper] Using ONLY the live web (web_fetch / web_search), pull the Methods section of Bugeon et al. 2022 Nature ('A transcriptomic axis predicts state modulation of cortical interneurons', doi:10.1038/s41586-022-04915-7) from https://www.nature.com/articles/s41586-022-04915-7 and extract: (a) how many mice were used, (b) the three-level cell-type hierarchy they define (subclass → type → subtype), and (c) one named example of an intermediate-level 'type' (e.g. 'Sst-Reln (putative Martinotti cells)'). Save /work/bugeon_methods_extract.md. Do NOT answer from memory; you must quote the page.

## Summary

Done. All three items extracted from the live web and quoted verbatim; saved to `/work/bugeon_methods_extract.md`.

## Summary
From Bugeon et al. 2022 (*Nature*, "A transcriptomic axis predicts state modulation of cortical interneurons"): the study used **4 mice** (17 recording sessions, 1,090 unique molecularly identified inhibitory cells). They define a **three-level hierarchy: subclass (5: Pvalb, Sst, Lamp5, Vip, Sncg) → type (11, UMAP-derived, putatively mapped to morphological cell types) → subtype (35, fine scRNA-seq transcriptomic clusters)**. A named intermediate-level *type* example is **Sst-Reln (putative Martinotti cells)**.

## What I did
- `web_fetch` on the Nature URL: it is JS-rendered and returns only the JSON-LD abstract (no Methods/Results body). The abstract did confirm "5 subclasses, 11 types and 35 subtypes."
- For the verbatim mouse count, hierarchy definitions, and the full list of 11 named types, I `web_fetch`-ed the live NCBI PMC full text of the same article (eutils efetch, PMC9279161) and quoted it directly.
- Saved `/work/bugeon_methods_extract.md` (2.9 KB) with the quotes and source provenance.

## Caveats / next steps
- The static nature.com HTML does not expose the Methods body, so I relied on the open-access PMC mirror of the identical article (live web, CC BY) for the quotes — content is the published version. The PMC dump hit the ~50 KB fetch cap before the formal "Online Methods," but the main-text Results contain all three requested facts verbatim. For methods-protocol detail (coppaFISH rounds, pciSeq params) one would page deeper into the PMC XML.

## Files

- [`bugeon_methods_extract.md`](./bugeon_methods_extract.md)
- [`code/_cell_0001.py`](./code/_cell_0001.py)
- [`notebook.ipynb`](./notebook.ipynb)
- [`summary.md`](./summary.md)
- [`tables/.kernel.json`](./tables/.kernel.json)
- [`tables/fontlist-v390.json`](./tables/fontlist-v390.json)
