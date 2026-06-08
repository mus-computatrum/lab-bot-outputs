import os, glob
for p in glob.glob('/work/*.snap')+glob.glob('/work/staged/green-2023-ppc-inhibitory-snatac/*'):
    print(f"{os.path.getsize(p)/1e9:8.2f} GB  {p}")
print("---h5ads done so far---")
for p in glob.glob('/work/*.h5ad'):
    print(f"{os.path.getsize(p)/1e6:8.1f} MB  {p}")
