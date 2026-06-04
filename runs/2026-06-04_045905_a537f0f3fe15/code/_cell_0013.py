# Good! First NWB is already Sst-IRES-Cre + VISp. Now understand DfOverF structure.
with h5py.File(nwb_path, 'r') as f:
    dff = f['processing/brain_observatory_pipeline/DfOverF']
    print("DfOverF keys:", list(dff.keys()))
    
    roi_series = dff['imaging_plane_1']
    print("\nROI series keys:", list(roi_series.keys()))
    for k in roi_series.keys():
        v = roi_series[k]
        if isinstance(v, h5py.Dataset):
            print(f"  {k}: shape={v.shape} dtype={v.dtype}")
