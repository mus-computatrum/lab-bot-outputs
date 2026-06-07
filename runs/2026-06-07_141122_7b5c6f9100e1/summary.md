# searchlit-internet-recent-sst-papers

**Mode**: search-lit  ·  **Effort**: standard

## Request

> Find 2 peer-reviewed papers published in 2023 or 2024 on Sst (somatostatin) interneuron classification in mouse cortex. For each, report: title, first author, year, venue, DOI, and 1-2 sentences on the key finding. You must use the web/scholarly tools (pubmed_search / arxiv_search / semantic_scholar / web_fetch) — do NOT answer from memory. Save the summary as /work/summary.md (the harness inserts a header automatically; just include your findings).

## Final summary

Both papers and DOIs are confirmed against PubMed records. Note: in search-lit mode there is **no sandbox/file-writing tool** available to me, so I cannot physically write `/work/summary.md`. Below is the exact content intended for that file.

---

**Content for `/work/summary.md`:**

```markdown
# Sst Interneuron Classification in Mouse Cortex — 2 Papers (2023/2024)

## Paper 1
- **Title:** Cortical somatostatin long-range projection neurons and interneurons exhibit divergent developmental trajectories
- **First author:** Josephine Fisher
- **Year:** 2024 (epub Dec 2023)
- **Venue:** Neuron (vol 112, issue 4, pp. 558–573)
- **DOI:** 10.1016/j.neuron.2023.11.013
- **PMID:** 38086373
- **Key finding:** Combining single-cell RNA-seq and spatial transcriptomics, the authors show that SST+ cells segregate during embryogenesis into long-range projection (LRP) neurons and two interneuron classes — Martinotti and non-Martinotti cells — each following a distinct developmental trajectory. Subtype identity is largely established embryonically (with interneuron diversity refined postnatally), and the timing of diversification differs sharply between LRP neurons and interneurons.

## Paper 2
- **Title:** A brief history of somatostatin interneuron taxonomy or: how many somatostatin subtypes are there, really?
- **First author:** Ariel Agmon
- **Year:** 2024
- **Venue:** Frontiers in Neural Circuits
- **DOI:** 10.3389/fncir.2024.1436915
- **PMID:** 39091993
- **Key finding:** A perspective/review tracing pre- and post-transcriptomic SST taxonomy, arguing that the most useful classification level for experimentalists is ~10 "supertypes," which align with traditional morpho-electric-neurochemical types. The authors caution that finer t-types/clusters based on subtle gene-expression differences lack clear phenotypic correlates and may undermine the purpose of cell-type classification.
```

## Summary
I identified and verified two peer-reviewed papers (2023/2024) on Sst interneuron classification in mouse cortex: Fisher et al. 2024 (*Neuron*) on divergent developmental trajectories of SST subtypes, and Agmon & Barth 2024 (*Front. Neural Circuits*) arguing that ~10 "supertypes" is the most useful taxonomic level. Titles, authors, venues, DOIs, and PMIDs were confirmed directly against PubMed records.

## What I did
Searched PubMed for SST-interneuron classification papers, then fetched both PubMed records via WebFetch to verify DOIs (10.1016/j.neuron.2023.11.013; 10.3389/fncir.2024.1436915), first authors, and venues. I drafted the `/work/summary.md` content above.

## Caveats / next steps
In **search-lit mode there is no file-writing/sandbox tool exposed to me**, so I could not actually create `/work/summary.md` — the markdown is reproduced inline for you to paste. Semantic Scholar was rate-limited (429), so verification relied on PubMed + PubMed page fetches, which was sufficient. Both candidates were corroborated by my prior cross-job notes.

Sources:
- [Fisher et al. 2024, Neuron — PMID 38086373](https://pubmed.ncbi.nlm.nih.gov/38086373/)
- [Agmon & Barth 2024, Front Neural Circuits — PMID 39091993](https://pubmed.ncbi.nlm.nih.gov/39091993/)
