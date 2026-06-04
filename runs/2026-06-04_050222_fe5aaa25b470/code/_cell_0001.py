import os, pathlib

base = pathlib.Path("/data/microns-functional")
print("Exists:", base.exists())
if base.exists():
    for p in sorted(base.rglob("*.nwb"))[:20]:
        print(p, "  size:", p.stat().st_size // 1024, "KB")
    # Also list top-level structure
    print("\n--- top-level ---")
    for x in sorted(base.iterdir())[:30]:
        print(x)
