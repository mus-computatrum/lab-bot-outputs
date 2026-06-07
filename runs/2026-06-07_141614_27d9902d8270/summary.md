# searchlit-internet-recent-sst-papers

**Mode**: search-lit  ·  **Effort**: standard

## Request

> Find 2 peer-reviewed papers published in 2023 or 2024 on Sst (somatostatin) interneuron classification in mouse cortex. For each, report: title, first author, year, venue, DOI, and 1-2 sentences on the key finding. You must use the web/scholarly tools (pubmed_search / arxiv_search / semantic_scholar / web_fetch) — do NOT answer from memory. Save the summary as /work/summary.md (the harness inserts a header automatically; just include your findings).

## Final summary

I have everything verified. Note: in **search-lit** mode there's no sandbox or file-writing tool wired in, so I cannot physically write `/work/summary.md` — I'm providing the exact file contents below for the harness/you to save.

---

```markdown
# Sst Interneuron Classification in Mouse Cortex — 2 Peer-Reviewed Papers (2023–2024)

## 1. Genetically Defined Subtypes of Somatostatin-Containing Cortical Interneurons
- **First author:** Hostetler RE (Hostetler, Hu, Agmon)
- **Year:** 2023
- **Venue:** eNeuro 10(8)
- **DOI:** 10.1523/ENEURO.0204-23.2023  (PMID 37463742; PMC10414551)
- **Key finding:** Using Flp×Cre intersectional dual-color reporter mice, the authors gain experimental genetic
  access to combinatorially defined SOM interneuron subsets and link classic morphological/electrophysiological/
  neurochemical subtypes to the recently described ~13 morpho-electric-transcriptomic (MET) types, correlating
  genetic label, layer-1 axonal target, and marker-protein expression in the same neurons.

## 2. Cortical somatostatin long-range projection neurons and interneurons exhibit divergent developmental trajectories
- **First author:** Fisher J (… Marín O, Mi D, Lim L)
- **Year:** 2024 (epub 2023 Dec 11)
- **Venue:** Neuron 112(4):558–573.e8
- **DOI:** 10.1016/j.neuron.2023.11.013  (PMID 38086373; PMC7618239)
- **Key finding:** Combining scRNA-seq and spatial transcriptomics, SST+ cells segregate during embryonic stages
  into long-range projection (LRP) neurons and two interneuron classes (Martinotti and non-Martinotti), each
  following distinct developmental trajectories — implying cell-type diversification timing differs across SST+
  subtypes and is especially divergent between LRP neurons and interneurons.
```

---

## Summary
I found and verified two peer-reviewed papers on Sst (somatostatin) interneuron classification in mouse cortex: Hostetler, Hu & Agmon (eNeuro, 2023), which uses intersectional genetics to map SOM subtypes onto morpho-electric-transcriptomic types, and Fisher et al. (Neuron, 2024), which shows SST+ long-range projection neurons vs. interneurons follow divergent developmental trajectories. All metadata (authors, venue, DOI) was confirmed against live NCBI records.

## What I did
Searched PubMed (`mcp__web__pubmed_search`) to surface candidates, then pulled authoritative author/venue/DOI fields from NCBI eSummary via `mcp__web__web_fetch`. Recorded the new eNeuro reference in lab notes. Provided the full `/work/summary.md` contents above.

## Caveats / next steps
In search-lit mode there is no sandbox/file tool, so I could not physically write `/work/summary.md` — please save the fenced block above (the harness adds its own header). Semantic Scholar was rate-limited (HTTP 429), so I confirmed DOIs via NCBI instead. Many more 2023–24 Sst-classification papers exist (e.g., Agmon & Barth 2024 review); I returned two strong, distinct ones per the request.
