text = r'''# Bugeon et al. 2022, Nature — Methods/Results extract

**Paper:** "A transcriptomic axis predicts state modulation of cortical interneurons"
Bugeon, Duffield, Dipoppa, ... Carandini, Harris. *Nature* 607, 330-338 (2022).
doi:10.1038/s41586-022-04915-7 - PMID 35794483

**Sources fetched (live web):**
- https://www.nature.com/articles/s41586-022-04915-7 - JS-rendered; static HTML returns only
  the JSON-LD abstract metadata, NOT the Methods/Results body.
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=PMC9279161 - live NCBI PMC
  full text of the same article (used for the verbatim quotes below).

---

## (a) How many mice

**4 mice.**

> "We applied this method to **17 recording sessions from 4 mice**, and obtained 89 +/- 31
> (mean +/- s.d.) molecularly identified inhibitory cells together with 393 +/- 173 pyramidal
> neurons per session, making a total of 1,090 unique molecularly identified inhibitory cells"

Corroborated by figure legends, e.g. Fig. 1i "(n = 4 mice)" and Fig. 3b "(n = 4 mice, 17 sessions)".

---

## (b) Three-level cell-type hierarchy (subclass -> type -> subtype)

> "We classified inhibitory neurons imaged in layers 1-3 into a **three-level hierarchy of
> 5 subclasses, 11 types and 35 subtypes** using previously defined transcriptomic clusters." (Abstract)

Definitions of each level (from "Identifying recorded inhibitory subtypes"):

> "We classified these inhibitory cells using a three-level hierarchy (Fig. 1f). The lowest
> hierarchical level ('**subtype**') comprised the fine transcriptomic clusters defined
> previously, and the top level ('**subclass**') was the Pvalb, Sst, Lamp5, Vip and Sncg
> groupings that were defined in the same previous report. An intermediate level ('**type**')
> was suggested by uniform manifold approximation and projection (UMAP) analysis of scRNA-seq
> data ... which revealed collections of clusters that we could putatively associate to
> morphological cell types"

- **Subclass (top, 5):** Pvalb, Sst, Lamp5, Vip, Sncg.
- **Type (intermediate, 11):** UMAP-derived collections of clusters putatively mapped to
  morphological cell types.
- **Subtype (lowest, 35):** the fine transcriptomic clusters (from prior scRNA-seq); imaged
  cells fell into 35 superficial-inhibitory clusters.

---

## (c) One named example of an intermediate-level 'type'

**Sst-Reln (putative Martinotti cells).**

Full list of the 11 named types, quoted verbatim:

> "We named these intermediate-level types Pvalb-Tac1 (putative Pvalb basket cells);
> Pvalb-Vipr2 (putative chandelier cells); **Sst-Reln (putative Martinotti cells)**;
> Sst-Tac1 (putative non-Martinotti Sst cells); Lamp5-Npy (putative neurogliaform cells);
> Lamp5-Tmem182 (putative canopy cells); Lamp5-Chrna7 (putative layer-1 a7 cells);
> Vip-Reln (putative layer-1 Vip cells); Vip-Cp (other Vip cells);
> Sncg-Pdzrn3 (putative large Cck cells); and Sncg-Vip (putative small Cck/Vip cells)."
'''
with open('/work/bugeon_methods_extract.md','w') as f:
    f.write(text)
print('bytes:', len(text))
print(open('/work/bugeon_methods_extract.md').read()[:300])
