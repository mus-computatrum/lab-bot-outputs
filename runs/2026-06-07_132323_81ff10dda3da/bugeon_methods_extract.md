# Bugeon et al. 2022 — Methods Extract
**Source fetched live from:** https://pmc.ncbi.nlm.nih.gov/articles/PMC9279161/
  (via NCBI E-utilities XML API, PMC9279161 / PMID 35794483 / DOI 10.1038/s41586-022-04915-7)

---

## (a) Number of mice used

**4 mice, 17 recording sessions.**

Direct quote from the article (Results / "Identifying recorded inhibitory subtypes" section):

> "We applied this method to **17 recording sessions from 4 mice**, and obtained 89 ± 31 (mean ± s.d.) molecularly identified inhibitory cells together with 393 ± 173 pyramidal neurons per session, making a total of 1,090 unique molecularly identified inhibitory cells."

Confirmed in figure legends:
> "n = 4 mice, 17 sessions"

---

## (b) Three-level cell-type hierarchy (subclass → type → subtype)

From the abstract:

> "We classified inhibitory neurons imaged in layers 1–3 into a **three-level hierarchy of 5 subclasses, 11 types and 35 subtypes** using previously defined transcriptomic clusters."

The hierarchy, as named explicitly in the Methods/Results section:

| Hierarchical level | Term used | Count | Definition |
|----|----|----|---|
| Top | **subclass** | 5 | Pvalb, Sst, Lamp5, Vip, Sncg (marker-gene-based groupings from prior scRNA-seq) |
| Intermediate | **type** | 11 | Suggested by UMAP of scRNA-seq data; putatively linked to morphological cell types |
| Bottom | **subtype** | 35 | Fine transcriptomic clusters defined by Tasic et al. 2018 (ref 3 in paper) |

Direct quote defining each level:

> "The lowest hierarchical level ('**subtype**') comprised the fine transcriptomic clusters defined previously, and the top level ('**subclass**') was the Pvalb, Sst, Lamp5, Vip and Sncg groupings that were defined in the same previous report. An intermediate level ('**type**') was suggested by uniform manifold approximation and projection (UMAP) analysis of scRNA-seq data, which revealed collections of clusters that we could putatively associate to morphological cell types."

---

## (c) Named example of an intermediate-level 'type'

**Sst-Reln (putative Martinotti cells)**

Direct quote listing all 11 named types:

> "We named these intermediate-level types **Pvalb-Tac1** (putative Pvalb basket cells); **Pvalb-Vipr2** (putative chandelier cells); **Sst-Reln** (putative Martinotti cells); **Sst-Tac1** (putative non-Martinotti Sst cells); **Lamp5-Npy** (putative neurogliaform cells); **Lamp5-Tmem182** (putative canopy cells); **Lamp5-Chrna7** (putative layer-1 α7 cells); **Vip-Reln** (putative layer-1 Vip cells); **Vip-Cp** (other Vip cells); **Sncg-Pdzrn3** (putative large Cck cells); and **Sncg-Vip** (putative small Cck/Vip cells)."

So the full list of 11 intermediate types is:
1. Pvalb-Tac1 (putative Pvalb basket cells)
2. Pvalb-Vipr2 (putative chandelier cells)
3. **Sst-Reln (putative Martinotti cells)**  ← example from user query
4. Sst-Tac1 (putative non-Martinotti Sst cells)
5. Lamp5-Npy (putative neurogliaform cells)
6. Lamp5-Tmem182 (putative canopy cells)
7. Lamp5-Chrna7 (putative layer-1 α7 cells)
8. Vip-Reln (putative layer-1 Vip cells)
9. Vip-Cp (other Vip cells)
10. Sncg-Pdzrn3 (putative large Cck cells)
11. Sncg-Vip (putative small Cck/Vip cells)

---

## Source / retrieval note

All quotes above are verbatim from the PMC full-text XML (PMC9279161), fetched live on 2026-06-07
via `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=PMC9279161&rettype=xml`.
The Nature landing page (https://www.nature.com/articles/s41586-022-04915-7) was also accessed
but was JavaScript-rendered and truncated before the Methods section.
The PMC text (CC BY 4.0) contains the full article text including Methods, Results, and figure legends.
