import h5py

nwb_path = "/data/microns-functional/sub-17797_ses-4-scan-9_behavior+image+ophys.nwb"

def print_tree(name, obj, depth=0, max_depth=4):
    indent = "  " * depth
    if depth > max_depth:
        return
    if isinstance(obj, h5py.Group):
        print(f"{indent}[G] {name.split('/')[-1] if name else '/'}")
        for k in list(obj.keys())[:30]:
            print_tree(name + "/" + k, obj[k], depth+1, max_depth)
    elif isinstance(obj, h5py.Dataset):
        print(f"{indent}[D] {name.split('/')[-1]} shape={obj.shape} dtype={obj.dtype}")

with h5py.File(nwb_path, "r") as f:
    print_tree("", f, 0, 3)
