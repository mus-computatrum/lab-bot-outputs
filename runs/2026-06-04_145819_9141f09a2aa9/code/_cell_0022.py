
# Check the parquet file
import pyarrow.parquet as pq
pq_path = "/data/yao2023-wmb-10x/_abc_cache/metadata/WMB-10X/20241115/cell_metadata.parquet"
schema = pq.read_schema(pq_path)
print("Parquet schema:")
for field in schema:
    print(f"  {field.name}: {field.type}")
