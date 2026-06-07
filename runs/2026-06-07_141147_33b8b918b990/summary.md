# research-internet-fetch-method-from-paper

**Mode**: research  ·  **Effort**: deep

## Request

> Using ONLY the live web (web_fetch / web_search), pull the Methods section of Bugeon et al. 2022 Nature ('A transcriptomic axis predicts state modulation of cortical interneurons', doi:10.1038/s41586-022-04915-7) from https://www.nature.com/articles/s41586-022-04915-7 and extract: (a) how many mice were used, (b) the three-level cell-type hierarchy they define (subclass → type → subtype), and (c) one named example of an intermediate-level 'type' (e.g. 'Sst-Reln (putative Martinotti cells)'). Save /work/bugeon_methods_extract.md. Do NOT answer from memory; you must quote the page.

## Final summary

Saved. All three items were extracted verbatim from the live document.

## Summary
I pulled the live full text of Bugeon et al. 2022 *Nature* and extracted the three requested items, all quoted verbatim. (a) The study used **4 mice** (17 recording sessions, 1,090 unique molecularly identified inhibitory cells). (b) They define a **three-level hierarchy**: top **subclass** (5: Pvalb, Sst, Lamp5, Vip, Sncg) → intermediate **type** (11, UMAP-derived) → lowest **subtype** (35 recorded, fine scRNA-seq clusters). (c) A named intermediate "type" example: **Sst‑Reln (putative Martinotti cells)**.

## What I did
- Fetched the requested `nature.com` URL live — it returns a 303 auth-redirect and the body is JS-rendered, so no static Methods text is served.
- Pulled the identical article's full text live from the open-access PMC mirror via NCBI eFetch PMC XML (CC BY 4.0) and quoted it directly.
- Saved `/work/bugeon_methods_extract.md` (3.8 KB) with verbatim quotes for (a), (b), (c) plus provenance and extra Methods context.

## Caveats / next steps
- The verbatim text comes from the PMC open-access mirror, not the paywalled/JS-rendered nature.com HTML, because the latter serves no static Methods text. The two are the publisher-deposited same version; the requested figure-1 detail ("Hierarchical classification ... 5 subclasses, 11 types and 35 subtypes") and counts appear in the main Results, which is what I quoted. The formal "Online Methods" subsection lies beyond eFetch's returned window but every requested fact is covered by the quoted Results/abstract/figure legends.

Sources:
- [Bugeon et al. 2022, PMC9279161 (open-access mirror)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9279161/)
- [Nature article page (auth-walled/JS-rendered)](https://www.nature.com/articles/s41586-022-04915-7)
