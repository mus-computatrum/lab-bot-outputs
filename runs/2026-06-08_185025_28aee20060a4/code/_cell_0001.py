import os, glob
for base in ['/work']:
    for root, dirs, files in os.walk(base):
        # skip deep hidden
        if '.ipython' in root or '.cache' in root: 
            continue
        depth = root[len(base):].count(os.sep)
        if depth > 3: 
            continue
        for f in files:
            p = os.path.join(root,f)
            try:
                sz = os.path.getsize(p)
            except: 
                sz = -1
            print(f"{sz/1e6:10.2f} MB  {p}")
