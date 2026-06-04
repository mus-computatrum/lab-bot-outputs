import os
os.environ['MPLCONFIGDIR'] = '/work/mplconfig'
os.makedirs('/work/mplconfig', exist_ok=True)

# --- Step 4: Merge and build final DataFrame ---
soma_cols = soma_sub[['pt_root_id', 'soma_x', 'soma_y', 'soma_z']].rename(columns={'pt_root_id': 'pre_pt_root_id'})
result = top10_ids.merge(soma_cols, on='pre_pt_root_id', how='left')
result = result.sort_values('n_outgoing_syn', ascending=False).reset_index(drop=True)
print(result)

# Save CSV
result.to_csv('/work/v1dd_top_axon_proofread.csv', index=False)
print("\nSaved /work/v1dd_top_axon_proofread.csv")
