
# Write markdown notes
notes = """# SST Subtype Marker Expression: VISp vs. ALM — Analysis Notes
## Dataset
- Tasic et al. 2018, `tasic2018_full_counts.h5ad`
- 2,551 SST interneurons total: 1,567 VISp, 984 ALM
- 21 SST clusters present (20 shared between regions, 1 VISp-only: *Sst Tac1 Tacr3*)
- Expression: raw counts → CPM normalisation (target_sum=1e4) → log1p

## Marker availability
All six markers (Calb2, Crh, Hpse, Nos1, Pdyn, Chrna2) were present in the
45,768-gene SMART-seq panel. No missing markers.

## Indistinguishability test
For each marker the max |VISp_mean − ALM_mean| and max |VISp_frac − ALM_frac|
were computed across the 20 clusters shared between regions.
Threshold: max_Δmean < 0.2 **AND** max_Δfrac < 0.05.

| Marker  | max Δmean | avg Δmean | max Δfrac | avg Δfrac | Flag |
|---------|-----------|-----------|-----------|-----------|------|
| Calb2   | 0.708     | 0.108     | 0.379     | 0.084     | DISTINGUISHABLE |
| Crh     | 0.946     | 0.196     | 0.392     | 0.125     | DISTINGUISHABLE |
| Hpse    | 0.217     | 0.031     | 0.246     | 0.077     | DISTINGUISHABLE |
| Nos1    | 0.439     | 0.068     | 0.523     | 0.168     | DISTINGUISHABLE |
| Pdyn    | 1.621     | 0.317     | 0.347     | 0.118     | DISTINGUISHABLE |
| Chrna2  | 0.519     | 0.089     | 0.694     | 0.124     | DISTINGUISHABLE |

**No marker is indistinguishable** by the stated thresholds.

## Qualitative notes on markers that look most similar between regions

### Hpse — most region-stable on average
- avg Δmean = 0.031 (lowest of all six). For most clusters Hpse is near-zero in
  both regions, so the average difference is tiny.
- However, in the two Hpse-named clusters (*Sst Hpse Cbln4*, *Sst Hpse Sema3c*) Hpse
  expression is high in both VISp and ALM (mean 0.97 vs 0.88 and 0.35 vs 0.57
  respectively), so it is a *consistent* marker for those subtypes regardless of region.
- The single largest cluster-level difference is 0.217 (*Sst Hpse Sema3c*, VISp lower
  than ALM), just above the 0.2 threshold.

### Calb2 — broadly expressed but patterned
- Expressed in ~every cluster, avg Δmean = 0.108, but *Sst Calb2 Pdlim5* shows
  a notable ALM > VISp shift (2.29 vs 1.83 mean log-CPM).

## Strongest region differences
- **Pdyn** shows the largest overall spread (max Δmean = 1.621 in *Sst Tac2 Myh4*:
  VISp = 2.735, ALM = 1.114). Pdyn is broadly higher in VISp SST subtypes.
- **Crh** is elevated in *Sst Crh 4930553C11Rik* and ALM is substantially higher than
  VISp in that cluster (max Δmean = 0.946).
- **Chrna2** shows the largest fraction-expressing difference (max Δfrac = 0.694 in
  *Sst Chrna2 Glra3*): VISp frac = 0.88, ALM frac = 0.19.

## Cluster asymmetry
- 1 VISp-only cluster: *Sst Tac1 Tacr3* (48 VISp cells, 0 ALM). Shown as an
  open circle in the ALM panel of the dot plot.
- 0 ALM-only clusters.
"""

with open('/work/sst_subtype_markers_notes.md', 'w') as f:
    f.write(notes)
print("Saved /work/sst_subtype_markers_notes.md")
