# Multiple missing deps. AllenSDK path is blocked. 
# Go direct: read NWBs with h5py to get the data we need.
# The Allen Visual Coding NWBs have a well-documented structure.

import h5py
import numpy as np

# Inspect one NWB to understand its structure
nwb_path = '/data/abo-visualcoding-v1/ophys_experiment_data/573720508.nwb'
with h5py.File(nwb_path, 'r') as f:
    def print_tree(name, obj):
        indent = '  ' * name.count('/')
        if isinstance(obj, h5py.Dataset):
            print(f"{indent}{name}: shape={obj.shape} dtype={obj.dtype}")
        else:
            print(f"{indent}{name}/")
    
    # Print first 2 levels
    def print_level2(name, obj):
        depth = name.count('/')
        if depth <= 2:
            if isinstance(obj, h5py.Dataset):
                print(f"  {'  '*depth}{name}: {obj.shape} {obj.dtype}")
            else:
                print(f"  {'  '*depth}{name}/")
    
    f.visititems(print_level2)
