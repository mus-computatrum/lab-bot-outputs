
# C4: More refined structural analysis — separate zero-syn vs. synaptically-connected close pairs
# For structural gap-junction candidates: close soma + 0 synapses

# Among very close pairs (d < 30 µm) with 0 synapses
very_close_zero = close_pairs_df[(close_pairs_df['dist_um'] < 30) & (close_pairs_df['syn_total'] == 0)]
very_close_conn = close_pairs_df[(close_pairs_df['dist_um'] < 30) & (close_pairs_df['syn_total'] > 0)]

print(f"d < 30µm, zero synapse pairs (structural GJ candidates): {len(very_close_zero):,}")
print(f"d < 30µm, connected pairs (chemical synapse control): {len(very_close_conn):,}")
print(f"\nOf zero-syn pairs at <30µm:")
print(f"  Pure isolation (no synapse either way): {(very_close_zero['syn_total'] == 0).all()}")

# Summary table of structural candidates (all pairs < 20µm, zero synapses)
struct_gj_cands = close_pairs_df[(close_pairs_df['dist_um'] < 20) & (close_pairs_df['syn_total'] == 0)]
print(f"\nStructural GJ candidates (soma d<20µm, 0 synapses): {len(struct_gj_cands):,}")
print(f"Top 10 by distance:")
print(struct_gj_cands.sort_values('dist_um').head(10)[['root_id_a','root_id_b','dist_um','syn_total']].to_string(index=False))

# Save full list of structural candidates
struct_gj_cands.sort_values('dist_um').to_csv('/work/structural_gj_candidates.csv', index=False)
