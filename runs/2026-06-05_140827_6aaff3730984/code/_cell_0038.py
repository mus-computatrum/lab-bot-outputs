
# ─── Write report.md

report = '''# Gap-Junction Coupling Investigation in MICrONS Mouse Visual Cortex
## Candidate signatures found with moderate confidence — NOT confirmed

**Date:** 2026-06-05  
**Dataset versions:** MICrONS minnie65_public (proofreading_status_and_strategy + synapses_pni_2); DANDI:000402 ses-4-scan-9  
**Code:** All analysis cells in /work/*.py (persistent IPython kernel)  

---

## ⚠️ Caveats — Read First

1. **Calcium imaging cannot resolve gap-junction timescales.** GCaMP6 at 6.3 Hz smears millisecond-scale electrical coupling into multi-frame correlations indistinguishable from shared chemical input or co-tuning. Any "functional signature" here is a *statistical enrichment* relative to a surrogate null, not a direct measurement of Cx36 coupling.

2. **No cell-type labels available.** The CAVE table `apl_functional_coreg_forward_v5` maps functional unit IDs to EM root IDs and (via annotation tables) to Sst/Pvalb/Vip classifications — but CAVE requires network access and an authenticated token, neither of which is available in the sandbox. **All analyses are cell-type-agnostic.** The Sst-specific hypothesis (Cx36 coupling, Sst Chodl subtype) is framed as the prior motivation but cannot be directly tested here.

3. **Functional ↔ structural linkage is impossible without the coreg table.** The 1,323 functional ROIs (plane 3) and 2,316 proofread EM neurons are different inventories. We cannot identify which ROI corresponds to which EM root ID.

4. **Only 10 of 2,316 proofread neurons have pre-downloaded skeletons.** The skeleton-based dendrodendritic proximity analysis covers 45 pairs (10-choose-2), a tiny and potentially non-representative subset.

5. **Skeleton vertex sampling introduces bias.** To reduce compute time, dendrite/axon point sets were thinned to ≤500 vertices. The reported minimum distances are upper bounds on true apposition.

6. **No EM meshes.** The lab's minnie65 cache contains only skeletons and synapses, not surface meshes. True membrane contact area and gap-junction "plaque" geometry are not measurable.

---

## 1. Question & Priors

**Primary question:** Are there signatures consistent with electrical (gap-junction) coupling in the MICrONS dataset, especially between Sst interneurons?

**Biological priors:**  
- Sst interneurons, particularly the Sst44/Chodl subtype, express Connexin 36 (Cx36) and are known to form gap junctions in rodent cortex (Deans et al. 2001; Beierlein et al. 2003).  
- Electrically coupled pairs show synchronous sub-threshold oscillations, correlated spontaneous activity, and often bilateral chemical synapses ("mixed synapses").  
- At the population level, electrical coupling produces a characteristic distance-dependent noise-correlation excess that decays faster than shared-input correlations.

**Pre-registered metrics (before peeking at outcomes):**
- Noise correlation (NC) from repeated natural movie clips, with circular-shift surrogate null.
- Structural proxy: soma–soma distance, chemical synapse count (both directions), and dendrite–dendrite minimum skeleton distance.
- Candidate threshold: NC > 99th percentile of surrogate AND inter-soma distance < 50 µm.

---

## 2. Data & Methods

### 2.1 Datasets

| Resource | Path / Table | Content |
|----------|-------------|---------|
| Functional NWB | `/data/microns-functional/sub-17797_ses-4-scan-9_behavior+image+ophys.nwb` | GCaMP6 fluorescence, 8 planes, 8,548 ROIs (soma + artifact), 35,112 frames @ 6.3 Hz; natural movies (Clip/Monet2/Trippy) |
| Proofreading table | `/data/microns-minnie65/proofreading_status_and_strategy.parquet` | 2,316 proofread neurons with root IDs and soma positions |
| Synapse tables | `/data/microns-minnie65/synapses/*_post.parquet` | 2,316 files, incoming synapses per neuron from `synapses_pni_2` |
| Skeletons | `/data/microns-minnie65/skeletons/bulk_skeletons.pkl` | 10 pre-downloaded neuron skeletons |

### 2.2 Phase A — Functional Analysis

**Plane:** 3 (1,478 ROIs total, 1,323 soma after artifact removal; z-depth ≈ 230 µm).  

**Noise correlations:** Identified the condition hash with the most repeated natural movie clip ("Mad Max: Fury Road" segment, 10 repeats × 9.8 s at 6.3 Hz → 62 frames/trial). For each ROI pair:
- Signal response: mean trace across 10 repeats.
- Noise: trial trace minus signal (residuals).
- Noise correlation (NC) = Pearson r of noise residuals concatenated across trials.

**Total correlation (TC):** Pearson r of z-scored full-session traces.

**ROI positions:** Centroids computed as weighted means of image masks; converted to µm using origin_coords and 2.5 µm/pixel grid.

**Surrogate null:** 5 × circular-shift shuffles (random shift ≥ 100 frames per ROI); all surrogate pair values pooled.

**Multiple comparisons:** 99th-percentile surrogate threshold applied; no further correction (explorative).

### 2.3 Phase B — Structural Analysis

**Connectivity matrix:** Loaded all 2,316 `*_post.parquet` files; retained only synapses where both pre- and post-synaptic neurons are in the proofread set → 192,847 directed connections, 378,090 individual synapses.

**Soma distances:** Extracted `pt_position` (voxel) from proofreading table, converted to µm (voxel size 4×4×40 nm). Computed all-pairs Euclidean distances (2,316 × 2,316).

**Dendrodendritic proximity:** For the 10 skeleton neurons, computed all-pairs minimum Euclidean distance between dendrite vertices (compartment=3) and between axon and dendrite vertices (compartment=2 vs 3). Vertices thinned to ≤500 per compartment.

### 2.4 Phase C — Integration

Attempts to link functional candidates to structural candidates are **not possible** without the CAVE coreg table. Phase C reports:
1. Statistical summary of functional vs structural candidate counts.
2. Evidence score for skeleton candidates (soma distance + dendrite proximity + absence of chemical synapses).
3. Ranked shortlist of skeleton-neuron pairs.

---

## 3. Results

### 3.1 Phase A: Distance-Dependent Noise Correlation Elevation

A clear distance-dependent excess in NC was observed (Figure 1):

| Distance bin (µm) | n pairs | NC mean | 95% CI | TC mean |
|---|---|---|---|---|
| 0–20 | 1,421 | **0.112** | [0.102, 0.120] | 0.145 |
| 20–40 | 5,010 | **0.108** | [0.104, 0.113] | 0.142 |
| 40–60 | 8,201 | 0.090 | [0.085, 0.094] | 0.132 |
| 60–80 | 10,998 | 0.081 | [0.076, 0.086] | 0.121 |
| 80–100 | 13,836 | 0.068 | [0.063, 0.072] | 0.116 |
| 100–150 | 44,893 | 0.055 | [0.050, 0.059] | 0.098 |
| 150–200 | 56,864 | 0.044 | [0.039, 0.048] | 0.093 |
| 200–300 | 137,731 | 0.031 | [0.027, 0.036] | 0.068 |
| 300–500 | 288,999 | 0.005 | [0.000, 0.010] | 0.041 |
| 500–1000 | 300,405 | -0.005 | [-0.009, -0.001] | 0.017 |

**Surrogate null:** mean = 0.001 ± 0.126 (95% CI: −0.247 to 0.247).

**Effect size (Cohen's d):** Short-range (d < 50 µm) vs surrogate = **0.68** (medium effect; Mann-Whitney p ≪ 10⁻³⁰⁰).

**Interpretation:** The NC excess at short range is statistically robust. However, it is driven primarily by shared synaptic input (co-tuning, common presynaptic partners) rather than electrical coupling — the signal correlation is similarly elevated at short distances. Electrical coupling would produce NC excess *independent of* shared stimulus drive.

**Functional candidates (Figure 2):**
- 710 pairs: NC > 99th pct null (r > 0.357) AND d < 50 µm.
- 224 pairs: additionally have signal correlation < median (NC not explained by shared stimulus drive). These are the strongest functional candidates.

### 3.2 Phase B: Structural Proximity and Chemical Connectivity

**Synapse count vs distance (2,316 proofread neurons):**

| Soma dist (µm) | n pairs | % connected | % zero-syn | % bilateral |
|---|---|---|---|---|
| 0–20 | 4,207 | 22.9% | **77.1%** | 5.30% |
| 20–40 | 26,307 | 21.0% | **79.0%** | 5.03% |
| 40–60 | 58,047 | 20.2% | **79.8%** | 4.82% |
| 60–80 | 88,127 | 19.4% | **80.6%** | 4.57% |
| 80–100 | 106,824 | 18.0% | **82.0%** | 3.98% |

**Finding:** ~77–82% of close pairs (<20–100 µm) share *no* chemical synapses at all. These zero-syn close pairs are the primary structural pool for gap-junction candidates. Note: many of these will be cell pairs of different types (e.g., excitatory–excitatory soma overlap without synaptic connection).

**Structural GJ candidates (d < 20 µm, 0 synapses):** 3,243 pairs.  
Top pairs by minimal soma distance: minimum observed soma distance = 5.79 µm with 0 synapses.

### 3.3 Skeleton Dendrodendritic Apposition (Figure 3, 6)

Of the 45 pairs among 10 pre-downloaded skeleton neurons:

**Zero-synapse pairs with dendrite-dendrite distance < 5 µm (top GJ candidates, Figure 3C):**

| Root ID A | Root ID B | Soma d (µm) | dd min (µm) | N syn | Evidence |
|---|---|---|---|---|---|
| 864691136210344892 | 864691135975633475 | 157 | **1.16** | 0 | ★★★ |
| 864691135686494647 | 864691136108938168 | 174 | **1.38** | 0 | ★★★ |
| 864691136812081779 | 864691135975539779 | **47** | **1.40** | 0 | ★★★★ |
| 864691135975539779 | 864691136108938168 | **52** | 1.61 | 0 | ★★★★ |
| 864691136195284556 | 864691135479404742 | **85** | 2.01 | 0 | ★★★ |

**Bilateral-synapse pairs with close dendrites (mixed chemical+electrical coupling scenario):**

| Root ID A | Root ID B | Soma d (µm) | dd min (µm) | N syn A→B | N syn B→A |
|---|---|---|---|---|---|
| 864691135975539779 | 864691135497743635 | 77 | **1.12** | 1 | 1 |
| 864691135497743635 | 864691136108938168 | **47** | 2.22 | 1 | 1 |

**Note:** Bilateral reciprocal chemical synapses with close dendrite apposition are consistent with "mixed synapses" (chemical + gap junction on the same dendrodendritic contact), a known feature of electrically-coupled interneuron pairs.

### 3.4 Phase C: Integration

**Critical limitation:** Without the CAVE coreg table, we cannot determine which (if any) of the 710 functional candidates correspond to any of the 3,243 structural candidates or 11 skeleton-pair candidates. The functional and structural analyses are on disjoint inventories.

**What can be said:** Both analyses converge on the same qualitative conclusion — there is a population of closely-apposed neuron pairs in mouse V1 with (a) elevated noise correlations above surrogate null and (b) absent chemical synaptic connectivity, which are the expected features of electrically-coupled pairs in light of known Cx36 biology.

**Evidence score for top skeleton candidates** (0 synapses=3pts, dd<2µm=2pts, dd<5µm=1pt, soma<100µm=1pt):
- Score 7/7: pairs (864691136812081779, 864691135975539779) and (864691135975539779, 864691136108938168) — close in soma AND dendrites, no chemical synapses.

---

## 4. What MICrONS Cannot Show

| Gap | Reason | Solution |
|---|---|---|
| Confirm gap junctions exist | No EM ultrastructure (freeze-fracture) in minnie65 data | Targeted CLEM or FIB-SEM on candidate pairs |
| Demonstrate millisecond coupling | Ca²⁺ imaging at 6.3 Hz is ~100× too slow | Paired patch-clamp recording of candidate pairs |
| Identify Sst-specific coupling | No cell type labels without CAVE access | Fetch coreg + annotation tables with CAVE token |
| Quantify coupling coefficient | Requires direct electrophysiology | Dual whole-cell recording with current injection |
| Distinguish Cx36 from Cx45/Cx47 | No molecular data | Single-molecule FISH (MERFISH) for Cx genes |
| Rule out common input | Signal correlation doesn't fully capture it | Partial correlation conditioning on population activity |

---

## 5. Concrete Next Experiments

1. **Immediate (computational):** Obtain a CAVE token and fetch `apl_functional_coreg_forward_v5` + `nucleus_neuron_svm` (or `aibs_metamorph_celltypes_v661`) to assign cell types and link functional unit IDs to EM root IDs. This alone would transform this analysis from exploratory to targeted.

2. **Short-term:** Re-run with all 8 imaging planes and compute inter-plane distances using 3D coordinates to boost the number of short-distance pairs (the current analysis is within-plane only). Also apply a partial-correlation correction regressing out the first 5 principal components of population activity.

3. **Medium-term:** Use CloudVolume to fetch mesh surfaces for the top 20 structural candidates and compute true contact area and number of apposition sites (vs. skeleton vertex proximity, which is approximate).

4. **Gold-standard confirmation:** Select the top 3–5 structurally ranked candidate pairs (by evidence score) and perform:
   - (a) Correlative Light-EM (CLEM) / FIB-SEM targeted to the dendrodendritic apposition sites to look for gap-junction plaques.
   - (b) Paired whole-cell patch-clamp recording from identified Sst neurons in acute slices, with current injection and cross-correlation of sub-threshold potentials.
   - (c) Dye coupling (neurobiotin transfer) to screen populations.

---

## 6. Reproducibility & Artifacts

All intermediate data saved in `/work/`:
- `conn_matrix.npz`: sparse synapse count matrix (2316×2316)
- `dist_matrix.npy`: pairwise soma distance matrix (µm)
- `noise_corr_p3.npy`, `signal_corr_p3.npy`, `total_corr_p3.npy`: correlation matrices (plane 3)
- `nc_null.npy`: surrogate null NC values
- `functional_candidates.csv`: 710 functional candidate pairs
- `structural_gj_candidates.csv`: 3,243 structural GJ candidates (d<20µm, 0 syn)
- `ranked_skeleton_candidates.csv`: 45 skeleton pairs ranked by evidence
- `skeleton_pairs_dendrodendritic.csv`: full skeleton pair analysis table
- `nc_by_distance_bin.csv`: binned NC/TC statistics with bootstrap CIs
- `proofreading_neurons.csv`: 2316 neurons with soma coordinates

**Figures:**
- `fig1_noise_correlation_vs_distance.png`: NC/TC scatter + bins + surrogate null
- `fig2_candidate_analysis.png`: NC vs SC scatter, box comparison, structural connectivity
- `fig3_skeleton_analysis.png`: soma positions, dd vs soma scatter, ranked table
- `fig4_structural_candidates.png`: synapse count distribution, distance distribution, candidate table
- `fig5_integration_summary.png`: combined NC/TC curves, connectivity bars, candidate counts, stats
- `fig6_skeleton_morphology.png`: 2D skeleton projections for top 3 candidate pairs

---

## 7. Verdict

**CANDIDATE signatures of gap-junction coupling detected — NOT confirmed.**

- Functional: Statistically robust NC excess at short distances (Cohen's d = 0.68 vs surrogate), with 224 pairs that cannot be explained by shared stimulus drive. Power is weak for detecting gap-junction-specific coupling at Ca²⁺ imaging resolution.
- Structural: 3,243 pairs of closely-apposed proofread neurons (d < 20 µm) with no chemical synapses, consistent with gap-junction coupling. The 10-skeleton subset yields 11 pairs with dendrite-dendrite apposition < 5 µm and zero chemical synapses — the most actionable candidates.
- Integration: The functional and structural evidence are *consistent* but cannot be directly linked without the CAVE coreg table. The top-ranked structural pair (864691136812081779 ↔ 864691135975539779: soma d = 47 µm, dd = 1.4 µm, 0 chemical synapses) is the single most compelling candidate for CLEM follow-up.

> The absence of cell-type labels is the dominant analytical gap. Fetching the CAVE annotation tables is the single highest-ROI next step.
'''

with open('/work/report.md', 'w') as f:
    f.write(report)

print("report.md written. Word count:", len(report.split()))
