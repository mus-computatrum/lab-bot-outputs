import os

ext_dir = "/data/v1dd/extensions"
print("Extensions directory contents:")
for f in sorted(os.listdir(ext_dir)):
    path = os.path.join(ext_dir, f)
    size_mb = os.path.getsize(path) / 1e6
    print(f"  {f}  ({size_mb:.1f} MB)")
