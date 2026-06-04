import os, glob

base = '/data/abo-visualcoding-v1'
print("Top-level contents:")
for f in sorted(os.listdir(base)):
    p = os.path.join(base, f)
    if os.path.isdir(p):
        sub = os.listdir(p)
        print(f"  {f}/  [{len(sub)} items]")
    else:
        sz = os.path.getsize(p)
        print(f"  {f}  ({sz/1e6:.1f} MB)")
