# Run `1990da02b4fe` — search-lit

**When (UTC):** 2026-06-07 13:55:21
**Datasets:** _none_

## Request

> [bench:searchlit-internet-recent-sst-papers] Find 2 peer-reviewed papers published in 2023 or 2024 on Sst (somatostatin) interneuron classification in mouse cortex. For each, report: title, first author, year, venue, DOI, and 1-2 sentences on the key finding. You must use the web/scholarly tools (pubmed_search / arxiv_search / semantic_scholar / web_fetch) — do NOT answer from memory. Save the summary as /work/summary.md (the harness inserts a header automatically; just include your findings).

## Summary

Here are the exact contents to save as `/work/summary.md` (I can't write files in search-lit mode — no sandbox is wired):

```markdown
# Sst interneuron classification in mouse cortex — 2 recent papers (2023–2024)

## 1. A brief history of somatostatin interneuron taxonomy: how many somatostatin subtypes are there, really?
- **First author:** Agmon, A. (with Barth, A. L.)
- **Year:** 2024
- **Venue:** Frontiers in Neural Circuits, 18:1436915
- **DOI:** 10.3389/fncir.2024.1436915  (PMID 39091993)
- **Key finding:** Review of the decade-long scRNA-seq effort to taxonomize cortical Sst interneurons. Argues that for experimental work the most useful level is ~10 "supertypes" (which align with classical morpho-electro-chemical types), and that finer "t-types"/clusters based on small gene-expression differences are less useful and may defeat the purpose of classification.

## 2. Cortical somatostatin long-range projection neurons and interneurons exhibit divergent developmental trajectories
- **First author:** Fisher, J. (senior author Lim, L.)
- **Year:** 2024 (published Feb 2024; e-pub Dec 2023)
- **Venue:** Neuron, 112(4):558–573.e8
- **DOI:** 10.1016/j.neuron.2023.11.013  (PMID 38086373)
- **Key finding:** Using scRNA-seq + spatial transcriptomics, SST+ cells segregate embryonically into long-range projection (LRP) neurons and two interneuron types (Martinotti and non-Martinotti), each following distinct developmental trajectories; diversification timing differs by subtype and is especially divergent for LRP neurons.
```

## Summary
I found two peer-reviewed papers (both 2024, one e-published Dec 2023) directly on Sst interneuron classification in mouse cortex: a Frontiers in Neural Circuits review (Agmon & Barth) advocating a ~10-"supertype" taxonomy, and a Neuron study (Fisher et al.) showing SST+ cells split early into long-range projection neurons vs. Martinotti/non-Martinotti interneurons. All details (titles, authors, venues, DOIs) were verified from live PubMed and NCBI esummary output.

## What I did
Ran PubMed searches, then pulled authoritative metadata/DOIs from NCBI esummary (Semantic Scholar was rate-limited). Saved a durable lab note. Provided the full `/work/summary.md` text above.

## Caveats / next steps
This mode has no sandbox, so I could not write the file myself — please paste the block above into `/work/summary.md`. The Neuron paper's print year is 2024 (online Dec 2023); it qualifies under the 2023–2024 window either way. Many other 2024 Sst-taxonomy papers exist (e.g., BICCN atlas updates) if you want a broader set.

## Files

- [`summary.md`](./summary.md)
