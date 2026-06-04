
import os

base = "/data/vizgen-merfish-brain-map/Slice3_Replicate1"
contents = os.listdir(base)
print("Directory contents:", contents)

# Check for parquet
parquet_path = os.path.join(base, "detected_transcripts.parquet")
csv_path = os.path.join(base, "detected_transcripts.csv")
print("Parquet exists:", os.path.exists(parquet_path))
print("CSV exists:", os.path.exists(csv_path))

# If parquet dir, check its contents
if os.path.isdir(parquet_path):
    print("Parquet dir contents:", os.listdir(parquet_path))
