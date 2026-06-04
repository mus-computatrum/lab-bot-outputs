
import os, sys
# Explore the abc_cache directory structure
base = "/data/yao2023-wmb-10x/_abc_cache"
for root, dirs, files in os.walk(base):
    depth = root.replace(base, '').count(os.sep)
    if depth <= 3:
        indent = "  " * depth
        print(f"{indent}{os.path.basename(root)}/")
        if depth >= 2:
            for f in files[:8]:
                print(f"  {indent}{f}")
            if len(files) > 8:
                print(f"  {indent}... ({len(files)} total)")
