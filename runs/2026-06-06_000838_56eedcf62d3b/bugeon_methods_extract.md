# Bugeon et al. 2022 — Methods Extract
**Source:** Bugeon S. et al. "A transcriptomic axis predicts state modulation of cortical interneurons"  
**Journal:** Nature 607(7918):330–338 (2022)  
**DOI:** https://doi.org/10.1038/s41586-022-04915-7  
**Retrieved from:** PMC full-text XML, PMC9279161  
**Fetch date:** 2026-06-05  
**Fetch URL:** https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=PMC9279161&rettype=full&retmode=xml

---

> **Note on source section:** The three items below are quoted from the
> section titled "Identifying recorded inhibitory subtypes" in the main body
> of the article (equivalent to the Methods/Results integration typical of
> Nature papers). The formal appendix "Methods" section was beyond the 50 KB
> fetch limit, but the key methodological facts appear verbatim in the main
> text. The Nature.com page itself (50 KB cap) returned only JSON-LD
> metadata; the PMC XML API (PMC9279161) provided the full article text.

---

## (a) Number of mice used

Direct quote from the section "Identifying recorded inhibitory subtypes":

> "We applied this method to **17 recording sessions from 4 mice**, and
> obtained 89 ± 31 (mean ± s.d.) molecularly identified inhibitory cells
> together with 393 ± 173 pyramidal neurons per session, making a total of
> 1,090 unique molecularly identified inhibitory cells (some of which were
> recorded in multiple sessions; Supplementary Data 1)."

**Answer: 4 mice** (across 17 recording sessions).

---

## (b) Three-level cell-type hierarchy

Direct quote from the section "Identifying recorded inhibitory subtypes":

> "We classified these inhibitory cells using a **three-level hierarchy**
> (Fig. 1f). The lowest hierarchical level ('**subtype**') comprised the fine
> transcriptomic clusters defined previously [ref. 3], and the top level
> ('**subclass**') was the *Pvalb*, *Sst*, *Lamp5*, *Vip* and *Sncg*
> groupings that were defined in the same previous report. An intermediate
> level ('**type**') was suggested by uniform manifold approximation and
> projection (UMAP) analysis of scRNA-seq data (Extended Data Fig. 3), which
> revealed collections of clusters that we could putatively associate to
> morphological cell types."

The abstract also states:

> "We classified inhibitory neurons imaged in layers 1–3 into a three-level
> hierarchy of **5 subclasses, 11 types and 35 subtypes** using previously
> defined transcriptomic clusters [ref. 3]."

**Summary of levels (top → bottom):**

| Level | Name | Count |
|-------|------|-------|
| Top | **Subclass** | 5 (Pvalb, Sst, Lamp5, Vip, Sncg) |
| Intermediate | **Type** | 11 |
| Bottom | **Subtype** | 35 |

---

## (c) Named example of an intermediate-level 'type'

Direct quote from the section "Identifying recorded inhibitory subtypes"
(listing all 11 named types):

> "We named these intermediate-level types *Pvalb-Tac1* (putative *Pvalb*
> basket cells); *Pvalb-Vipr2* (putative chandelier cells);
> ***Sst-Reln* (putative Martinotti cells)**; *Sst-Tac1* (putative
> non-Martinotti *Sst* cells); *Lamp5-Npy* (putative neurogliaform cells);
> *Lamp5-Tmem182* (putative canopy cells); *Lamp5-Chrna7* (putative layer-1
> α7 cells); *Vip-Reln* (putative layer-1 *Vip* cells); *Vip-Cp* (other Vip
> cells); *Sncg-Pdzrn3* (putative large *Cck* cells); and *Sncg-Vip*
> (putative small *Cck*/*Vip* cells)."

**Example:** `Sst-Reln` = putative Martinotti cells  
(This is the same example cited in the user's prompt, confirming it appears
verbatim in the paper.)

---

## Additional context (from the same section)

The hierarchy is validated in two ways:
1. Subtype cortical-depth estimates from coppaFISH match independent Patch-seq data (Pearson r = 0.91, P = 1×10⁻¹³).
2. Grouping cells by expected transgenic line labels (Sst, Pvalb, Vip) reproduces results from prior calcium-imaging studies.

Gene-panel size: 72 genes detected by coppaFISH (7 rounds × 7-colour
imaging). Detection rate: 144 ± 57 transcripts per cell (mean ± s.d.).
