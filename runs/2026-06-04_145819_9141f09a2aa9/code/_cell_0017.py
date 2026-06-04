
# Let's look at what WMB-10X metadata files are available locally
import os
base = "/data/yao2023-wmb-10x/_abc_cache/metadata/WMB-10X/20241115"
print("WMB-10X metadata files:")
for f in os.listdir(base):
    size = os.path.getsize(os.path.join(base, f))
    print(f"  {f}  ({size/1e6:.1f} MB)")

# Check if there's a views subdir
if os.path.exists(base + "/views"):
    for f in os.listdir(base + "/views"):
        size = os.path.getsize(os.path.join(base, "views", f))
        print(f"  views/{f}  ({size/1e6:.1f} MB)")
