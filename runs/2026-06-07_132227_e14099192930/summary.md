# searchlit-internet-recent-sst-papers

**Mode**: search-lit  ·  **Effort**: standard

## Request

> Find 2 peer-reviewed papers published in 2023 or 2024 on Sst (somatostatin) interneuron classification in mouse cortex. For each, report: title, first author, year, venue, DOI, and 1-2 sentences on the key finding. You must use the web/scholarly tools (pubmed_search / arxiv_search / semantic_scholar / web_fetch) — do NOT answer from memory. Save the summary as /work/summary.md (the harness inserts a header automatically; just include your findings).

## Final summary

I now have both papers with full details. Let me compile the findings. Note: in **search-lit mode** there is no sandbox, so I cannot write to `/work/summary.md` directly — I'll provide the exact file content below for the record, and note the limitation.

---

**`/work/summary.md` content** (to be saved manually or by the harness):

```markdown
## SST Interneuron Classification in Mouse Cortex: 2023–2024 Literature

---

### Paper 1

**Title:** Cortical somatostatin long-range projection neurons and interneurons exhibit divergent developmental trajectories
**First author:** J. Fisher
**Year:** 2024 (epub November 2023)
**Venue:** *Neuron*
**DOI:** 10.1016/j.neuron.2023.11.013
**PMID:** 38086373

**Key finding:** Using single-cell RNA sequencing and spatial transcriptomics in mice, SST⁺ cells were found to diverge as early as embryonic development into two broad classes — long-range projection (LRP) neurons and cortical interneurons (Martinotti and non-Martinotti cells) — each following a distinct transcriptomic trajectory. Interneuron subtype diversity is largely established in the embryo but is further refined during early postnatal life.

---

### Paper 2

**Title:** A brief history of somatostatin interneuron taxonomy or: how many somatostatin subtypes are there, really?
**First author:** Ariel Agmon
**Year:** 2024 (published 17 July 2024)
**Venue:** *Frontiers in Neural Circuits*
**DOI:** 10.3389/fncir.2024.1436915
**PMID:** 39091993

**Key finding:** This perspective reviews 10+ years of large-scale transcriptomic efforts and argues that ~10 functional "supertypes" of SST interneurons — corresponding to well-established morphological, electrophysiological, and neurochemical categories — represent the most experimentally actionable classification level. The authors contend that finer t-type subdivisions based on subtle gene expression differences lack clear phenotypic correlates and may hinder rather than advance experimental neuroscience.
```

---

## Summary
I found two peer-reviewed papers from 2023–2024 on SST interneuron classification in mouse cortex. The first (Fisher et al., *Neuron* 2024, DOI: 10.1016/j.neuron.2023.11.013) uses scRNA-seq and spatial transcriptomics to show that SST⁺ cells diverge into long-range projection neurons vs. Martinotti/non-Martinotti interneurons as early as embryonic development. The second (Agmon & Barth, *Frontiers in Neural Circuits* 2024, DOI: 10.3389/fncir.2024.1436915) is a perspective arguing for ~10 "supertypes" as the optimal practical classification level, noting that finer t-types lack clear phenotypic support.

## What I did
- Queried PubMed (`somatostatin interneuron classification mouse cortex 2023 2024`) → retrieved 8 results with abstracts
- Retrieved full Semantic Scholar record for PMID 38086373 to confirm DOI and first author
- Fetched the PubMed landing page for PMID 39091993 to confirm DOI, date, and authors
- Identified 2 high-quality peer-reviewed papers fitting the request criteria
- ⚠️ **`/work/summary.md` could not be written** — this job runs in `search-lit` mode with no sandbox access; file content is provided above verbatim

## Caveats / next steps
- **search-lit mode = no `/work` write access** — the harness or a follow-up sandbox job would need to create the file
- Paper 1 (Fisher et al.) was epub November 2023 but appears as a 2024 Neuron issue; it qualifies as 2023 or 2024 depending on whether epub or print date is used
- Agmon & Barth is a **perspective/opinion piece** (not primary research); if a primary-research-only paper is preferred, PMID 37463742 (Favuzzi et al., *eNeuro* 2023) is a strong alternative covering genetically-defined SST subtypes via intersectional mouse line crosses
