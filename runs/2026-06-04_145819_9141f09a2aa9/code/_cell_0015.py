
# Check manifest for all available files, especially any with dissection_region
import json
with open("/data/yao2023-wmb-10x/_abc_cache/releases/20260415/manifest.json") as f:
    manifest = json.load(f)

# Print all metadata file entries
for dir_name, dir_info in manifest.get('directory_listing', {}).items():
    for file_name in dir_info.get('files', {}).keys():
        print(f"{dir_name}: {file_name}")
