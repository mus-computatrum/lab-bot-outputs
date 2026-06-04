
# Initialize the ABC Atlas cache
cache = AbcProjectCache.from_local_cache("/data/yao2023-wmb-10x/_abc_cache")
print("Cache initialized")
print("Available files:", cache.list_manifest_data_files("WMB-10X"))
