
content = """# Bugeon et al. 2022 — Methods Extract
**Paper:** A transcriptomic axis predicts state modulation of cortical interneurons  
**Journal:** Nature 607, 330–338 (2022)  
**DOI:** 10.1038/s41586-022-04915-7  
**PMID:** 35794483 | **PMCID:** PMC9279161  
**License:** CC BY 4.0  
**Source fetched:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9279161/ (OAI-PMH full text)  
**Fetch date:** 2026-06-06

---

> **Note on section attribution:** Nature papers interleave methods and results in the narrative text.
> The 50 KB per-fetch cap prevents reaching the standalone formal "Methods" section at the end of the
> article. All quotes below are verbatim from the **"Identifying recorded inhibitory subtypes"** 
> section of the main text (PMC OAI-PMH XML, retrieved 2026-06-06), which describes the experimental
> approach in the same language as a Methods section. The abstract (also fetched) corroborates the
> numbers. The formal Methods section subsection on "Animals" would specify additional detail about
> the transgenic line and surgery; the four-mouse count is stated in both the main text and figure
> legends.

---

## (a) How many mice were used

**Direct quote (main text, "Identifying recorded inhibitory subtypes" section):**

> "We applied this method to **17 recording sessions from 4 mice**, and obtained 89 ± 31 (mean ± s.d.)
> molecularly identified inhibitory cells together with 393 ± 173 pyramidal neurons per session,
> making a total of 1,090 unique molecularly identified inhibitory cells (some of which were recorded
> in multiple sessions; Supplementary Data 1)."

**Corroborating quote (Fig. 1i legend and Fig. 3b legend):**

> "(n = 4 mice)"  
> "(n = 4 mice, 17 sessions)"

**Answer: 4 mice** (with 17 imaging sessions total).

---

## (b) Three-level cell-type hierarchy

**Quote from the abstract:**

> "We classified inhibitory neurons imaged in layers 1–3 into **a three-level hierarchy of
> 5 subclasses, 11 types and 35 subtypes** using previously defined transcriptomic clusters."

**Quote from the main text defining the three levels:**

> "We classified these inhibitory cells using a three-level hierarchy (Fig. 1f). The **lowest
> hierarchical level ('subtype')** comprised the fine transcriptomic clusters defined previously,
> and the **top level ('subclass')** was the *Pvalb*, *Sst*, *Lamp5*, *Vip* and *Sncg* groupings
> that were defined in the same previous report. An **intermediate level ('type')** was suggested
> by uniform manifold approximation and projection (UMAP) analysis of scRNA-seq data (Extended Data
> Fig. 3), which revealed collections of clusters that we could putatively associate to morphological
> cell types (see Methods for full explanation)."

**Summary of the hierarchy (broadest → finest):**

| Level | Name | Count | Marker genes / basis |
|-------|------|-------|----------------------|
| Top (broadest) | **subclass** | 5 | *Pvalb*, *Sst*, *Lamp5*, *Vip*, *Sncg* |
| Intermediate | **type** | 11 | UMAP-defined groups of clusters, putatively morphological |
| Bottom (finest) | **subtype** | 35 | Fine transcriptomic clusters from Tasic et al. 2018 (ref. 3) |

---

## (c) Named example of an intermediate-level 'type'

**Quote (main text, directly naming all 11 types):**

> "We named these intermediate-level types *Pvalb*-*Tac1* (putative *Pvalb* basket cells);
> *Pvalb*-*Vipr2* (putative chandelier cells); ***Sst*-*Reln*** **(putative Martinotti cells)**;
> *Sst*-*Tac1* (putative non-Martinotti *Sst* cells); *Lamp5*-*Npy* (putative neurogliaform cells);
> *Lamp5*-*Tmem182* (putative canopy cells); *Lamp5*-*Chrna7* (putative layer-1 α7 cells);
> *Vip*-*Reln* (putative layer-1 *Vip* cells); *Vip*-*Cp* (other Vip cells);
> *Sncg*-*Pdzrn3* (putative large *Cck* cells); and *Sncg*-*Vip* (putative small *Cck*/*Vip* cells)."

**Named example:** **Sst-Reln (putative Martinotti cells)**

---

## All 11 named intermediate-level 'types' (from the same quoted sentence)

| Type name | Putative morphological identity |
|-----------|--------------------------------|
| Pvalb-Tac1 | Pvalb basket cells |
| Pvalb-Vipr2 | Chandelier cells |
| **Sst-Reln** | **Martinotti cells** |
| Sst-Tac1 | Non-Martinotti Sst cells |
| Lamp5-Npy | Neurogliaform cells |
| Lamp5-Tmem182 | Canopy cells |
| Lamp5-Chrna7 | Layer-1 α7 cells |
| Vip-Reln | Layer-1 Vip cells |
| Vip-Cp | Other Vip cells |
| Sncg-Pdzrn3 | Large Cck cells |
| Sncg-Vip | Small Cck/Vip cells |

---

## Retrieval log

| Step | URL | Result |
|------|-----|--------|
| 1 | https://www.nature.com/articles/s41586-022-04915-7 | 50 KB cap; abstract + JSON-LD only |
| 2 | NCBI E-utilities idconv | Confirmed PMCID = PMC9279161 |
| 3 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=PMC9279161&rettype=full&retmode=xml | **Full main text retrieved**; Methods section beyond 50 KB cap |
| 4 | PMC OAI-PMH endpoint | Confirmed same full text, all quotes verified |
| 5 | Semantic Scholar API | Confirmed abstract quotes |

All three answers are **verbatim** from the fetched PMC full text of the CC BY open-access paper.
"""

with open("/work/bugeon_methods_extract.md", "w") as f:
    f.write(content)

print("Written:", len(content), "characters")
print("File saved to /work/bugeon_methods_extract.md")
