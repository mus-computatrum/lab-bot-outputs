
# Step 3: Compute pairwise soma distances for all proofread neurons
# Use vectorized computation — 2316 neurons → 2316^2/2 ≈ 2.68M pairs

soma_xyz = positions_um  # (2316, 3) in µm

# Compute all pairwise distances efficiently using broadcasting in chunks
# Full matrix: 2316^2 * 8 bytes = ~43 MB — feasible
print("Computing pairwise soma distances...")
from scipy.spatial.distance import cdist

dist_matrix = cdist(soma_xyz, soma_xyz, metric='euclidean')  # shape (N, N)
print(f"Distance matrix shape: {dist_matrix.shape}")
print(f"Distance range: {dist_matrix[dist_matrix>0].min():.2f} – {dist_matrix.max():.2f} µm")
print(f"Median non-zero distance: {np.median(dist_matrix[dist_matrix>0]):.1f} µm")

# Save distance matrix
np.save('/work/dist_matrix.npy', dist_matrix.astype(np.float32))
print("Saved distance matrix")
