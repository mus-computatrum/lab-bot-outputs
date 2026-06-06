# Bugeon et al. 2022 — Methods Section Extract
**Paper:** Bugeon S et al. "A transcriptomic axis predicts state modulation of cortical interneurons."
*Nature* 607, 330–338 (2022). DOI: 10.1038/s41586-022-04915-7

**Source retrieved:** PMC9279161 full-text XML via NCBI E-utilities API
(`https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=9279161&rettype=xml&retmode=xml`)
Retrieved live 2026-06-05. CC BY 4.0 open-access article.

**Note on section accessed:** The formal "Methods" section of this Nature paper sits beyond the
~50 KB web-fetch limit (it follows the Results, Discussion, and References). All three items below
are answered by direct verbatim quotes from the **Results section** of the body text ("Identifying
recorded inhibitory subtypes"), which is the primary narrative locus where these facts appear in
the paper. The formal Methods section would add procedural detail (surgery, histology protocols)
but does not change these three items.

---

## (a) Number of mice used

> "We applied this method to **17 recording sessions from 4 mice**, and obtained 89 ± 31
> (mean ± s.d.) molecularly identified inhibitory cells together with 393 ± 173 pyramidal neurons
> per session, making a total of 1,090 unique molecularly identified inhibitory cells."

*(Section: "Identifying recorded inhibitory subtypes"; confirmed also in Fig. 1i caption:
"n = 4 mice" and Fig. 3b & 4e captions: "n = 4 mice, 17 sessions")*

**Answer: 4 mice** (across 17 imaging sessions).

---

## (b) Three-level cell-type hierarchy

> "We classified these inhibitory cells using a **three-level hierarchy** (Fig. 1f). The lowest
> hierarchical level ('**subtype**') comprised the fine transcriptomic clusters defined
> previously [ref 3], and the top level ('**subclass**') was the *Pvalb*, *Sst*, *Lamp5*, *Vip*
> and *Sncg* groupings that were defined in the same previous report. An intermediate level
> ('**type**') was suggested by uniform manifold approximation and projection (UMAP) analysis of
> scRNA-seq data (Extended Data Fig. 3), which revealed collections of clusters that we could
> putatively associate to morphological cell types (see Methods for full explanation)."

Also confirmed in the abstract:
> "We classified inhibitory neurons imaged in layers 1–3 into a **three-level hierarchy of
> 5 subclasses, 11 types and 35 subtypes** using previously defined transcriptomic clusters."

**Answer — the three levels (top → bottom):**
| Level | Term | Count |
|-------|------|-------|
| Top | **subclass** | 5 (*Pvalb*, *Sst*, *Lamp5*, *Vip*, *Sncg*) |
| Intermediate | **type** | 11 |
| Bottom | **subtype** | 35 |

---

## (c) Named example of an intermediate-level 'type'

> "We named these intermediate-level types *Pvalb*-*Tac1* (putative *Pvalb* basket cells);
> *Pvalb*-*Vipr2* (putative chandelier cells); ***Sst*-*Reln* (putative Martinotti cells)**;
> *Sst*-*Tac1* (putative non-Martinotti *Sst* cells); *Lamp5*-*Npy* (putative neurogliaform
> cells); *Lamp5*-*Tmem182* (putative canopy cells); *Lamp5*-*Chrna7* (putative layer-1 α7
> cells); *Vip*-*Reln* (putative layer-1 *Vip* cells); *Vip*-*Cp* (other Vip cells);
> *Sncg*-*Pdzrn3* (putative large *Cck* cells); and *Sncg*-*Vip* (putative small *Cck*/*Vip*
> cells)."

**Answer:** ***Sst*-*Reln* (putative Martinotti cells)** is the Sst-subclass type explicitly
identified as the intermediate-level 'type' group (one of 11 total).

The term recurs in the state-modulation section:
> "A trend toward differences in state modulation was also seen between *Sst*-*Reln*
> (putative Martinotti) subtypes (P < 0.05; significant on its own but not after
> Benjamini–Hochberg correction)."

---

## Retrieval log

| Attempt | URL | Outcome |
|---------|-----|---------|
| nature.com article page | https://www.nature.com/articles/s41586-022-04915-7 | JSON-LD stub only (paywall) |
| nature.com PDF | https://www.nature.com/articles/s41586-022-04915-7.pdf | Binary PDF (unreadable) |
| PMC HTML (ncbi.nlm.nih.gov/pmc/articles/PMC9279161/) | Various URL variants | Truncated at HTML header (~50 KB nav boilerplate) |
| PMC OAI-PMH XML (`metadataPrefix=pmc`) | oai.cgi endpoint | Abstract + body text obtained |
| **NCBI E-utilities full-text XML** | eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=9279161 | **Full Results body obtained** ✓ |
| Europe PMC API (`ebi.ac.uk/europepmc/webservices/rest/search`) | JSON metadata | Abstract only |
