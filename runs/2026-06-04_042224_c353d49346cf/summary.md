# research-gouwens-patchseq-sst-mtype-mapping

**Mode**: research  ·  **Effort**: standard

## Request

> Using the Gouwens 2020 Patch-Seq dataset at /data/gouwens2020-patchseq/transcriptome/, load the v2 count matrix + metadata, restrict to Sst-class cells (metadata 'corresponding_AIT2.3.1_alias' starts with 'Sst' or subclass_label == 'Sst'), and for each Sst t-type produce the cell count + top 3 marker genes (by mean log1p expression). Save as /work/gouwens_sst_ttypes.csv (columns: ttype, n_cells, marker1, marker2, marker3).

## Final summary

Done. Here's the final report:

---

## Summary
Loaded the Gouwens 2020 Patch-Seq v2 count matrix (45,768 genes × 4,435 cells), filtered to 1,824 SST interneurons across 21 t-types (using `corresponding_AIT2.3.1_alias` starts-with "Sst"), computed log1p of raw counts, and ranked genes by mean log1p expression per t-type. Results saved to `/work/gouwens_sst_ttypes.csv` with 21 rows × 5 columns.

## What I did
- Loaded metadata CSV → filtered 1,824 SST cells across 21 t-types (e.g. "Sst Chodl" n=132, "Sst Calb2 Pdlim5" n=266, "Sst Chrna2 Ptgdr" n=10)
- Fixed a `pandas` `usecols`+`index_col` interaction bug (callable usecols silently misassigned the index column; fixed via explicit integer position list)
- Loaded only SST cell columns from the 425 MB CSV → log1p-transformed → computed per-t-type mean expression across 45,768 genes
- Identified top 3 genes by mean log1p per t-type; saved `/work/gouwens_sst_ttypes.csv`

## Caveats / next steps
- **"Top by mean expression" ≠ discriminative markers**: marker1/2 are almost universally *Rn18s-rs5* (rRNA pseudogene) and *Malat1* (lncRNA) — high-expression housekeeping genes on raw counts. marker3 starts to show t-type specificity (e.g. *Npy* for Sst Chodl, *Nrxn3* for Sst Hpse). For true markers, consider CPM normalization + differential expression (Wilcoxon/COSG) against other t-types.
- One SST cell (`PS0817_E1-50_S19`) was present in the count matrix but absent from the original metadata load due to the earlier usecols bug; it is correctly included in the final analysis.
- No `subclass_label` column exists in this metadata; SST filtering was done solely on `corresponding_AIT2.3.1_alias` prefix.
