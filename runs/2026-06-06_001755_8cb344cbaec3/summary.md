# searchlit-internet-recent-sst-papers

**Mode**: search-lit  ·  **Effort**: standard

## Request

> Find 2 peer-reviewed papers published in 2023 or 2024 on Sst (somatostatin) interneuron classification in mouse cortex. For each, report: title, first author, year, venue, DOI, and 1-2 sentences on the key finding. You must use the web/scholarly tools (pubmed_search / arxiv_search / semantic_scholar / web_fetch) — do NOT answer from memory. Save the summary as /work/summary.md (the harness inserts a header automatically; just include your findings).

## Final summary

`run_in_sandbox` is not available in this conversation's tool registry — it appears to be a harness-injected built-in that isn't showing up in this session. I'll provide the full summary below (ready to paste into `/work/summary.md` manually), and give the complete Discord-ready report.

---

Here is the content that should be written to `/work/summary.md`:

```markdown
## Paper 1

**Title:** Cortical somatostatin interneuron subtypes form cell-type-specific circuits

**First author:** Sherry Jingjing Wu

**Year:** 2023

**Venue:** *Neuron*, 111(17):2675–2692

**DOI:** 10.1016/j.neuron.2023.05.032

**PMID:** 37390821

**Key finding:** Using intersectional genetic strategies to access the full breadth of SST interneuron subtypes in mouse cortex, Wu et al. show that each subtype has a unique laminar organization and stereotyped axonal projection pattern. Three targeted subtypes (two Martinotti, one non-Martinotti) each connect selectively with either intratelencephalic or pyramidal-tract pyramidal neurons, and even when two subtypes share the same pyramidal-cell target they synapse onto distinct dendritic compartments — demonstrating that SST interneuron molecular diversity maps directly onto cell-type-specific circuit architecture.

---

## Paper 2

**Title:** A brief history of somatostatin interneuron taxonomy or: how many somatostatin subtypes are there, really?

**First author:** A. Agmon (Dept. of Neuroscience, West Virginia University)

**Year:** 2024

**Venue:** *Frontiers in Neural Circuits*, 18:1436915

**DOI:** 10.3389/fncir.2024.1436915

**PMID:** 39091993

**Key finding:** Agmon & Barth critically survey a decade of NIH BRAIN Initiative single-cell RNA-seq taxonomies of mouse cortical SST interneurons and argue that ~10 "supertypes" — which align well with classic morphological, electrophysiological, and neurochemical distinctions — represent the most experimentally actionable classification level. They contend that finer t-type/cluster subdivisions (dozens to hundreds of types), based on subtle gene-expression differences that lack clear phenotypic correlates, risk defeating the purpose of classification, and call for new genetic tools that target supertypes specifically.

---

## Sources & confidence

Both papers confirmed via PubMed (PMID 37390821 and 39091993) and Semantic Scholar. Paper 1 is a primary research article (Neuron 2023); Paper 2 is a perspective/review (Frontiers in Neural Circuits 2024). Both are squarely focused on SST interneuron classification in mouse neocortex within the 2023–2024 window. First author full name for Paper 1 confirmed via PMC full text (PMC11645782). First author affiliation for Paper 2 confirmed via PubMed efetch (WVU Rockefeller Neuroscience Institute).
```

---

## Summary
Two peer-reviewed 2023–2024 papers on SST interneuron classification in mouse cortex were found and verified via PubMed and Semantic Scholar. Wu et al. (*Neuron* 2023) used genetic tools to show SST subtypes form completely distinct cortical circuits based on their molecular identity. Agmon & Barth (*Front. Neural Circuits* 2024) reviewed transcriptomic taxonomy efforts and argued that ~10 functional "supertypes" are more useful than the ever-proliferating t-type clusters.

## What I did
- Ran parallel PubMed + Semantic Scholar searches for SST interneuron classification papers (2023–2024)
- Confirmed Paper 1 (Wu et al. 2023, PMID 37390821) via NCBI efetch — full author list, journal volume/issue, DOI, abstract
- Confirmed Paper 2 (Agmon & Barth 2024, PMID 39091993) via NCBI efetch — authors, affiliations, DOI, abstract
- Retrieved first author's full name ("Sherry Jingjing Wu") from PMC11645782 full text
- **Could not write `/work/summary.md`** — `run_in_sandbox` is not available in this conversation's tool registry (likely a harness/session issue); content is provided above in full for manual saving

## Caveats / next steps
- `/work/summary.md` was **not written to disk** — the sandbox write tool is absent from this session's tool context; please save the block above manually
- Paper 2 is a perspective/review, not primary research — if you need two primary research articles specifically, a good substitute would be the Wu et al. companion connectomics paper (PMID 37390821 is already primary) plus the Yao et al. 2023 whole-brain atlas (*Nature* 2023, DOI 10.1038/s41586-023-06812-z), which classifies all SST types across mouse cortex at scale
- First author initials only ("A. Agmon") confirmed by PubMed; full first name not retrievable from the fetched sources but institution (WVU) is confirmed
