# searchlit-internet-recent-sst-papers

**Mode**: search-lit  ·  **Effort**: standard

## Request

> Find 2 peer-reviewed papers published in 2023 or 2024 on Sst (somatostatin) interneuron classification in mouse cortex. For each, report: title, first author, year, venue, DOI, and 1-2 sentences on the key finding. You must use the web/scholarly tools (pubmed_search / arxiv_search / semantic_scholar / web_fetch) — do NOT answer from memory. Save the summary as /work/summary.md (the harness inserts a header automatically; just include your findings).

## Final summary

Both DOIs are confirmed from the NCBI record. Note: in search-lit mode I have no sandbox/file-write tool, so I cannot physically create `/work/summary.md` — I'm providing the exact markdown content below for the harness to save.

---

**Content for /work/summary.md:**

```markdown
# Sst Interneuron Classification in Mouse Cortex — 2 Papers (2023–2024)

## 1. A brief history of somatostatin interneuron taxonomy or: how many somatostatin subtypes are there, really?
- First author: Agmon (Ariel Agmon; with Alison L. Barth)
- Year: 2024 (epub 2024 Jul 17)
- Venue: Frontiers in Neural Circuits, vol. 18, art. 1436915
- DOI: 10.3389/fncir.2024.1436915 (PMID 39091993, PMC11292610)
- Key finding: A perspective/review arguing that, of the proliferating scRNA-seq classification levels, the most experimentally useful taxonomic granularity for cortical Sst interneurons is ~10 "supertypes," which align well with traditional morpho-electro-chemical types. It contends that finer "t-types"/clusters based on subtle gene-expression differences lack clear phenotypic correlates and are less useful for researchers.

## 2. Cortical somatostatin long-range projection neurons and interneurons exhibit divergent developmental trajectories
- First author: Fisher (Jonathan Fisher; senior author Lynette Lim)
- Year: 2024 (issue Feb 21, 2024; epub 2023 Dec 11)
- Venue: Neuron, 112(4):558–573.e8
- DOI: 10.1016/j.neuron.2023.11.013 (PMID 38086373, PMC7618239)
- Key finding: Combining single-cell RNA-seq and spatial transcriptomics, the authors show SST+ cells segregate during embryonic stages into long-range projection (LRP) neurons and two interneuron classes (Martinotti and non-Martinotti) along distinct developmental trajectories, with diversification timing unique to each subtype and especially divergent for LRP neurons.
```

---

## Summary
I verified two peer-reviewed papers on Sst interneuron classification in mouse cortex from 2023–2024 using PubMed and the NCBI record (DOIs confirmed from the structured metadata, not memory). Agmon & Barth (2024, *Front. Neural Circuits*) argue ~10 "supertypes" is the most useful taxonomic level; Fisher et al. (2024, *Neuron*) show SST+ cells split early in development into long-range projection neurons vs. Martinotti/non-Martinotti interneurons.

## What I did
Ran targeted PubMed searches confirming PMIDs 39091993 and 38086373, then fetched the NCBI esummary endpoint to verify exact DOIs, venues, volumes, and authors. Compiled the findings as markdown content for `/work/summary.md` (provided inline above, since search-lit mode has no file-write tool).

## Caveats / next steps
- I could not physically write `/work/summary.md` — no sandbox/file tool exists in search-lit mode; please save the block above.
- Fisher et al. is a Feb-2024 issue with a Dec-2023 epub, so it satisfies "2023 or 2024" either way.
- Both were already in my cross-job notes; live tool lookups confirmed and updated the exact citation details. With more time I could add 1–2 alternative candidates (e.g., the Allen/BICCN whole-cortex taxonomy papers) if you want options beyond these two.
