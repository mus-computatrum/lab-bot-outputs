
import os, glob, pandas as pd, numpy as np, pickle
from collections import defaultdict

# ═══════════════════════════════════════════════════════════
# PHASE B — STRUCTURAL ANALYSIS
# ═══════════════════════════════════════════════════════════

# Step 1: Load proofreading table and extract soma positions
pr = pd.read_parquet('/data/microns-minnie65/proofreading_status_and_strategy.parquet')
pr = pr[pr['valid'] == True].copy()

# pt_position is in EM voxel coords (4nm x 4nm x 40nm)
# Convert to nm: x,y * 4, z * 40
VOXEL_SIZE = np.array([4.0, 4.0, 40.0])  # nm per voxel (standard MICrONS voxel size)

positions = np.vstack([np.array(pos) for pos in pr['pt_position']])  # (N,3) voxel coords
positions_nm = positions * VOXEL_SIZE  # convert to nm
positions_um = positions_nm / 1000.0  # convert to µm

pr['soma_x_um'] = positions_um[:, 0]
pr['soma_y_um'] = positions_um[:, 1]
pr['soma_z_um'] = positions_um[:, 2]

print(f"Proofread neurons: {len(pr)}")
print(f"Soma positions (µm) ranges:")
print(f"  x: {positions_um[:,0].min():.1f} – {positions_um[:,0].max():.1f}")
print(f"  y: {positions_um[:,1].min():.1f} – {positions_um[:,1].max():.1f}")
print(f"  z: {positions_um[:,2].min():.1f} – {positions_um[:,2].max():.1f}")

# Build ID → index mapping
root_ids = pr['pt_root_id'].values.astype(str)
id_to_idx = {rid: i for i, rid in enumerate(root_ids)}
N = len(pr)
print(f"\nBuilding connectivity matrix for {N} neurons...")
