
# Save skeleton pair results
dd_df.to_csv('/work/skeleton_pairs_dendrodendritic.csv', index=False)

# Highlight key candidates: close dendrites (<5 µm) + 0 chemical synapses
candidates_dd = dd_df[(dd_df['dendrite_dendrite_dist_um'] < 5.0) & (dd_df['syn_total'] == 0)]
print("Gap junction structural candidates (dendrite-dendrite < 5µm, 0 chemical synapses):")
print(candidates_dd[['root_id_a','root_id_b','soma_dist_um','dendrite_dendrite_dist_um','syn_total']].to_string(index=False))

print("\nPairs with bilateral chemical synapses AND close dendrites (<5µm):")
bilat = dd_df[(dd_df['syn_a2b'] > 0) & (dd_df['syn_b2a'] > 0) & (dd_df['dendrite_dendrite_dist_um'] < 5.0)]
print(bilat[['root_id_a','root_id_b','soma_dist_um','dendrite_dendrite_dist_um','syn_a2b','syn_b2a']].to_string(index=False))
