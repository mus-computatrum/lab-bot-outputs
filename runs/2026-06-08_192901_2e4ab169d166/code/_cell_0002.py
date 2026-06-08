import os, glob
# Search whole filesystem for registry-like files
for pat in ['/**/registry.y*ml','/**/datasets.y*ml','/**/registry.json','/**/datasets.json']:
    hits = glob.glob(pat, recursive=True)
    hits = [h for h in hits if 'proc/' not in h and 'sys/' not in h]
    if hits: print(pat, '->', hits[:10])

print("\n--- contents of hrvatin dir ---")
print(sorted(os.listdir('/data/hrvatin-2019-pesca-interneuron')))
print("\n--- contents of green dir (registered same day) ---")
print(sorted(os.listdir('/data/green-2023-ppc-inhibitory-snatac')))
print("\n--- contents of a long-standing visible dataset tasic2018-v1 ---")
print(sorted(os.listdir('/data/tasic2018-v1')))
