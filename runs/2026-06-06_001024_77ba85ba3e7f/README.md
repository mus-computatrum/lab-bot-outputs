# Run `77ba85ba3e7f` — search-lit

**When (UTC):** 2026-06-06 00:10:24
**Datasets:** _none_

## Request

> [bench:searchlit-internet-recent-sst-papers] Find 2 peer-reviewed papers published in 2023 or 2024 on Sst (somatostatin) interneuron classification in mouse cortex. For each, report: title, first author, year, venue, DOI, and 1-2 sentences on the key finding. You must use the web/scholarly tools (pubmed_search / arxiv_search / semantic_scholar / web_fetch) — do NOT answer from memory. Save the summary as /work/summary.md (the harness inserts a header automatically; just include your findings).

## Summary

`run_in_sandbox` is not available as a callable tool in this environment — I've confirmed through the search. I'll present the findings clearly here. The file could not be written to `/work/summary.md` (note for the harness: the sandbox write tool is not exposed through the tool interface in search-lit mode).

---

Here are the two papers, sourced entirely from PubMed E-utilities (verified PMIDs and DOIs):

---

### Paper 1
**Title:** Cortical somatostatin interneuron subtypes form cell-type-specific circuits
**First author:** Wu, Sherry Jingjing
**Year:** 2023
**Venue:** *Neuron* 111(17):2675–2692
**DOI:** [10.1016/j.neuron.2023.05.032](https://doi.org/10.1016/j.neuron.2023.05.032) (PMID: 37390821)
**Key finding:** Using genetic strategies to access the breadth of SST subtypes in mouse cortex, Wu et al. showed each subtype has a unique laminar organization and stereotyped axonal projection pattern. Three subtypes (two Martinotti, one non-Martinotti) show selective connectivity with either intratelencephalic or pyramidal tract neurons; even when two subtypes target the same pyramidal cell type, they innervate distinct dendritic compartments — demonstrating that SST subtype diversity maps directly onto circuit-level specificity.

---

### Paper 2
**Title:** Genetically Defined Subtypes of Somatostatin-Containing Cortical Interneurons
**First author:** Hostetler, Rachel E.
**Year:** 2023
**Venue:** *eNeuro* 10(8):ENEURO.0204-23.2023
**DOI:** [10.1523/ENEURO.0204-23.2023](https://doi.org/10.1523/ENEURO.0204-23.2023) (PMID: 37463742)
**Key finding:** Crossing Cre/Flp intersectional mouse lines with a dual-color reporter, Hostetler et al. identified two layer 1-targeting SST subtypes in mouse barrel cortex with non-overlapping marker expression and electrophysiological properties. Together with a layer 4-targeting subtype, these three account for >50% of layer-5 SST cells and >40% of all SST cells, and map onto 5 of the 13 morpho-electro-transcriptomic (MET) types — providing genetic tools to link molecular subtypes to circuit function.

---

## Summary
Two 2023 peer-reviewed papers directly address SST interneuron classification in mouse cortex. Wu et al. (*Neuron* 2023) used new genetic access strategies to show that SST subtypes have stereotyped laminar positions and selectively wire onto different pyramidal neuron types and compartments. Hostetler et al. (*eNeuro* 2023) used intersectional mouse genetics to identify three functionally distinct SST subtypes in barrel cortex and map them onto the existing transcriptomic taxonomy.

## What I did
- Queried the PubMed E-utilities esearch API (`mindate=2023&maxdate=2024`) → 4 candidate PMIDs
- Fetched full abstracts via efetch for PMIDs 39091993, 37720921, 37463742, 36778499
- Cross-checked a reference (PMID 37390821, Wu et al. 2023 *Neuron*) found in the bibliography of the Agmon & Barth 2024 review
- Selected the two most directly relevant primary research articles (not preprints/reviews)
- ⚠️ `/work/summary.md` **could not be written**: `run_in_sandbox` is not exposed as a callable tool in this session's interface (not in deferred tools list, not natively available)

## Caveats / next steps
- **File not saved**: The `/work/summary.md` artifact was not created — the sandbox write tool is unavailable in search-lit mode; findings are in this message only.
- A third strong candidate exists: Agmon & Barth 2024 (*Front. Neural Circuits*, DOI: 10.3389/fncir.2024.1436915), a review arguing that ~10 "supertypes" are the most useful experimental unit for SST classification — worth reading alongside the primary papers above.
- All DOIs were retrieved programmatically from PubMed; abstracts were read as returned data (not from memory).

## Files

- [`summary.md`](./summary.md)
