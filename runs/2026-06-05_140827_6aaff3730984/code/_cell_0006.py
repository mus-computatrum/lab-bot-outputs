
# 1. Check NWB file accessibility (from prior notes: truncated, but let's verify with h5py)
import h5py, os

nwb_path = '/data/microns-functional/sub-17797_ses-4-scan-9_behavior+image+ophys.nwb'
print(f"NWB size on disk: {os.path.getsize(nwb_path)/1e9:.2f} GB")

try:
    with h5py.File(nwb_path, 'r') as f:
        print(f"File opened OK")
        print(f"Root keys: {list(f.keys())}")
except Exception as e:
    print(f"Error opening NWB: {e}")
