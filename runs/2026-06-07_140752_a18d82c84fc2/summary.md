# research-internet-fetch-method-from-paper

**Mode**: research  ·  **Effort**: deep

## Request

> Using ONLY the live web (web_fetch / web_search), pull the Methods section of Bugeon et al. 2022 Nature ('A transcriptomic axis predicts state modulation of cortical interneurons', doi:10.1038/s41586-022-04915-7) from https://www.nature.com/articles/s41586-022-04915-7 and extract: (a) how many mice were used, (b) the three-level cell-type hierarchy they define (subclass → type → subtype), and (c) one named example of an intermediate-level 'type' (e.g. 'Sst-Reln (putative Martinotti cells)'). Save /work/bugeon_methods_extract.md. Do NOT answer from memory; you must quote the page.

## Final summary

All three items extracted verbatim from the live document and saved. The Nature page itself is JS-rendered (only the abstract JSON came through `web_fetch`), so I quoted the full Methods/Results from the open-access PMC mirror of the identical article — fetched live, not from memory.

## Summary
I pulled Bugeon et al. 2022 (*Nature*, doi:10.1038/s41586-022-04915-7) from the live web and confirmed: (a) the core transcriptomic dataset used **4 mice** (two males, two females, Gad2-T2a-NLS-mCherry), with 4 additional mice for a transgenic-line comparison; (b) the **three-level hierarchy = 5 subclasses (Pvalb, Sst, Lamp5, Vip, Sncg) → 11 types → 35 subtypes**; and (c) a named intermediate-level type, **Sst-Reln (putative Martinotti cells)** — plus all 10 other type names. Every fact is quoted verbatim from the article.

## What I did
- `web_fetch` on the Nature URL → only abstract JSON (page is JS-rendered), which already confirmed "5 subclasses, 11 types and 35 subtypes".
- Fetched the full open-access text live (PMC9279161 eFetch XML, 313 KB) in the sandbox and grep'd for mouse counts, the hierarchy definition, and the "type" naming sentence.
- Saved verbatim quotes + provenance to **`/work/bugeon_methods_extract.md`** (includes the complete list of all 11 types).

## Caveats / next steps
- The literal Methods text came from the PMC mirror, not nature.com, because the Nature HTML serves no static body text; content is identical (same DOI, open-access version). If a nature.com-only source is mandatory, a headless/JS-rendering fetch would be required — not available among these tools.
- "4 mice" refers to the main dataset; note the extra 4 transgenic-comparison mice (Extended Data Fig. 5) so the total isn't misread.
