import os
# Explore the data directory structure
for root, dirs, files in os.walk('/data/bugeon2022-v1'):
    depth = root.replace('/data/bugeon2022-v1', '').count(os.sep)
    indent = '  ' * depth
    print(f"{indent}{os.path.basename(root)}/")
    for f in files:
        fpath = os.path.join(root, f)
        size_mb = os.path.getsize(fpath) / 1e6
        print(f"{indent}  {f}  ({size_mb:.1f} MB)")
