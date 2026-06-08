import os, glob
for d in ["tasic2018-v1","green-2023-ppc-inhibitory-snatac","hrvatin-2019-pesca-interneuron","bakken2021-biccn-m1"]:
    print(f"\n=== /data/{d} ===")
    base=f"/data/{d}"
    for root,dirs,files in os.walk(base):
        for f in sorted(files):
            p=os.path.join(root,f)
            print(f"  {p}  {os.path.getsize(p)/1e6:.1f} MB")
