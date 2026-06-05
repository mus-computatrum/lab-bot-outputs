
# Step A5: Compute pairwise distances between ROI centroids in Plane 3
from scipy.spatial.distance import cdist

roi_xy = np.stack([cx, cy], axis=1)  # (N_rois, 2) in µm
roi_dist = cdist(roi_xy, roi_xy, 'euclidean')  # (N_rois, N_rois) in µm

print(f"ROI distance matrix: {roi_dist.shape}")
print(f"Distance range: {roi_dist[roi_dist>0].min():.2f} – {roi_dist.max():.2f} µm")

# Extract upper triangle
iu = np.triu_indices(N_rois, k=1)
pair_dist_rois = roi_dist[iu]
pair_nc = noise_corr[iu]
pair_sc = signal_corr[iu]
pair_tc = total_corr[iu]

print(f"\nTotal unique ROI pairs: {len(pair_dist_rois):,}")
print(f"\nNoise corr summary by distance:")
for d_max in [20, 40, 60, 100, 200, 500]:
    mask = pair_dist_rois < d_max
    if mask.sum() > 0:
        print(f"  d < {d_max:4d} µm: n={mask.sum():6,}, "
              f"NC mean={pair_nc[mask].mean():.4f} ± {pair_nc[mask].std():.4f}, "
              f"TC mean={pair_tc[mask].mean():.4f} ± {pair_tc[mask].std():.4f}")

# Step A6: Circular-shift surrogate null distribution
# Circularly shift each ROI's noise trace by a random large offset → destroys temporal structure
print("\nComputing circular-shift surrogate null...")
np.random.seed(42)
min_shift = 100  # frames
n_surrogates = 5

nc_surrogate_all = []
for i_sur in range(n_surrogates):
    shifts = np.random.randint(min_shift, noise_flat.shape[1] - min_shift, size=N_rois)
    noise_shifted = np.stack([np.roll(noise_flat[j], shifts[j]) 
                              for j in range(N_rois)], axis=0)
    nc_sur = row_corr(noise_shifted.astype(np.float32))
    nc_surrogate_all.append(nc_sur[iu])

nc_null = np.concatenate(nc_surrogate_all)  # all surrogate pairs
print(f"Surrogate null: mean={nc_null.mean():.4f} ± {nc_null.std():.4f}")
print(f"Observed noise corr: mean={pair_nc.mean():.4f} ± {pair_nc.std():.4f}")
print(f"Surrogate null 95th percentile: {np.percentile(nc_null, 95):.4f}")
print(f"Observed 95th percentile: {np.percentile(pair_nc, 95):.4f}")
