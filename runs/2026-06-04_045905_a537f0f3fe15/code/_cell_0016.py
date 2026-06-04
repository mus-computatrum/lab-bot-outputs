with h5py.File(nwb_path, 'r') as f:
    seg = f['processing/brain_observatory_pipeline/ImageSegmentation']
    
    # cell_specimen_ids - this maps roi → actual specimen ID
    cell_ids = seg['cell_specimen_ids'][:]
    roi_ids = seg['roi_ids'][:]
    print("cell_specimen_ids:", cell_ids)
    print("roi_ids:", roi_ids)
    print("shapes:", cell_ids.shape, roi_ids.shape)
