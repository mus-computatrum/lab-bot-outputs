
content = """\
# Bugeon et al. 2022 — Methods Extract
**Citation:** Bugeon S, Duffield J, Dipoppa M, et al.
"A transcriptomic axis predicts state modulation of cortical interneurons."
*Nature* 607, 330–338 (2022). https://doi.org/10.1038/s41586-022-04915-7
**PMC:** PMC9279161 | **PMID:** 35794483
**Fetched from:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9279161/ (via NCBI E-utilities efetch, 2026-06-06)

---

## (a) Number of Mice

**Answer: 4 mice, across 17 recording sessions.**

Direct quote from the article body (Methods / Results overlap, paragraph on cell identification):

> "We applied this method to **17 recording sessions from 4 mice**, and obtained
> 89 ± 31 (mean ± s.d.) molecularly identified inhibitory cells together with
> 393 ± 173 pyramidal neurons per session, making a total of 1,090 unique
> molecularly identified inhibitory cells."

Corroborated by figure captions throughout (e.g. Fig. 3b): *"n = 4 mice, 17 sessions"*.

---

## (b) Three-Level Cell-Type Hierarchy

**Levels (bottom → top):** subtype → type → subclass

| Level | Count | Description |
|-------|-------|-------------|
| **Subclass** (top) | 5 | Broad marker-gene groupings: *Pvalb*, *Sst*, *Lamp5*, *Vip*, *Sncg* |
| **Type** (intermediate) | 11 | UMAP-suggested clusters putatively linked to morphological cell types |
| **Subtype** (lowest) | 35 | Fine transcriptomic clusters from prior scRNA-seq (Tasic et al.) |

Direct quote defining the hierarchy:

> "We classified these inhibitory cells using a **three-level hierarchy** (Fig. 1f).
> The **lowest** hierarchical level ('**subtype**') comprised the fine transcriptomic
> clusters defined previously, and the **top** level ('**subclass**') was the *Pvalb*,
> *Sst*, *Lamp5*, *Vip* and *Sncg* groupings that were defined in the same previous
> report. An **intermediate** level ('**type**') was suggested by uniform manifold
> approximation and projection (UMAP) analysis of scRNA-seq data (Extended Data
> Fig. 3), which revealed collections of clusters that we could putatively associate
> to morphological cell types."

From the abstract (same source):

> "We classified inhibitory neurons imaged in layers 1–3 into a three-level hierarchy
> of **5 subclasses, 11 types and 35 subtypes** using previously defined transcriptomic
> clusters."

---

## (c) Named Example of an Intermediate-Level 'Type'

**Example: *Sst-Reln* (putative Martinotti cells)**

Full list of the 11 named intermediate types, quoted directly:

> "We named these intermediate-level types
> ***Pvalb-Tac1*** (putative *Pvalb* basket cells);
> ***Pvalb-Vipr2*** (putative chandelier cells);
> ***Sst-Reln*** **(putative Martinotti cells)**;
> ***Sst-Tac1*** (putative non-Martinotti *Sst* cells);
> ***Lamp5-Npy*** (putative neurogliaform cells);
> ***Lamp5-Tmem182*** (putative canopy cells);
> ***Lamp5-Chrna7*** (putative layer-1 α7 cells);
> ***Vip-Reln*** (putative layer-1 *Vip* cells);
> ***Vip-Cp*** (other Vip cells);
> ***Sncg-Pdzrn3*** (putative large *Cck* cells); and
> ***Sncg-Vip*** (putative small *Cck*/*Vip* cells)."

The example *Sst-Reln (putative Martinotti cells)* is also used functionally in the text:

> "Within the *Sst* subclass, *Sst-Tac1* cells were most active during synchronized
> states, whereas ***Sst-Reln* cells were more active during running**."

---

## Source Note
All passages above were retrieved live from PMC full text (NCBI E-utilities API,
`efetch?db=pmc&id=PMC9279161&rettype=full&retmode=xml`), fetched 2026-06-06.
No information was drawn from model training memory.
"""

with open("/work/bugeon_methods_extract.md", "w") as f:
    f.write(content)

print("Saved. Line count:", content.count("\\n"))
print("\\nPreview of first 500 chars:")
print(content[:500])
