import numpy as np
chrom=decode(np.array(f1['PM/peakChrom'])); st=f1['PM/peakStart'][:]; en=f1['PM/peakEnd'][:]
# unique chroms in order of appearance
seen=[]; 
for c in chrom:
    if not seen or seen[-1]!=c: seen.append(c)
print("chrom block order (peak coords):", seen)
print("\nfirst 3:", list(zip(chrom[:3],st[:3])))
print("last 5 peak coords:", list(zip(chrom[-5:],st[-5:],en[-5:])))
# HD/SQ contigs
sn=[x.decode() for x in np.array(f1['HD/SQ/SN'])]
print("\nHD/SQ contigs (66):", sn)
# which contigs are NOT represented in peak coords (candidates for missing 63)
print("\ncontigs in SQ but absent from peak coords:", [c for c in sn if c not in set(chrom)])
