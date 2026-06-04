# ROI names are generic ('roi_XXXX'). We need actual cell_specimen_ids.
# Those are stored in ImageSegmentation.

with h5py.File(nwb_path, 'r') as f:
    seg = f['processing/brain_observatory_pipeline/ImageSegmentation']
    print("ImageSegmentation keys:", list(seg.keys()))
    
    plane = seg['imaging_plane_1']
    print("imaging_plane_1 keys:", list(plane.keys()))
    
    rois = plane['roi_list']
    print("roi_list shape/dtype:", rois.shape, rois.dtype)
    print("First 5:", rois[:5])
