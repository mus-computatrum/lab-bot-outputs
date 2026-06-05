
# Load and inspect the skeletons
with open('/data/microns-minnie65/skeletons/bulk_skeletons.pkl', 'rb') as f:
    skeletons = pickle.load(f)

print(f"Type of skeletons: {type(skeletons)}")
if isinstance(skeletons, dict):
    print(f"Number of skeletons: {len(skeletons)}")
    sample_key = list(skeletons.keys())[0]
    print(f"Sample key type: {type(sample_key)}, value: {sample_key}")
    sample_skel = skeletons[sample_key]
    print(f"Sample skeleton type: {type(sample_skel)}")
    if hasattr(sample_skel, '__dict__'):
        print(f"Skeleton attributes: {list(sample_skel.__dict__.keys())[:20]}")
    elif isinstance(sample_skel, dict):
        print(f"Skeleton keys: {list(sample_skel.keys())[:20]}")
    # Try to inspect
    print(f"\nSample skeleton repr: {repr(sample_skel)[:500]}")
elif isinstance(skeletons, list):
    print(f"Number of skeletons: {len(skeletons)}")
    print(f"First item type: {type(skeletons[0])}")
