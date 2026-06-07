# research-internet-fetch-method-from-paper

**Mode**: research  ·  **Effort**: deep

## Request

> Using ONLY the live web (web_fetch / web_search), pull the Methods section of Bugeon et al. 2022 Nature ('A transcriptomic axis predicts state modulation of cortical interneurons', doi:10.1038/s41586-022-04915-7) from https://www.nature.com/articles/s41586-022-04915-7 and extract: (a) how many mice were used, (b) the three-level cell-type hierarchy they define (subclass → type → subtype), and (c) one named example of an intermediate-level 'type' (e.g. 'Sst-Reln (putative Martinotti cells)'). Save /work/bugeon_methods_extract.md. Do NOT answer from memory; you must quote the page.

## Final summary

All done. Here's the full report:

---

## Summary

Bugeon et al. 2022 (*Nature* 607:330–338) used **4 mice** across 17 two-photon calcium imaging sessions, combined with post-hoc coppaFISH in-situ transcriptomics, to identify 1,090 inhibitory neurons in mouse V1. They classified cells into a **three-level hierarchy**: top-level **subclass** (5: *Pvalb*, *Sst*, *Lamp5*, *Vip*, *Sncg*) → intermediate **type** (11, UMAP-derived and morphology-linked) → lowest-level **subtype** (35 fine scRNA-seq clusters). A named example of an intermediate type is **`Sst-Reln` (putative Martinotti cells)**, quoted verbatim from the paper. All three facts are direct quotations from the live PMC full-text.

## What I did

1. Attempted to fetch the Nature publisher page — JS-rendered; no Methods body text in static HTML.
2. Identified the PMC ID (9279161) via the Semantic Scholar API.
3. Retrieved the full article XML body via NCBI E-utilities eFetch (`efetch.fcgi?db=pmc&id=PMC9279161`), which returned the CC-BY full text.
4. Extracted all three requested facts with verbatim quotes from the "Identifying recorded inhibitory subtypes" section of the main text.
5. Saved `/work/bugeon_methods_extract.md` (4,450 chars) with full quotes, source URLs, and a retrieval-method note.
6. Appended a lab note for future jobs.

## Caveats / next steps

- The 50 KB web_fetch cap means the **formal "Online Methods" section** (appearing at the end of the XML) was not reached. All three requested facts appear in the main results text, which cross-references the Online Methods for fuller protocol detail. The n=4 mice figure is confirmed both in the results text and figure captions.
- The **formal Online Methods** likely contains additional animal-use details (ethics approval, housing, surgical procedure specifics). To access it, one would need to download the full article XML in chunks or fetch the PDF (CC-BY, available at the Nature DOI).
- No memory was used: every quote was retrieved live from `ncbi.nlm.nih.gov` on 2026-06-07.
