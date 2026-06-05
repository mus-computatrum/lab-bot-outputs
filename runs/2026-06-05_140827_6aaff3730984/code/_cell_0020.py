
# ═══════════════════════════════════════════════════════════════
# PHASE A — FUNCTIONAL ANALYSIS
# ═══════════════════════════════════════════════════════════════

# Focus on Plane 3 (largest single plane: 1478 ROIs)
# Step A1: Extract ROI centroids from image masks
import h5py, numpy as np

PLANE = 3   # 1-indexed
GRID_UM = 2.5  # µm per pixel

with h5py.File(nwb_path, 'r') as f:
    # Load masks for plane 3 (shape: n_rois x 248 x 440)
    masks = f[f'processing/ophys/ImageSegmentation/PlaneSegmentation{PLANE}/image_mask'][:]
    mask_type = f[f'processing/ophys/ImageSegmentation/PlaneSegmentation{PLANE}/mask_type'][:]
    roi_ids = f[f'processing/ophys/ImageSegmentation/PlaneSegmentation{PLANE}/id'][:]
    origin = f[f'general/optophysiology/ImagingPlane{PLANE}/origin_coords'][:]  # meters
    
    # Load fluorescence traces
    traces = f[f'processing/ophys/Fluorescence/RoiResponseSeries{PLANE}/data'][:]  # (T, N)
    timestamps = f[f'processing/ophys/Fluorescence/RoiResponseSeries{PLANE}/timestamps'][:]

print(f"Masks shape: {masks.shape} (n_rois x H x W)")
print(f"Traces shape: {traces.shape} (frames x rois)")
print(f"ROI ids: {roi_ids[:5]}...{roi_ids[-5:]}")
print(f"Mask types: {np.unique(mask_type)}")
print(f"Origin (m): {origin}")

# Compute centroids: weighted centroid of each mask
# mask is (n_rois, H, W) → centroid (row, col) for each
row_coords = np.arange(masks.shape[1], dtype=np.float32)
col_coords = np.arange(masks.shape[2], dtype=np.float32)
ROW, COL = np.meshgrid(row_coords, col_coords, indexing='ij')

# Centroid = sum(mask * coord) / sum(mask)
mask_sum = masks.sum(axis=(1,2)) + 1e-8
centroid_row = (masks * ROW[np.newaxis]).sum(axis=(1,2)) / mask_sum  # pixels
centroid_col = (masks * COL[np.newaxis]).sum(axis=(1,2)) / mask_sum

# Convert to µm from origin
origin_um = origin * 1e6  # m → µm
centroid_x_um = origin_um[0] + centroid_col * GRID_UM  # col → x
centroid_y_um = origin_um[1] + centroid_row * GRID_UM  # row → y
centroid_z_um = origin_um[2]

del masks  # free RAM
print(f"\nCentroid range:")
print(f"  x: {centroid_x_um.min():.1f} – {centroid_x_um.max():.1f} µm")
print(f"  y: {centroid_y_um.min():.1f} – {centroid_y_um.max():.1f} µm")
print(f"  z: {centroid_z_um:.1f} µm")

# Filter soma-only ROIs (exclude artifacts)
is_soma = np.array([m == b'soma' for m in mask_type])
print(f"\nSoma ROIs: {is_soma.sum()} / {len(is_soma)}")

# Keep only soma ROIs
traces = traces[:, is_soma]
cx = centroid_x_um[is_soma]
cy = centroid_y_um[is_soma]
N_rois = traces.shape[1]
print(f"Soma-only traces: {traces.shape}")
