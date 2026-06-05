
# Check for ROI centroid positions and any additional metadata
with h5py.File(nwb_path, 'r') as f:
    # Get plane segmentation details - look for x,y positions
    ps1 = f['processing/ophys/ImageSegmentation/PlaneSegmentation1']
    print("PlaneSegmentation1 datasets:", list(ps1.keys()))
    
    # Check origin_coords across planes (to understand z-depth)
    print("\nOrigin coords per plane (nm):")
    for i in range(1, 9):
        try:
            oc = f[f'general/optophysiology/ImagingPlane{i}/origin_coords'][:]
            gs = f[f'general/optophysiology/ImagingPlane{i}/grid_spacing'][:]
            loc = f[f'general/optophysiology/ImagingPlane{i}/location'][()]
            n_rois = f[f'processing/ophys/Fluorescence/RoiResponseSeries{i}/data'].shape[1]
            print(f"  Plane {i}: origin={oc}, grid={gs}, loc={loc}, n_rois={n_rois}")
        except Exception as e:
            print(f"  Plane {i}: error - {e}")
    
    # Check if there's any unit_ids or cell type info in the NWB
    print("\nGeneral/subject info:")
    for k in f['general/subject'].keys():
        print(f"  {k}: {f['general/subject/'+k][()]}")
    
    # Look for any deconvolution (spike inference)
    print("\nProcessing/ophys groups:", list(f['processing/ophys'].keys()))
