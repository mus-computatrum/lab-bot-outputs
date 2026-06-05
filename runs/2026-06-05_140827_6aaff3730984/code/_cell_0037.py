
# ─── Compile the ranked candidate pair table (for report)

# Structural candidates (all evidence)
dd_df_sorted = dd_df.sort_values(['syn_total', 'dendrite_dendrite_dist_um']).copy()
dd_df_sorted['evidence_score'] = (
    (dd_df_sorted['syn_total'] == 0).astype(int) * 3 +
    (dd_df_sorted['dendrite_dendrite_dist_um'] < 2).astype(int) * 2 +
    (dd_df_sorted['dendrite_dendrite_dist_um'] < 5).astype(int) * 1 +
    (dd_df_sorted['soma_dist_um'] < 100).astype(int) * 1
)

print("=== RANKED CANDIDATE PAIRS (SKELETON NEURONS) ===")
print("Ranked by (0 syn first, then dd distance, then soma distance)")
print()
cols_show = ['root_id_a', 'root_id_b', 'soma_dist_um', 'dendrite_dendrite_dist_um', 
             'syn_total', 'syn_a2b', 'syn_b2a', 'evidence_score']
print(dd_df_sorted[cols_show].head(15).to_string(index=False))

# Save full ranked table
dd_df_sorted.to_csv('/work/ranked_skeleton_candidates.csv', index=False)

# Also compute overall stats for the report
print("\n=== KEY STATISTICS FOR REPORT ===")
print(f"Total proofread neurons: {N}")
print(f"Total within-proofread synaptic connections (ordered pairs): {len(pair_stats):,}")
print(f"Synapse count: min={counts.min()}, max={counts.max()}, mean={counts.mean():.2f}")
print(f"\nROIs in plane 3 (soma only): {N_rois}")
print(f"Stimulus repeats used (Mad Max): {n_repeats}")
print(f"Trial duration: {T_trial} frames ({T_trial/FRAME_RATE:.1f} s)")
print(f"\nNC elevation at d<20µm vs surrogate:")
print(f"  Observed: {pair_nc[pair_dist_rois<20].mean():.4f} ± {pair_nc[pair_dist_rois<20].std():.4f}")
print(f"  Surrogate: {nc_null.mean():.4f} ± {nc_null.std():.4f}")
print(f"  Cohen's d = {cohen_d:.3f}")
print(f"\nFunctional candidates (NC>99th pct null, d<50µm): {func_cand_mask.sum()}")
print(f"  Of which low-SC: {pure_noise_mask.sum()}")
print(f"\nStructural GJ candidates (d<20µm, 0 syn): {len(struct_gj_cands):,}")
print(f"Skeleton pairs dd<5µm + 0 syn: {len(candidates_dd)}")
print(f"Skeleton pairs bilateral + dd<5µm: {len(bilat)}")
