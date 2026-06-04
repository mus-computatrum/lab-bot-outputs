with h5py.File(nwb_path, 'r') as f:
    roi_series = f['processing/brain_observatory_pipeline/DfOverF/imaging_plane_1']
    
    # Cell IDs
    roi_names = roi_series['roi_names'][:]
    print("ROI names (cell specimen IDs):", roi_names[:5])
    print("Number of cells:", len(roi_names))
    print("Number of timepoints:", roi_series['data'].shape[1])
    
    # Timestamps
    ts = roi_series['timestamps'][:]
    print(f"Timestamps: {ts[:5]} ... fps≈{1/(ts[1]-ts[0]):.1f}")
    
    # Stimulus timing - frame_duration is in time (seconds)?
    dg = f['stimulus/presentation/drifting_gratings_stimulus']
    fd = dg['frame_duration'][:]
    print(f"\nframe_duration sample (first 3): {fd[:3]}")
    print(f"frame_duration range: {fd[~np.isnan(fd)].min():.1f} to {fd[~np.isnan(fd)].max():.1f}")
    print("NB: these look like frame indices, not seconds")
    print(f"Total frames in DfF: {roi_series['data'].shape[1]}")
