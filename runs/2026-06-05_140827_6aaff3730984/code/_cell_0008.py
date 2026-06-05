
import h5py, numpy as np, pandas as pd

with h5py.File(nwb_path, 'r') as f:
    # Check imaging rates and plane metadata
    img_rate = f['general/optophysiology/ImagingPlane1/imaging_rate'][()]
    indicator = f['general/optophysiology/ImagingPlane1/indicator'][()]
    location = f['general/optophysiology/ImagingPlane1/location'][()]
    origin_coords = f['general/optophysiology/ImagingPlane1/origin_coords'][:]
    grid_spacing = f['general/optophysiology/ImagingPlane1/grid_spacing'][:]
    
    print(f"Imaging rate: {img_rate} Hz")
    print(f"Indicator: {indicator}")
    print(f"Location: {location}")
    print(f"Origin coords (nm?): {origin_coords}")
    print(f"Grid spacing (um?): {grid_spacing}")

    # Check session info
    sess_id = f['general/session_id'][()]
    print(f"\nSession ID: {sess_id}")
    
    # Check mask_type for plane 1 (could be cell type labels)
    mask_type1 = f['processing/ophys/ImageSegmentation/PlaneSegmentation1/mask_type'][:]
    print(f"\nMask type unique values (plane 1): {np.unique(mask_type1)[:10]}")
    print(f"Mask type sample: {mask_type1[:5]}")
    
    # Get unit IDs (ROI ids)
    unit_ids_p1 = f['processing/ophys/ImageSegmentation/PlaneSegmentation1/id'][:]
    print(f"\nUnit IDs plane 1 (first 10): {unit_ids_p1[:10]}")
    print(f"Unit IDs plane 1 (last 5): {unit_ids_p1[-5:]}")

    # Get total ROIs across all planes
    total = 0
    for i in range(1, 9):
        n = f[f'processing/ophys/Fluorescence/RoiResponseSeries{i}/data'].shape[1]
        ts = f[f'processing/ophys/Fluorescence/RoiResponseSeries{i}/timestamps'][:]
        rate = 1.0 / np.median(np.diff(ts))
        total += n
        print(f"  Plane {i}: {n} ROIs, {len(ts)} frames, rate≈{rate:.2f} Hz")
    print(f"Total ROIs: {total}")
    
    # Check stimulus timestamps
    clip_start = f['intervals/Clip/start_time'][:]
    clip_stop = f['intervals/Clip/stop_time'][:]
    clip_stim = f['intervals/Clip/stimulus_type'][:5]
    print(f"\nClip trials: {len(clip_start)}")
    print(f"Clip duration range: {(clip_stop - clip_start).min():.2f} - {(clip_stop - clip_start).max():.2f} s")
    print(f"Clip stim types: {np.unique(f['intervals/Clip/stimulus_type'][:])}")
    print(f"Clip movie names (first 5): {f['intervals/Clip/movie_name'][:5]}")
