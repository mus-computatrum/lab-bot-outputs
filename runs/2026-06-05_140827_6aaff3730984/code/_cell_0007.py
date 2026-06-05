
# NWB opens! Explore the structure
with h5py.File(nwb_path, 'r') as f:
    def print_tree(group, indent=0, max_depth=3, max_children=10):
        if indent > max_depth:
            return
        for i, (key, item) in enumerate(group.items()):
            if i >= max_children:
                print("  " * indent + f"... ({len(group.items())-max_children} more)")
                break
            if isinstance(item, h5py.Dataset):
                print("  " * indent + f"[DS] {key}: shape={item.shape}, dtype={item.dtype}")
            elif isinstance(item, h5py.Group):
                print("  " * indent + f"[GRP] {key}/")
                print_tree(item, indent+1, max_depth, max_children)
    
    print("=== NWB STRUCTURE ===")
    print_tree(f, max_depth=4, max_children=15)
