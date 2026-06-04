import subprocess, os

# Check filesystem type and whether /work and /data share the same fs
result = subprocess.run(["df", "-T", "/work", "/data"], capture_output=True, text=True)
print(result.stdout)

# Try reflink copy (instant on btrfs/XFS)
nwb_src = "/data/microns-functional/sub-17797_ses-4-scan-9_behavior+image+ophys.nwb"
nwb_dst = "/work/sub17797_ses4_scan9_patched.nwb"

if not os.path.exists(nwb_dst):
    cp_res = subprocess.run(
        ["cp", "--reflink=auto", nwb_src, nwb_dst],
        capture_output=True, text=True
    )
    print("reflink cp exit:", cp_res.returncode)
    print(cp_res.stderr or "(no stderr)")
    if os.path.exists(nwb_dst):
        print("Copy exists:", os.path.getsize(nwb_dst), "bytes")
else:
    print("Already exists:", os.path.getsize(nwb_dst))
