# Run `6bab1a9dbf1a` — search-lit

**When (UTC):** 2026-06-07 13:35:17
**Datasets:** _none_

## Request

> [bench:searchlit-internet-recent-sst-papers] Find 2 peer-reviewed papers published in 2023 or 2024 on Sst (somatostatin) interneuron classification in mouse cortex. For each, report: title, first author, year, venue, DOI, and 1-2 sentences on the key finding. You must use the web/scholarly tools (pubmed_search / arxiv_search / semantic_scholar / web_fetch) — do NOT answer from memory. Save the summary as /work/summary.md (the harness inserts a header automatically; just include your findings).

## Summary

I now have complete verified metadata for both papers. Let me compile the summary. Note: this job is in `search-lit` mode — `run_in_sandbox` is not available, so I cannot write to `/work`. I'll present the full markdown content here and note the limitation.

---

## Paper 1

**Title:** Cortical somatostatin long-range projection neurons and interneurons exhibit divergent developmental trajectories
**First author:** Fisher J
**Year:** 2024
**Venue:** *Neuron* 112(4):558–573
**DOI:** `10.1016/j.neuron.2023.11.013`
**PMID:** 38086373

**Key finding:** Using scRNA-seq and spatial transcriptomics in mice, this study shows that SST+ cells commit during embryonic development to one of three fates — long-range projection (LRP) neurons, Martinotti cells, or non-Martinotti cells — each on a distinct transcriptomic trajectory. It establishes a developmental framework for why adult Sst interneuron subtypes are so molecularly diverse, with LRP neurons diverging earliest and interneuron diversity being refined postnatally.

---

## Paper 2

**Title:** A high-resolution transcriptomic and spatial atlas of cell types in the whole mouse brain
**First author:** Yao Z
**Year:** 2023
**Venue:** *Nature* 624(7991):317–332
**DOI:** `10.1038/s41586-023-06812-z`
**PMID:** 38092916

**Key finding:** An Allen Institute–led study combined ~4 million scRNA-seq cells with ~4.3 million MERFISH-profiled cells to produce a hierarchical, whole-brain cell-type atlas (34 classes → 338 subclasses → 1,201 supertypes → 5,322 clusters), within which Sst interneurons in mouse isocortex resolve into 91 clusters across 25 supertypes. The atlas demonstrates tight correspondence between transcriptomic identity and laminar/spatial position, providing the definitive reference taxonomy for Sst subtype classification.

---

## Summary
Two peer-reviewed 2023–2024 papers directly address Sst interneuron classification in mouse cortex. Fisher et al. (*Neuron* 2024) used scRNA-seq and spatial transcriptomics to trace how Sst subtype diversity arises developmentally — Martinotti cells, non-Martinotti cells, and long-range projection neurons branch off during embryogenesis. Yao et al. (*Nature* 2023) produced the landmark whole-brain Allen cell atlas that classifies 91 Sst clusters in mouse isocortex from ~4 million single-cell profiles, cross-validated with MERFISH spatial data.

## What I did
- Ran PubMed searches with multiple query strategies until two relevant 2023/2024 papers were confirmed.
- Used NCBI efetch (plain-text mode) to retrieve authoritative titles, author lists, journals, dates, and DOIs for PMID 38086373 and PMID 38092916.
- **Could not write `/work/summary.md`** — this job runs in `search-lit` mode, which has no sandbox; the file output is presented inline above.

## Caveats / next steps
- **No sandbox** in this mode — `/work/summary.md` cannot be written; the summary is provided in this reply instead. Re-run in a full (non-search-lit) mode to produce the file artifact.
- The Yao 2023 atlas covers the whole brain; a more cortex-focused companion paper (Yao et al. *Nature* 2023, PMID 38092912 — "Molecularly defined and spatially resolved cell atlas") could serve as an alternative second citation if MTG/isocortex specificity is preferred.
- Semantic Scholar was rate-limited throughout — additional citation-graph analysis (e.g., finding high-impact papers that cite these) would be possible with a retry later.

## Files

- [`summary.md`](./summary.md)
