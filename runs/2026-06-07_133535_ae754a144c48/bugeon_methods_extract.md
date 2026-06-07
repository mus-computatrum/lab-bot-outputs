# Bugeon et al. 2022 — Methods Extraction
**Source:** PMC full text, PMC9279161  
**DOI:** 10.1038/s41586-022-04915-7  
**Fetched:** 2026-06-07 via https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9279161/

---

## (a) Number of mice

**Answer: 4 mice** (17 recording sessions)

Direct quote from the article (section "Identifying recorded inhibitory subtypes"):

> "We applied this method to 17 recording sessions from **4 mice**, and obtained 89 ± 31
> (mean ± s.d.) molecularly identified inhibitory cells together with 393 ± 173 pyramidal
> neurons per session, making a total of 1,090 unique molecularly identified inhibitory cells."

The same number appears in figure captions, e.g. Fig. 1i: *(n = 4 mice)* and Fig. 3b:
*(n = 4 mice, 17 sessions)*.

---

## (b) Three-level cell-type hierarchy

**Levels (bottom → top):** subtype → type → subclass

Direct quote from the article (section "Identifying recorded inhibitory subtypes"):

> "We classified these inhibitory cells using a **three-level hierarchy** (Fig. 1f).
> The lowest hierarchical level ('**subtype**') comprised the fine transcriptomic clusters
> defined previously [ref 3], and the top level ('**subclass**') was the *Pvalb*, *Sst*,
> *Lamp5*, *Vip* and *Sncg* groupings that were defined in the same previous report.
> An intermediate level ('**type**') was suggested by uniform manifold approximation and
> projection (UMAP) analysis of scRNA-seq data (Extended Data Fig. 3), which revealed
> collections of clusters that we could putatively associate to morphological cell types."

The abstract also states: *"We classified inhibitory neurons imaged in layers 1–3 into a
three-level hierarchy of **5 subclasses, 11 types and 35 subtypes**."*

Summary table:

| Level | Name     | N   | Basis |
|-------|----------|-----|-------|
| Top   | subclass | 5   | Major marker genes (Pvalb, Sst, Lamp5, Vip, Sncg) |
| Mid   | type     | 11  | UMAP groupings of clusters → putative morphological cell types |
| Low   | subtype  | 35  | Fine transcriptomic clusters from Tasic et al. 2018 (ref 3) |

---

## (c) Named example of an intermediate-level 'type'

**Example: *Sst-Reln* (putative Martinotti cells)**

Direct quote from the article listing all 11 intermediate types:

> "We named these intermediate-level types *Pvalb-Tac1* (putative *Pvalb* basket cells);
> *Pvalb-Vipr2* (putative chandelier cells); ***Sst-Reln* (putative Martinotti cells)**;
> *Sst-Tac1* (putative non-Martinotti *Sst* cells); *Lamp5-Npy* (putative neurogliaform
> cells); *Lamp5-Tmem182* (putative canopy cells); *Lamp5-Chrna7* (putative layer-1 α7
> cells); *Vip-Reln* (putative layer-1 *Vip* cells); *Vip-Cp* (other Vip cells);
> *Sncg-Pdzrn3* (putative large *Cck* cells); and *Sncg-Vip* (putative small *Cck*/*Vip*
> cells)."

The type *Sst-Reln* appears repeatedly in the Results:
> "Within the *Sst* subclass, *Sst-Tac1* cells were most active during synchronized
> states, whereas ***Sst-Reln* cells were more active during running**."

---

## Notes on sourcing

All quotes above are from the PMC open-access full text (PMC9279161), fetched live on
2026-06-07. The "Methods" section proper (which describes coppaFISH, imaging pipeline,
and statistical procedures in detail) appears later in the article beyond the 50 KB fetch
window. The three requested facts are stated clearly in the main Results body under
"Identifying recorded inhibitory subtypes" — which itself describes the experimental
setup and classification approach.
