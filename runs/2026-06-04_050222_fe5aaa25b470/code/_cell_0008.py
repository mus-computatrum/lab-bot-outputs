import h5py

nwb_dst = "/work/sub17797_ses4_scan9_patched.nwb"

try:
    with h5py.File(nwb_dst, "r") as f:
        print("Opened! Top-level keys:", list(f.keys()))
except Exception as e:
    print(f"Still failed: {e}")
