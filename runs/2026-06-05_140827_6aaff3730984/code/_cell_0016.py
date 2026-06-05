
# Step 4: Analyze synapse count vs distance and identify gap-junction structural candidates

# Build a DataFrame of all unique ordered pairs (i,j), i<j
import pandas as pd

triu_i, triu_j = np.triu_indices(N, k=1)  # upper triangle, ~2.68M pairs

# Sample these for analysis (all 2.68M pairs is large but manageable for a pandas DF)
print(f"Total upper-triangle pairs: {len(triu_i):,}")

# Soma distance for each pair
pair_dist = dist_matrix[triu_i, triu_j]

# Synapse count: consider BOTH directions (pre→post + post→pre)
# conn_matrix[post, pre] → symmetric sum
conn_dense = conn_matrix.toarray()
syn_ij = conn_dense[triu_i, triu_j]   # i→j direction (i=post, j=pre? No...)
# conn_matrix[post, pre] so conn_dense[i,j] = synapses from j→i
# conn_dense[j,i] = synapses from i→j
# Total both directions:
syn_fwd = conn_dense[triu_i, triu_j]  # synapses j→i
syn_rev = conn_dense[triu_j, triu_i]  # synapses i→j
syn_both = syn_fwd + syn_rev

print(f"\nPairs with ≥1 synapse in either direction: {(syn_both>0).sum():,} ({(syn_both>0).mean()*100:.2f}%)")
print(f"Pairs with 0 synapses (both ways):          {(syn_both==0).sum():,}")

# Build compact DataFrame for close pairs only (<100 µm)
close_mask = pair_dist < 100.0
close_pairs_df = pd.DataFrame({
    'idx_a': triu_i[close_mask],
    'idx_b': triu_j[close_mask],
    'dist_um': pair_dist[close_mask],
    'syn_ab': conn_dense[triu_j, triu_i][close_mask],  # a→b
    'syn_ba': conn_dense[triu_i, triu_j][close_mask],  # b→a
    'syn_total': syn_both[close_mask],
    'root_id_a': [root_ids[i] for i in triu_i[close_mask]],
    'root_id_b': [root_ids[j] for j in triu_j[close_mask]],
})

print(f"\nClose pairs (d < 100 µm): {len(close_pairs_df):,}")
print(f"  With 0 synapses (gap-jn candidates): {(close_pairs_df['syn_total']==0).sum():,}")
print(f"  With ≥1 synapse: {(close_pairs_df['syn_total']>0).sum():,}")
print(f"\nDistance bins for 0-synapse pairs:")
zero_syn = close_pairs_df[close_pairs_df['syn_total'] == 0]
for dmax in [20, 30, 40, 50, 75, 100]:
    n = (zero_syn['dist_um'] < dmax).sum()
    print(f"  d < {dmax:3d} µm: {n:,} zero-synapse pairs")
