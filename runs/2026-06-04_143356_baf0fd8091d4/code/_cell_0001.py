
import os, pathlib

base = pathlib.Path("/data/vizgen-merfish-brain-map/Slice3_Replicate1")
parquet_dir = base / "detected_transcripts.parquet"
csv_file    = base / "detected_transcripts.csv"

print("parquet dir exists:", parquet_dir.exists())
if parquet_dir.exists():
    # show partition structure
    for p in sorted(parquet_dir.iterdir())[:10]:
        print(" ", p.name)
print("csv exists:", csv_file.exists())
