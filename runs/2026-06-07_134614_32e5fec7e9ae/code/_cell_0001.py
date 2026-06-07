
content = """# Bugeon et al. 2022 — Methods-Section Extract
**Full citation:** Bugeon S, Duffield J, Dipoppa M, et al. "A transcriptomic axis predicts state modulation of cortical interneurons." *Nature* 607, 330–338 (2022). https://doi.org/10.1038/s41586-022-04915-7  
**PMC:** PMC9279161 | **PMID:** 35794483  
**Source fetched:** https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=PMC9279161&rettype=full&retmode=xml  (plus https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9279161/ for crosscheck)  
**Date retrieved:** 2026-06-07

---

## (a) How many mice were used

**Direct quote from the paper (main results text, "Identifying recorded inhibitory subtypes" section):**

> "We applied this method to **17 recording sessions from 4 mice**, and obtained 89 ± 31 (mean ± s.d.) molecularly identified inhibitory cells together with 393 ± 173 pyramidal neurons per session, making a total of **1,090 unique molecularly identified inhibitory cells** (some of which were recorded in multiple sessions; Supplementary Data 1)."

**Also confirmed in figure captions (e.g. Fig. 1i and Fig. 3b):**

> "(*n* = **4 mice**, 17 sessions)"

**Answer: 4 mice** (across 17 imaging sessions).

---

## (b) The three-level cell-type hierarchy

### Abstract quote:

> "We classified inhibitory neurons imaged in layers 1–3 into a **three-level hierarchy of 5 subclasses, 11 types and 35 subtypes** using previously defined transcriptomic clusters."

### Main text elaboration ("Identifying recorded inhibitory subtypes"):

> "We classified these inhibitory cells using a **three-level hierarchy** (Fig. 1f). The **lowest hierarchical level ('subtype')** comprised the fine transcriptomic clusters defined previously, and the **top level ('subclass')** was the *Pvalb*, *Sst*, *Lamp5*, *Vip* and *Sncg* groupings that were defined in the same previous report. An **intermediate level ('type')** was suggested by uniform manifold approximation and projection (UMAP) analysis of scRNA-seq data (Extended Data Fig. 3), which revealed collections of clusters that we could putatively associate to morphological cell types (see Methods for full explanation)."

### Summary of hierarchy:

| Level | Description | Count |
|-------|-------------|-------|
| **Subclass** (top) | Marker-gene-defined groupings: *Pvalb*, *Sst*, *Lamp5*, *Vip*, *Sncg* | 5 |
| **Type** (intermediate) | UMAP-derived morphology-linked clusters, named by gene pairs | 11 |
| **Subtype** (lowest) | Fine transcriptomic clusters from prior scRNA-seq (Tasic et al.) | 35 |

---

## (c) Named example of an intermediate-level 'type'

**Direct quote (main text, "Identifying recorded inhibitory subtypes"):**

> "We named these intermediate-level types *Pvalb*-*Tac1* (putative *Pvalb* basket cells); *Pvalb*-*Vipr2* (putative chandelier cells); ***Sst*-*Reln* (putative Martinotti cells)**; *Sst*-*Tac1* (putative non-Martinotti *Sst* cells); *Lamp5*-*Npy* (putative neurogliaform cells); *Lamp5*-*Tmem182* (putative canopy cells); *Lamp5*-*Chrna7* (putative layer-1 α7 cells); *Vip*-*Reln* (putative layer-1 *Vip* cells); *Vip*-*Cp* (other Vip cells); *Sncg*-*Pdzrn3* (putative large *Cck* cells); and *Sncg*-*Vip* (putative small *Cck*/*Vip* cells)."

**Example intermediate 'type': `Sst-Reln` (putative Martinotti cells)**  
This is also the exact example suggested in the user request, and it appears verbatim in the paper.

---

## Retrieval notes

- The Nature publisher page (https://www.nature.com/articles/s41586-022-04915-7) is JavaScript-rendered and does not expose article body text in the static HTTP response.  
- The Europe PMC page returned HTTP 403.  
- Full-text XML was successfully retrieved via the NCBI E-utilities OAI and eFetch endpoints (PMC9279161), which returned the complete article body as CC-BY open-access content.  
- The 50 KB web_fetch cap meant the formal "Online Methods" section (which appears at the end of the article XML) was not reached in the fetched window. However, all three facts requested appear verbatim in the main results text of the paper ("Identifying recorded inhibitory subtypes" subsection), which itself functions as the combined results+methods narrative; that section explicitly cross-references "see Methods for full explanation" for the type-level classification.  
- The formal Online Methods section is expected to contain further animal protocol details (e.g., ethics, housing, surgical procedures) beyond the n=4 mice statement above.
"""

with open("/work/bugeon_methods_extract.md", "w") as f:
    f.write(content)

print("Saved /work/bugeon_methods_extract.md")
print(f"File size: {len(content)} characters")
