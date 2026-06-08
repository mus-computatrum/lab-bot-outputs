import tarfile, gzip, io, pandas as pd
base='/work/staged/hrvatin-2019-pesca-interneuron'
t=tarfile.open(os.path.join(base,'GSE136802_RAW.tar'))

# peek one scRNA counts tsv
m='GSM4058339_180320_6-19-1-1_WITH_BARCODES.counts.tsv.gz'
f=t.extractfile(m)
raw=gzip.decompress(f.read())
head=raw[:800].decode('utf-8','replace')
print("=== scRNA counts tsv head ===")
print(head)
print("\n... lines:", raw.count(b'\n'))

# atac master counts
print("\n=== atac_master_counts.csv head ===")
with gzip.open(os.path.join(base,'GSE136802_atac_master_counts.csv.gz'),'rt') as fh:
    for i,line in enumerate(fh):
        print(line.rstrip()[:300])
        if i>4: break

print("\n=== S2_annotated_gres.csv head ===")
with gzip.open(os.path.join(base,'GSE136802_S2_annotated_gres.csv.gz'),'rt') as fh:
    for i,line in enumerate(fh):
        print(line.rstrip()[:300])
        if i>4: break
