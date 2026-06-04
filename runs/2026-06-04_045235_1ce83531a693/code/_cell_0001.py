
import os, glob

# Explore the cache directory structure
for root, dirs, files in os.walk("/data/yao2023-wmb-10x/_abc_cache/metadata"):
    for f in files:
        print(os.path.join(root, f))
