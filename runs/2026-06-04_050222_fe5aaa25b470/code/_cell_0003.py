import h5py, os

nwb_path = "/data/microns-functional/sub-17797_ses-4-scan-9_behavior+image+ophys.nwb"
actual_size = os.path.getsize(nwb_path)
print(f"Actual file size: {actual_size:,} bytes = {actual_size/1e9:.1f} GB")
print(f"Stored EOF:       62,421,277,435 bytes = {62421277435/1e9:.1f} GB")
print(f"File is {actual_size/62421277435*100:.0f}% complete")

# Try swmr=True
try:
    with h5py.File(nwb_path, "r", swmr=True) as f:
        print("\nOpened with swmr=True — listing keys:")
        print(list(f.keys()))
except Exception as e:
    print(f"swmr failed: {e}")
