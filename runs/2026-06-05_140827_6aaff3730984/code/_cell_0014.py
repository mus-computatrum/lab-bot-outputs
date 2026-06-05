
# Aggregate synapse data into (pre_idx, post_idx) -> (count, total_size)
from collections import defaultdict

pair_stats = defaultdict(lambda: {'count': 0, 'total_size': 0.0})
for r, c, sz in zip(rows_list, cols_list, data_size):
    pair_stats[(r, c)]['count'] += 1
    pair_stats[(r, c)]['total_size'] += sz

print(f"Unique (pre,post) proofread pairs with ≥1 synapse: {len(pair_stats)}")

# Build sparse count matrix (CSR): conn_matrix[post, pre] = n_synapses
post_idxs = np.array([k[0] for k in pair_stats])
pre_idxs  = np.array([k[1] for k in pair_stats])
counts    = np.array([v['count'] for v in pair_stats.values()])
sizes     = np.array([v['total_size'] for v in pair_stats.values()])

conn_matrix = sp.csr_matrix((counts, (post_idxs, pre_idxs)), shape=(N, N))
size_matrix = sp.csr_matrix((sizes, (post_idxs, pre_idxs)), shape=(N, N))

print(f"Connectivity matrix shape: {conn_matrix.shape}")
print(f"Density: {conn_matrix.nnz / (N*N) * 100:.3f}%")
print(f"Synapse count distribution:")
print(f"  min={counts.min()}, max={counts.max()}, mean={counts.mean():.2f}, median={np.median(counts):.1f}")
print(f"  pairs with ≥5 synapses: {(counts>=5).sum()}")
print(f"  pairs with ≥10 synapses: {(counts>=10).sum()}")
print(f"  pairs with ≥20 synapses: {(counts>=20).sum()}")

# Save connectivity data
np.save('/work/pre_idxs.npy', pre_idxs)
np.save('/work/post_idxs.npy', post_idxs)
np.save('/work/syn_counts.npy', counts)
np.save('/work/syn_sizes.npy', sizes)
sp.save_npz('/work/conn_matrix.npz', conn_matrix)
sp.save_npz('/work/size_matrix.npz', size_matrix)
print("Saved connectivity matrices")
