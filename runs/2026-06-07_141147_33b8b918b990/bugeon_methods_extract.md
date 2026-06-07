# Bugeon et al. 2022, Nature — Methods/Results extract
**Article:** "A transcriptomic axis predicts state modulation of cortical interneurons"
**DOI:** 10.1038/s41586-022-04915-7 · Nature 607(7918):330-338 · PMID 35794483 · PMC9279161

## Provenance (live web only)
- Requested source https://www.nature.com/articles/s41586-022-04915-7 returned a 303 redirect to
  idp.nature.com/authorize?... (auth wall) and the article body is JS-rendered, so no static Methods
  text is served there.
- Full text was therefore pulled live from the open-access PMC mirror of the IDENTICAL article via NCBI
  E-utilities eFetch (PMC XML):
  https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=PMC9279161&rettype=full&retmode=xml
  (CC BY 4.0). All quotes below are verbatim from that document.

---

## (a) How many mice
> "We applied this method to **17 recording sessions from 4 mice**, and obtained 89 +/- 31 (mean +/- s.d.)
> molecularly identified inhibitory cells together with 393 +/- 173 pyramidal neurons per session, making a
> total of 1,090 unique molecularly identified inhibitory cells (some of which were recorded in multiple
> sessions; Supplementary Data 1)."

Corroborating quote (abstract):
> "We classified inhibitory neurons imaged in layers 1-3 into a three-level hierarchy of **5 subclasses,
> 11 types and 35 subtypes** using previously defined transcriptomic clusters."

Figure-legend confirmation (n = 4 mice):
> "Mean expression of the 72 genes ... for the 35 subtypes, ordered as in f (n = 4 mice)."
> "... box plots showing the distributions of state modulation ... (n = 4 mice, 17 sessions ...)."

---

## (b) Three-level cell-type hierarchy (subclass -> type -> subtype)
> "We classified these inhibitory cells using a **three-level hierarchy** (Fig. 1f). The lowest
> hierarchical level ('**subtype**') comprised the fine transcriptomic clusters defined previously, and
> the top level ('**subclass**') was the Pvalb, Sst, Lamp5, Vip and Sncg groupings that were defined in
> the same previous report. An intermediate level ('**type**') was suggested by uniform manifold
> approximation and projection (UMAP) analysis of scRNA-seq data (Extended Data Fig. 3), which revealed
> collections of clusters that we could putatively associate to morphological cell types."

So, top -> bottom:
- **Subclass** (top, 5): Pvalb, Sst, Lamp5, Vip, Sncg - defined by marker genes.
- **Type** (intermediate, 11): UMAP-derived collections of clusters mapped to morphological cell types.
- **Subtype** (lowest, 35 recorded): fine transcriptomic scRNA-seq clusters.

---

## (c) Named example of an intermediate-level 'type'
> "We named these intermediate-level types **Pvalb-Tac1 (putative Pvalb basket cells)**;
> **Pvalb-Vipr2 (putative chandelier cells)**; **Sst-Reln (putative Martinotti cells)**;
> **Sst-Tac1 (putative non-Martinotti Sst cells)**; **Lamp5-Npy (putative neurogliaform cells)**;
> **Lamp5-Tmem182 (putative canopy cells)**; **Lamp5-Chrna7 (putative layer-1 a7 cells)**;
> **Vip-Reln (putative layer-1 Vip cells)**; **Vip-Cp (other Vip cells)**;
> **Sncg-Pdzrn3 (putative large Cck cells)**; and **Sncg-Vip (putative small Cck/Vip cells)**."

Single requested example: **Sst-Reln (putative Martinotti cells)**.

---

## Extra context quoted verbatim
> "Cells that were functionally imaged in vivo were assigned to a subtype (and thus also a type and
> subclass) using pciSeq, a Bayesian algorithm that computes for each cell a probability distribution
> over clusters defined by previous scRNA-seq data."

> "We performed two-photon calcium imaging in mice expressing mCherry in inhibitory neurons
> (Gad2-T2a-NLS-mCherry), injected with a pan-neuronal GCaMP6m virus (AAV1-Syn-GCaMP6m-WPRE-SV40), and
> then applied in situ transcriptomics to sagittal slices of the imaged region."
