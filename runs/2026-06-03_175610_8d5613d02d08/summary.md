# research-marmoset-mouse-chrm-comparison

**Mode**: research  ·  **Effort**: deep

## Request

> Using tasic2018-v1 (mouse V1) and marmoset-cortical-atlas (which was registered earlier in this run), compare expression of acetylcholine receptor genes (Chrm1, Chrm2, Chrm3, Chrm4, Chrna2, Chrna4, Chrna5, Chrna7) in SST interneurons between mouse and marmoset. Account for orthologue naming differences (query the marmoset dataset's var/feature column for equivalents if symbols differ). Produce: /work/chrm_mouse_marmoset.csv (mean expression per receptor × species, SST cells only), and /work/chrm_dotplot.png. Note any caveats about subtype labeling differences.

## Final summary

All outputs validated. Here's the full picture:

---

## Summary
In SST interneurons, **CHRM3** (muscarinic M3) is the dominant and broadly conserved acetylcholine receptor in both mouse V1 (~91% of cells expressing) and marmoset MTG (~98%). In contrast, **CHRM1** (56% mouse → 5% marmoset) and the nicotinic subunits **CHRNA4** (63% → 3%), **CHRNA2** (19% → 0.4%), and **CHRNA7** (18% → 1%) all show dramatic apparent divergence. CHRM2 is similarly expressed (~25%) in both species. CHRM4 is absent from the marmoset gene panel.

## What I did
- Loaded mouse V1 SST cells (Tasic 2018, n=1,567) and marmoset MTG SST cells (Jorstad 2023, n=3,474; includes Sst + Sst Chodl)
- Discovered the marmoset `.X` stores **raw integer counts** (not pre-normalized as previously noted — corrected lab memo); normalized both datasets to log1p(CPM10k) for comparison
- Found all 8 mouse genes present; **CHRM4 absent from the 12,897-gene marmoset panel** (not just lowly expressed)
- Saved: `/work/chrm_mouse_marmoset.csv` (16 rows × 7 cols, mean expression + % expressing per gene × species)
- Saved: `/work/chrm_dotplot.png` — dot size = % expressing, color intensity = mean log1p expression; grey × marks CHRM4 as absent from marmoset panel

## Caveats / next steps
- **Confound: brain region ≠ species** — mouse V1 vs marmoset MTG; apparent divergence in CHRM1/CHRNA4 could partly reflect region differences rather than (or in addition to) species differences
- **Platform bias**: SMART-seq2 (full-length, ~200 counts/cell) vs 10x 3′ v3 (~7,600 counts/cell) — 10x has lower sensitivity per gene, which could artificially suppress detection of lowly-expressed nicotinic subunits in marmoset
- **Subtype composition**: Mouse SST is 21 clusters all from VISp; marmoset SST subtype diversity within MTG may differ substantially. The "Sst Chodl" subset (81 cells) was included in marmoset — consider analyzing separately
- **CHRM4 absence** in marmoset panel is a data gap, not a biological claim about expression
- To disambiguate species vs. region, a mouse ALM × marmoset prefrontal comparison would help
