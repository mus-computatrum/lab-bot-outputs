
# It's a directory - list contents
pq_dir = "/data/yao2023-wmb-10x/_abc_cache/metadata/WMB-10X/20241115/cell_metadata.parquet"
for f in os.listdir(pq_dir):
    size = os.path.getsize(os.path.join(pq_dir, f))
    print(f"  {f}  ({size/1e6:.1f} MB)")
