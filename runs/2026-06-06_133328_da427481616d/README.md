# Run `da427481616d` — search-lit

**When (UTC):** 2026-06-06 13:33:28
**Datasets:** _none_

## Request

> [bench:searchlit-internet-recent-sst-papers] Find 2 peer-reviewed papers published in 2023 or 2024 on Sst (somatostatin) interneuron classification in mouse cortex. For each, report: title, first author, year, venue, DOI, and 1-2 sentences on the key finding. You must use the web/scholarly tools (pubmed_search / arxiv_search / semantic_scholar / web_fetch) — do NOT answer from memory. Save the summary as /work/summary.md (the harness inserts a header automatically; just include your findings).

## Summary

The `/work` path lives inside the Docker sandbox container, which isn't available in this `search-lit` mode job (no `run_in_sandbox` is provisioned). I'll deliver the full summary inline — here it is formatted exactly as it would appear in `summary.md`:

---

## Paper 1

**Title:** Genetically Defined Subtypes of Somatostatin-Containing Cortical Interneurons

**First author:** Hostetler RE

**Year:** 2023

**Venue:** *eNeuro*

**DOI:** `10.1523/ENEURO.0204-23.2023`

**Key finding:** Using intersectional Cre × Flp mouse driver lines with a dual-color combinatorial reporter, the authors identified two layer 1-targeting Sst subtypes in deep cortical layers with non-overlapping marker protein expression and electrophysiological properties. Together with a previously characterized layer 4-targeting subtype, these three account for >40% of all cortical Sst interneurons and map onto 5 of the 13 morpho-electro-transcriptomic (MET) types defined by large-scale single-cell studies.

---

## Paper 2

**Title:** A brief history of somatostatin interneuron taxonomy or: how many somatostatin subtypes are there, really?

**First author:** Agmon A

**Year:** 2024

**Venue:** *Frontiers in Neural Circuits*

**DOI:** `10.3389/fncir.2024.1436915`

**Key finding:** Drawing on a decade of NIH-supported single-cell RNA-seq atlases, this review argues that ~10 "supertypes" represent the most experimentally useful level of Sst interneuron taxonomy because they align with traditional morphological, electrophysiological, and neurochemical features. Finer transcriptomic t-type/cluster divisions — which double roughly every two years — lack clear phenotypic correlates and may hinder rather than guide experimental neuroscience.

---

*Sources retrieved 2026-06-06 via NCBI E-utilities. PMIDs: 37463742 (Hostetler 2023), 39091993 (Agmon 2024).*

---

## Summary
Two peer-reviewed papers (2023–2024) on Sst interneuron classification in mouse cortex were identified via PubMed E-utilities. Hostetler et al. (eNeuro 2023) used intersectional mouse genetics to physically map genetically defined Sst subtypes onto MET types. Agmon & Barth (Front. Neural Circuits 2024) reviewed the entire classification landscape and advocate for ~10 "supertypes" as the most useful experimental unit.

## What I did
- Queried NCBI E-utilities esearch (2023–2024 date filter) → retrieved 4 PMIDs
- Fetched full abstracts via efetch for all 4 records
- Selected the 2 most directly relevant peer-reviewed papers on Sst classification (excluded the Atsumi 2023 circuit-tracing paper and the Hostetler bioRxiv preprint, which is the same work as the eNeuro paper)
- Attempted to save `/work/summary.md`; blocked because search-lit mode has no sandbox; summary delivered inline above

## Caveats / next steps
- **`/work/summary.md` was NOT written** — search-lit mode does not provision `run_in_sandbox`; a sandbox-enabled job would be needed to persist the file
- PubMed query returned only 4 hits — a broader query (e.g., adding "transcriptomics" or "single-cell") might surface additional 2023–2024 papers (e.g., from the Allen Brain Cell Atlas work)
- Semantic Scholar returned 429 (rate-limited) throughout; could yield additional relevant hits if retried

## Files

- [`summary.md`](./summary.md)
