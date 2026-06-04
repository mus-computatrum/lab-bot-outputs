# --- Step 3: Extract soma positions for the top 10 cells ---
top10_ids = out_counts.head(10).reset_index()

# Soma positions: pt_position is stored as a list [x, y, z]
soma_sub = soma[soma['pt_root_id'].isin(top10_ids['pre_pt_root_id'])].copy()
print(f"Soma matches for top 10: {len(soma_sub)}")
print(soma_sub[['pt_root_id', 'pt_position']].head())

# Extract x, y, z from the pt_position list column
soma_sub['soma_x'] = soma_sub['pt_position'].apply(lambda v: v[0])
soma_sub['soma_y'] = soma_sub['pt_position'].apply(lambda v: v[1])
soma_sub['soma_z'] = soma_sub['pt_position'].apply(lambda v: v[2])
print(soma_sub[['pt_root_id', 'soma_x', 'soma_y', 'soma_z']])
