import os, glob
print("=== /data listing ===")
for p in sorted(glob.glob("/data/*")):
    print(p, "DIR" if os.path.isdir(p) else "file")
print("\n=== look for registry files ===")
for pat in ["/data/registry.yaml","/data/registry.yml","/data/*.yaml","/data/*.yml","/data/*.json","/config/*","/work/staged/*"]:
    for p in glob.glob(pat):
        print(p)
