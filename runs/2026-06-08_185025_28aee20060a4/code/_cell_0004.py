import tarfile, os, gzip, pandas as pd, glob
base='/work/staged/hrvatin-2019-pesca-interneuron'
print(os.listdir(base))
# peek inside RAW.tar
with tarfile.open(os.path.join(base,'GSE136802_RAW.tar')) as t:
    names=t.getnames()
print(f"\nRAW.tar has {len(names)} members")
for n in names[:30]: print('  ',n)
print('  ...' if len(names)>30 else '')
# categorize
import collections
def cat(n):
    if n.endswith('.counts.tsv.gz'): return 'scRNA counts tsv'
    if n.endswith('.bed.gz'): return 'atac bed'
    return 'other'
c=collections.Counter(cat(n) for n in names)
print("\ncategories:",dict(c))
