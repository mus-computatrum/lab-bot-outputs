# searchlit-internet-recent-sst-papers

**Mode**: search-lit  ·  **Effort**: standard

## Request

> Find 2 peer-reviewed papers published in 2023 or 2024 on Sst (somatostatin) interneuron classification in mouse cortex. For each, report: title, first author, year, venue, DOI, and 1-2 sentences on the key finding. You must use the web/scholarly tools (pubmed_search / arxiv_search / semantic_scholar / web_fetch) — do NOT answer from memory. Save the summary as /work/summary.md (the harness inserts a header automatically; just include your findings).

## Final summary

I have everything I need. I found two excellent peer-reviewed papers. Now let me compile the report. Note that in `search-lit` mode I have no sandbox file-writer, but I'll include the full `/work/summary.md` content and note the limitation.

---

## Summary

Both papers were found via live tool calls (Semantic Scholar + PubMed E-utilities + PMC fetch). Here is the verified literature:

---

### Paper 1
**Title:** Genetically Defined Subtypes of Somatostatin-Containing Cortical Interneurons
**First author:** Rachel E. Hostetler
**Year:** 2023
**Venue:** *eNeuro* 10(8):ENEURO.0204-23.2023
**DOI:** `10.1523/ENEURO.0204-23.2023`
**PMID:** 37463742 (PMC10414551)

**Key finding:** By crossing Flp and Cre driver lines with a dual-color intersectional reporter in adult mouse barrel cortex, Hostetler et al. characterized three genetically distinct Sst interneuron subtypes in deep cortical layers: two layer 1-targeting subtypes with non-overlapping marker protein expression and electrophysiological fingerprints, plus a known layer 4-targeting subtype. Together these three account for >50% of all layer 5 Sst cells and map onto 5 of the 13 morpho-electric transcriptomic (MET) types defined by large-scale sequencing studies, providing genetic handles for previously inaccessible MET types.

---

### Paper 2
**Title:** Transcriptional maintenance of cortical somatostatin interneuron subtype identity during migration
**First author:** Hermany Munguba
**Year:** 2023
**Venue:** *Neuron* 111(22):3590–3603.e5
**DOI:** `10.1016/j.neuron.2023.07.018`
**PMID:** 37625400

**Key finding:** Conditional removal of Sox6 in migrating Sst+ interneurons revealed that Sox6 is required during migration—but not postnatally—to maintain 5 of 8 molecular Sst+ cortical subtypes in mice, without reducing total Sst cell number. The data show that subtype identity is already specified before cortical integration (by E18.5) and that active transcriptional programs during the migratory phase are essential to preserve the full landscape of Sst cortical interneuron subtypes.

---

> ⚠️ **Note on `/work/summary.md`:** This job runs in `search-lit` mode, which has no sandbox (`run_in_sandbox` is not available). I cannot write files to `/work`. The content above constitutes the full summary — please save it manually, or re-run in a mode with sandbox access to write the file automatically.

---

## What I did
1. Called `mcp__web__semantic_scholar` → found Hostetler et al. 2023 (*eNeuro*) and confirmed peer-review status.
2. Fetched `https://pmc.ncbi.nlm.nih.gov/articles/PMC10414551/` → confirmed journal, DOI, PMID, and abstract for Paper 1.
3. Called PubMed E-utilities API (`eutils.ncbi.nlm.nih.gov/esearch`) with date filter 2023–2024 → retrieved 16 matching PMIDs.
4. Called `mcp__web__web_fetch` on efetch for top PMIDs → retrieved full abstracts; selected Munguba et al. 2023 (*Neuron*) as the strongest directly on-topic second paper.

## Caveats / next steps
- PubMed's MCP tool returned no results for multiple queries (apparent service issue); I fell back to the E-utilities HTTP API directly.
- The Yao et al. 2023 *Nature* whole-brain cell atlas (`10.1038/s41586-023-06812-z`) is also highly relevant if you want a dataset-scale reference — it resolves Sst cortical types into hundreds of transcriptomic clusters.
- Fisher et al. 2024 *Neuron* (`10.1016/j.neuron.2023.11.013`) is a strong alternative/addition for Paper 2, focusing on developmental trajectories of Martinotti vs. non-Martinotti Sst subtypes using scRNA-seq + spatial transcriptomics.
- In a future run with sandbox access, `/work/summary.md` can be written automatically.
