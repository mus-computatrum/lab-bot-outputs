# searchlit-easy-sst-v1-papers

**Mode**: search-lit  ·  **Effort**: standard

## Request

> Find 3-5 papers from 2023 or later on SST (somatostatin) interneuron diversity in mouse primary visual cortex (V1, VISp). For each: title, authors, year, journal/DOI, and ONE sentence on the key finding.

## Final summary

I now have enough verified papers to compile a strong, honest answer. Let me synthesize.

---

Here are **5 papers from 2023–2025** on SST interneuron diversity in mouse V1/VISp, all with confirmed abstracts and DOIs. I've ordered them from broadest transcriptomic taxonomy → functional/circuit-level diversity.

---

### 1. Yao et al. (2023) — *Nature*
**Title:** A high-resolution transcriptomic and spatial atlas of cell types in the whole mouse brain
**Authors:** Yao Z, van Velthoven CTJ, Kunst M, Zhang M, … Zhuang X, Zeng H (Allen Institute for Brain Science)
**DOI:** 10.1038/s41586-023-06812-z · PMID: 38092916
**Key finding:** Integrating ~4 million scRNA-seq cells with MERFISH spatial data across the entire adult mouse brain (including VISp), this atlas identifies **5,322 transcriptomic clusters** organized into 4 hierarchical levels, defining dozens of SST subtypes with region-specific spatial distributions.
> ⚠️ *Whole-brain scope; SST diversity in VISp is part of a much larger dataset — check the Allen Brain Cell Atlas portal for VISp-specific SST cluster breakdowns.*

---

### 2. Zhang et al. (2023) — *Nature*
**Title:** Molecularly defined and spatially resolved cell atlas of the whole mouse brain
**Authors:** Zhang M, Pan X, Jung W, Halpern AR, … Tasic B, Yao Z, Zeng H, Zhuang X (Zhuang Lab / Harvard)
**DOI:** 10.1038/s41586-023-06808-9 · PMID: 38092912
**Key finding:** MERFISH imaging of >1,100 genes across ~10 million cells in whole adult mouse brain yields **>5,000 transcriptomically distinct clusters** spatially registered to the Allen CCF, including in-situ resolution of SST subtype distributions within VISp layers.
> ⚠️ *Companion paper to Yao et al. 2023 — the spatial complement to the scRNA-seq atlas.*

---

### 3. Fisher et al. (2024) — *Neuron*
**Title:** Cortical somatostatin long-range projection neurons and interneurons exhibit divergent developmental trajectories
**Authors:** Fisher J, Verhagen M, Long Z, Moissidis M, … Marín O, Mi D, Lim L (King's College London / Tsinghua / KU Leuven)
**DOI:** 10.1016/j.neuron.2023.11.013 · PMID: 38086373
**Key finding:** Using scRNA-seq and spatial transcriptomics, SST⁺ cells in mouse cortex segregate embryonically into **two long-range projection neuron subtypes** and two interneuron types (Martinotti and non-Martinotti cells), with diversity refined through distinct postnatal developmental programs.

---

### 4. de Brito Van Velze et al. (2024) — *Cell Reports*
**Title:** Feedforward and disinhibitory circuits differentially control activity of cortical somatostatin interneurons during behavioral state transitions
**Authors:** de Brito Van Velze M, Dhanasobhon D, Martinez M, Morabito A, … Zerlaut Y, Rebola N (Paris Brain Institute / ICM)
**DOI:** 10.1016/j.celrep.2024.114197 · PMID: 38733587
**Key finding:** SST-INs in **V1 are not recruited by locomotion** (unlike S1), because feedforward thalamic sensory drive — not VIP-mediated disinhibition — is the dominant recruitment mechanism in visual cortex, revealing **region-specific functional diversity** of the same SST class.

---

### 5. Morabito et al. (2024) — *bioRxiv* ⚠️ preprint
**Title:** A dendritic substrate for temporal diversity of cortical inhibition
**Authors:** Morabito A, Zerlaut Y, Dhanasobhon D, Berthaux E, Tzilivaki A, … Poirazi P, Bacci A, DiGregorio D, Lourenço J, Rebola N (Paris Brain Institute / Institut Pasteur)
**DOI:** 10.1101/2024.07.09.602783 · PMID: 39026855
**Key finding:** SST-INs exhibit **NMDAR-dependent dendritic integration with uniform synapse density** (vs. passive integration with proximal enrichment in PV-INs), creating a long-lasting integrative inhibitory mode confirmed by in vivo V1 recordings in awake mice.

---

## Summary
Two large 2023 *Nature* atlas papers (Yao/Allen Institute; Zhang/Zhuang Lab) define the transcriptomic and spatial landscape of SST subtypes in VISp as part of whole-brain atlases. Fisher et al. 2024 (*Neuron*) traces how those transcriptomic subtypes (Martinotti, non-Martinotti, LRP) emerge developmentally. The two Paris Brain Institute papers (de Brito Van Velze 2024; Morabito 2024) reveal the functional/biophysical diversity underlying SST heterogeneity — including the surprising absence of locomotion-driven SST recruitment in V1 specifically.

## What I did
- Queried NCBI E-utilities (esearch + efetch) with multiple term combinations to find and verify abstracts + DOIs for all 5 papers.
- Restricted to 2023–2025; excluded non-peer-reviewed work except where the preprint was the best available source.
- Checked each abstract to confirm V1/VISp relevance and SST-diversity content.

## Caveats / next steps
- **Papers 1 & 2** are whole-brain atlases — SST-VISp subtypes are best explored via the [Allen Brain Cell Atlas](https://portal.brain-map.org/atlases-and-data/bkp/abc-atlas) portal rather than the PDFs alone.
- **Paper 5** (Morabito) is still a preprint; no peer-reviewed journal version found as of June 2025.
- The search did **not** turn up a focused in vivo 2-photon imaging paper specifically comparing SST subtype visual responses in V1 — if that's the target, a deeper bioRxiv or Google Scholar search filtered to "Martinotti" or "SST layer 4/5/6 V1" may be warranted.
- Semantic Scholar was rate-limited throughout; a second pass with that tool might surface additional hits.
