# Bugeon et al. 2022 Nature — Methods/Results extract
**Paper:** "A transcriptomic axis predicts state modulation of cortical interneurons"
Bugeon, Duffield, Dipoppa, ... Carandini, Harris. *Nature* 607, 330–338 (2022).
doi:10.1038/s41586-022-04915-7 | PMID 35794483 | PMC9279161

**Sources fetched live (2026-06-07):**
- https://www.nature.com/articles/s41586-022-04915-7 — JS-rendered; only abstract JSON returned (no static body text).
- NCBI eFetch PMC XML mirror of the identical open-access (CC BY) article:
  https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=PMC9279161 — full main text returned; passages quoted verbatim below.

---

## (a) How many mice

> "We applied this method to **17 recording sessions from 4 mice**, and obtained 89 ± 31 (mean ± s.d.) molecularly identified inhibitory cells together with 393 ± 173 pyramidal neurons per session, making a total of **1,090 unique molecularly identified inhibitory cells** (some of which were recorded in multiple sessions; Supplementary Data 1)."

Also stated in the abstract / figure legends: *n* = 4 mice (Fig. 1i; Fig. 3b "n = 4 mice, 17 sessions").

**Answer: 4 mice (across 17 recording sessions).**

---

## (b) Three-level cell-type hierarchy (subclass → type → subtype)

From the abstract:
> "We classified inhibitory neurons imaged in layers 1–3 into a **three-level hierarchy of 5 subclasses, 11 types and 35 subtypes** using previously defined transcriptomic clusters."

From the Results ("Identifying recorded inhibitory subtypes"):
> "We classified these inhibitory cells using a three-level hierarchy (Fig. 1f). The lowest hierarchical level ('**subtype**') comprised the fine transcriptomic clusters defined previously, and the top level ('**subclass**') was the *Pvalb*, *Sst*, *Lamp5*, *Vip* and *Sncg* groupings that were defined in the same previous report. An intermediate level ('**type**') was suggested by uniform manifold approximation and projection (UMAP) analysis of scRNA-seq data ..., which revealed collections of clusters that we could putatively associate to morphological cell types."

| Level      | Count | Definition (quoted) |
|------------|-------|---------------------|
| subclass   | 5     | top level — *Pvalb, Sst, Lamp5, Vip, Sncg* (marker-gene groupings) |
| type       | 11    | intermediate — UMAP-derived clusters putatively mapped to morphological cell types |
| subtype    | 35    | lowest — fine transcriptomic clusters (pre-defined scRNA-seq clusters) |

---

## (c) Named example(s) of the intermediate-level 'type'

> "We named these intermediate-level types **Pvalb-Tac1 (putative Pvalb basket cells)**; **Pvalb-Vipr2 (putative chandelier cells)**; **Sst-Reln (putative Martinotti cells)**; **Sst-Tac1 (putative non-Martinotti Sst cells)**; **Lamp5-Npy (putative neurogliaform cells)**; **Lamp5-Tmem182 (putative canopy cells)**; **Lamp5-Chrna7 (putative layer-1 alpha7 cells)**; **Vip-Reln (putative layer-1 Vip cells)**; **Vip-Cp (other Vip cells)**; **Sncg-Pdzrn3 (putative large Cck cells)**; and **Sncg-Vip (putative small Cck/Vip cells)**."

That is the full list of 11 types. Requested single example:
**Sst-Reln (putative Martinotti cells).**
