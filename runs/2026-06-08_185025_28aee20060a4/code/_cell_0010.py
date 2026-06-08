import subprocess, os, gzip, shutil, h5py
base='/work/staged/green-2023-ppc-inhibitory-snatac'
# decompress snap.gz -> .snap (need uncompressed to open with h5py)
for gsm in ['GSM7317753_biorep1','GSM7317754_biorep2']:
    src=f"{base}/{gsm}.snap.gz"; dst=f"/work/{gsm}.snap"
    if not os.path.exists(dst):
        with gzip.open(src,'rb') as fi, open(dst,'wb') as fo:
            shutil.copyfileobj(fi, fo, length=64*1024*1024)
    print(dst, f"{os.path.getsize(dst)/1e9:.2f} GB")

# inspect HDF5 structure of biorep1
f=h5py.File('/work/GSM7317753_biorep1.snap','r')
def show(name,obj):
    import h5py as _h
    if isinstance(obj,_h.Dataset):
        print(f"  D {name:40s} shape={obj.shape} dtype={obj.dtype}")
    else:
        print(f"  G {name}")
f.visititems(show)
print("\nroot attrs:", dict(f.attrs))
