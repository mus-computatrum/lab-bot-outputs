# Lab Claude Bot — Outputs

Code, figures, notebooks, tables, and summaries produced by the lab Discord +
Claude bot. Each `/code` (and `/research`, `/figure`) request lands in its own
folder under [`runs/`](runs/) with a per-run README describing the request, the
datasets used, and what was produced.

> The lab datasets themselves are **not** pushed here. They live read-only on
> the always-on lab Mac at `/Users/Shared/lab-data/<id>` and are mounted into
> the sandbox at `/data/<id>`. See the dataset registry for the catalog.

## Latest run

**[`2026-06-05_120205_c22aeee6cf41`](runs/2026-06-05_120205_c22aeee6cf41/)** — research — 2026-06-05 12:02:05 UTC — [bench:research-easy-tasic-celltype-counts] Count cells per cell type (use the 'cluster' …


## Recent runs
| When (UTC) | Folder | Mode | Request |
|---|---|---|---|
| 2026-06-05 12:02:05 | [`2026-06-05_120205_c22aeee6cf41`](runs/2026-06-05_120205_c22aeee6cf41/) | research | [bench:research-easy-tasic-celltype-counts] Count cells per cell type (use the 'cluster' … |
| 2026-06-05 03:56:42 | [`2026-06-05_035642_873a40e0aebb`](runs/2026-06-05_035642_873a40e0aebb/) | research | [bench:research-wide-subagent-marker-fanout] Find robust marker genes for FOUR Sst sub-cl… |
| 2026-06-05 03:29:58 | [`2026-06-05_032958_88c8356f6438`](runs/2026-06-05_032958_88c8356f6438/) | research | [bench:research-easy-tasic-celltype-counts] Count cells per cell type (use the 'cluster' … |
| 2026-06-05 03:28:03 | [`2026-06-05_032803_606f45476928`](runs/2026-06-05_032803_606f45476928/) | research | [bench:research-easy-tasic-celltype-counts] Count cells per cell type (use the 'cluster' … |
| 2026-06-05 03:15:26 | [`2026-06-05_031526_d977a287c62e`](runs/2026-06-05_031526_d977a287c62e/) | research | [bench:research-easy-tasic-celltype-counts] Count cells per cell type (use the 'cluster' … |
| 2026-06-05 03:13:51 | [`2026-06-05_031351_28f75704fbaa`](runs/2026-06-05_031351_28f75704fbaa/) | research | [bench:research-easy-tasic-celltype-counts] Count cells per cell type (use the 'cluster' … |
| 2026-06-04 15:33:41 | [`2026-06-04_153341_1b2b6f1ef98a`](runs/2026-06-04_153341_1b2b6f1ef98a/) | research | [bench:research-yao-isocortex-sst-supertypes] Using Yao 2023 WMB-10X (Isocortex subset) a… |
| 2026-06-04 14:58:19 | [`2026-06-04_145819_9141f09a2aa9`](runs/2026-06-04_145819_9141f09a2aa9/) | research | [bench:research-yao-isocortex-sst-supertypes] Using Yao 2023 WMB-10X (Isocortex subset) a… |
| 2026-06-04 14:33:56 | [`2026-06-04_143356_baf0fd8091d4`](runs/2026-06-04_143356_baf0fd8091d4/) | research | [bench:research-vizgen-spatial-marker-genes] Using Vizgen MERFISH Slice 3 Replicate 1 at … |
| 2026-06-04 14:23:47 | [`2026-06-04_142347_a202b9843468`](runs/2026-06-04_142347_a202b9843468/) | research | [bench:research-vizgen-spatial-marker-genes] Using Vizgen MERFISH Slice 3 Replicate 1 at … |
| 2026-06-04 05:02:22 | [`2026-06-04_050222_fe5aaa25b470`](runs/2026-06-04_050222_fe5aaa25b470/) | research | [bench:research-microns-coreg-functional-em] Using the MICrONS functional NWB at /data/mi… |
| 2026-06-04 04:59:05 | [`2026-06-04_045905_a537f0f3fe15`](runs/2026-06-04_045905_a537f0f3fe15/) | research | [bench:research-abo-v1-sst-osi] Using the Allen Brain Observatory (Visual Coding 2P) cach… |
| 2026-06-04 04:52:35 | [`2026-06-04_045235_1ce83531a693`](runs/2026-06-04_045235_1ce83531a693/) | research | [bench:research-yao-isocortex-sst-supertypes] Using Yao 2023 WMB-10X (Isocortex subset) a… |
| 2026-06-04 04:52:12 | [`2026-06-04_045212_79a2487bf55e`](runs/2026-06-04_045212_79a2487bf55e/) | research | [bench:research-v1dd-connectivity-top-cells] Using the v1dd connectivity extension at /da… |
| 2026-06-04 04:22:24 | [`2026-06-04_042224_c353d49346cf`](runs/2026-06-04_042224_c353d49346cf/) | research | [bench:research-gouwens-patchseq-sst-mtype-mapping] Using the Gouwens 2020 Patch-Seq data… |
| 2026-06-04 04:19:32 | [`2026-06-04_041932_60ec242e0ff5`](runs/2026-06-04_041932_60ec242e0ff5/) | research | [bench:research-bugeon-state-modulation] Using the Bugeon 2022 dataset at /data/bugeon202… |
| 2026-06-03 18:05:21 | [`2026-06-03_180521_843bfb5e610e`](runs/2026-06-03_180521_843bfb5e610e/) | search-lit | [bench:searchlit-easy-sst-v1-papers] Find 3-5 papers from 2023 or later on SST (somatosta… |
| 2026-06-03 17:56:10 | [`2026-06-03_175610_8d5613d02d08`](runs/2026-06-03_175610_8d5613d02d08/) | research | [bench:research-marmoset-mouse-chrm-comparison] Using tasic2018-v1 (mouse V1) and marmose… |
| 2026-06-03 17:52:30 | [`2026-06-03_175230_7cc5bc8549f4`](runs/2026-06-03_175230_7cc5bc8549f4/) | download | [bench:download-marmoset-atlas] Find and register a marmoset cortical cell-type single-ce… |
| 2026-06-03 17:51:55 | [`2026-06-03_175155_51374c5ec197`](runs/2026-06-03_175155_51374c5ec197/) | search-lit | [bench:searchlit-hard-crossspecies-neuromod-sst] Synthesize what's currently known about … |
| 2026-06-03 17:45:59 | [`2026-06-03_174559_5070c8befa36`](runs/2026-06-03_174559_5070c8befa36/) | research | [bench:research-hard-sst-v1-vs-alm-markers] Using the Tasic 2018 dataset (both V1/VISp an… |
| 2026-06-03 17:43:55 | [`2026-06-03_174355_0daf4873aebf`](runs/2026-06-03_174355_0daf4873aebf/) | search-lit | [bench:searchlit-easy-sst-v1-papers] Find 3-5 papers from 2023 or later on SST (somatosta… |
| 2026-06-03 17:41:04 | [`2026-06-03_174104_4646c920eb94`](runs/2026-06-03_174104_4646c920eb94/) | research | [bench:research-easy-tasic-celltype-counts] Count cells per cell type (use the 'cluster' … |
| 2026-06-02 15:12:20 | [`2026-06-02_151220_34d52be273e7`](runs/2026-06-02_151220_34d52be273e7/) | code | [recovered] Zhuang whole-brain spatial-gradient analysis (May 29). Original /code job hit… |
| 2026-05-29 11:54:31 | [`2026-05-29_115431_3d55d7fdae1f`](runs/2026-05-29_115431_3d55d7fdae1f/) | code | Visualize the proportions of different cell-types in VISp vs. ALM using bar plots. |
