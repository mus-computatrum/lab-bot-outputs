
summary_md = """# MICrONS minnie65_public — CAVE Materialization Table Inventory
*Generated 2026-06-05 via caveclient v8.1.0 against https://global.daf-apis.com*

---

## (a) Total tables

**45 tables** are currently registered in the `minnie65_public` datastack.

All 45 returned HTTP 200 (no errors or 404s encountered — see section c).

Voxel resolution breakdown:
- 42 tables: `4.0 × 4.0 × 40.0 nm` (native MICrONS minnie65 voxel grid)
- 2 tables: `1.0 × 1.0 × 1.0 nm` (`myelin_auto_tags_2points`, `vortex_axon_backtrace_column`, `cell_type_multifeature_combo`)
- 1 table:  `8.0 × 8.0 × 40.0 nm` (`vortex_compartment_targets`)

---

## (b) Top 5 tables for a gap-junction analysis

Gap junctions (GJs) in cortical EM appear as symmetric, very tight membrane appositions
(~2 nm cleft) — quite distinct from the ~20 nm cleft of chemical synapses.
The `synapses_pni_2` automated detection was tuned for *chemical* synapses, so a GJ
analysis requires careful strategy: using cell-type and proofreading tables to define
candidate cell pairs, then inspecting raw EM for GJ-type contacts between them.

### 1. `synapses_pni_2` — schema: `synapse`
The master connectivity table (~337 M synaptic clefts). While optimised for
chemical synapses, GJs may appear as very small, soma/shaft-targeting contacts
with near-zero cleft size. More importantly, this table defines the *full
pre↔post adjacency graph* from which candidate GJ-coupled cell pairs can be
enumerated — any pair with a suspiciously small "synapse" between them is a GJ
candidate worth inspecting in EM. **Essential as the connectivity backbone.**

### 2. `aibs_metamodel_celltypes_v661` — schema: `cell_type_reference`
Whole-dataset cell-type predictions (Elabbady 2022; v661 materialisation).
GJs in mouse V1 are highly cell-type–specific: SST↔SST, PV chandelier↔chandelier,
and astrocyte↔astrocyte coupling are the known dominant motifs. You must label
every node in the adjacency graph by cell type before any GJ specificity analysis.
This is the broadest, most complete annotation available.

### 3. `proofreading_status_and_strategy` — schema: `compartment_proofread_status_strategy`
Merge errors in automated segmentation create phantom connectivity, which would
generate massive false-positive GJ candidates. This table flags which neurons have
had dendrite and/or axon *cleaned* or *extended* manually. Restricting both pre- and
post-synaptic cells to at minimum `status_dendrite=clean` is critical for
soma-targeting GJ contact reliability.

### 4. `gamlin_2023_mcs` + `gamlin_2023_mcs_met_types` — schema: `cell_type_reference` / `reference_tag_float`
Martinotti cells (SST subtype, a.k.a. MCs) are among the most GJ-coupled
interneuron classes in mouse V1. These two companion tables (Gamlin et al. 2023,
Nature) provide EM↔MET-type linkage for MCs: morpho-electric-transcriptomic
classification with cross-validation reliability scores. If your GJ analysis focuses
on SST interneurons, this table gives you the finest subtype resolution available —
crucial for testing whether GJ coupling is MET-type–specific within MCs.

### 5. `nucleus_detection_v0` — schema: `nucleus_detection`
GJs only form between cells whose processes are in physical proximity.
This table provides soma centroid positions (XYZ in voxels) for ~100 k nuclei.
Using soma-to-soma distance as a spatial pre-filter before EM inspection massively
reduces the search space: candidate GJ pairs should have somas within ~150 µm
of each other. Also needed to join cell-type tables (which key on `nucleus_id`)
back to root segment IDs.

### Honourable mention: `synapse_target_predictions_ssa_v2`
Classifies each synapse in `synapses_pni_2` as soma / shaft / spine. GJs overwhelmingly
target soma and proximal shaft, so filtering the adjacency graph to soma/shaft contacts
between same-cell-type pairs is a useful first-pass enrichment step before EM inspection.

---

## (c) 404s and other HTTP errors

**None.** All 45 metadata endpoints returned HTTP 200 with valid JSON payloads.

This implies:
- The token at `/home/sandbox/.cloudvolume/secrets/global.daf-apis.com-cave-secret.json`
  is valid and grants read access to `minnie65_public`.
- The CAVE materialization service at `https://global.daf-apis.com` is fully reachable
  from the sandbox network.
- The materialization version queried is live and all advertised tables have
  corresponding metadata records (no stale catalogue entries).

If 404s appear in future runs they would most likely indicate a table has been
*retired or renamed* (the catalogue updated but the metadata record deleted), or
a version mismatch between the table list endpoint and the metadata endpoint.
"""

with open("/work/cave_summary.md", "w") as f:
    f.write(summary_md)

print("Saved /work/cave_summary.md")
print(f"  Characters: {len(summary_md)}")
