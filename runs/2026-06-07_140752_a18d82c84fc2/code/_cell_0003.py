md = r"""# Bugeon et al. 2022, Nature — Methods/Results extract

**Paper:** "A transcriptomic axis predicts state modulation of cortical interneurons"
**DOI:** 10.1038/s41586-022-04915-7 — *Nature* 607(7918):330–338 (2022)
**Requested page:** https://www.nature.com/articles/s41586-022-04915-7
**How retrieved (live web):** The Nature article page is JavaScript-rendered; `web_fetch`
returned only the embedded abstract JSON (which already confirms the hierarchy). The full
open-access text — identical article, same DOI — was fetched live from the NCBI PMC mirror
(PMC9279161, eFetch full XML) to quote the Methods/Results verbatim. Nothing below is from
memory; every quoted block is copied from the live document.

---

## (a) How many mice were used

Main functional-neuromics dataset = **4 mice**. Verbatim:

> "We applied this method to 17 recording sessions from 4 mice, and obtained 89 ± 31
> (mean ± s.d.) molecularly identified inhibitory cells together with 393 ± 173 pyramidal
> neurons per session, making a total of 1,090 unique molecularly identified inhibitory
> cells (some of which were recorded in multiple sessions; Supplementary Data 1)."

Methods section, verbatim:

> "For post-hoc identification of transcriptomic subtypes, four (two males and two females)
> Gad2-T2a-NLS-mCherry transgenic mice (stock no: 023140, The Jackson Laboratory),
> expressing the red fluorescent protein mCherry in the nuclei of Gad2-expressing cells,
> were used. For comparison to transgenic mouse lines (Extended Data Fig. 5), additional
> experiments were performed as in ref. 30 using one male Pvalb tm1(cre)Arbr and two males
> and one female Sst tm2.1(cre)Zjh crossed with Gt(ROSA)26Sor tm14(CAG-tdTomato)Hze."

So: **4 mice** for the core transcriptomic dataset, plus **4 additional mice** (1 Pvalb-Cre
+ 3 Sst-Cre crosses) used only for the transgenic-line comparison in Extended Data Fig. 5.

---

## (b) The three-level cell-type hierarchy (subclass → type → subtype)

Verbatim (abstract / Results):

> "We classified inhibitory neurons imaged in layers 1–3 into a three-level hierarchy of
> 5 subclasses, 11 types and 35 subtypes using previously defined transcriptomic clusters."

Verbatim definition of each level (Results):

> "We classified these inhibitory cells using a three-level hierarchy (Fig. 1f). The lowest
> hierarchical level ('subtype') comprised the fine transcriptomic clusters defined
> previously, and the top level ('subclass') was the Pvalb, Sst, Lamp5, Vip and Sncg
> groupings that were defined in the same previous report. An intermediate level ('type')
> was suggested by..."

Verbatim (Methods, on how the levels nest):

> "The final population of 1,065 cells belonged to 35 transcriptomic subtypes. For
> hierarchical analysis, the 35 subtypes were grouped into 11 types corresponding to
> putative anatomical or physiological cell types based on the previous literature."

Summary of the hierarchy:
- **Subclass (top, n = 5):** Pvalb, Sst, Lamp5, Vip, Sncg
- **Type (intermediate, n = 11):** putative anatomical/physiological cell types (named below)
- **Subtype (lowest, n = 35):** fine transcriptomic clusters from Tasic-style scRNA-seq

---

## (c) A named example of an intermediate-level 'type'

Requested example confirmed verbatim. Full naming sentence (Results):

> "We named these intermediate-level types Pvalb-Tac1 (putative Pvalb basket cells);
> Pvalb-Vipr2 (putative chandelier cells); Sst-Reln (putative Martinotti cells);
> Sst-Tac1 (putative non-Martinotti Sst cells); Lamp5-Npy (putative neurogliaform cells);
> Lamp5-Tmem182 (putative canopy cells); Lamp5-Chrna7 (putative layer-1 α7 cells);
> Vip-Reln (putative layer-1 Vip cells); Vip-Cp (other Vip cells);
> Sncg-Pdzrn3 (putative large Cck cells); and Sncg-Vip (putative small Cck / Vip cells)."

That is the complete list of all 11 types. The canonical requested example:

> **Sst-Reln (putative Martinotti cells)**
"""
with open("/work/bugeon_methods_extract.md","w") as f:
    f.write(md)
print("wrote /work/bugeon_methods_extract.md", len(md), "chars")
