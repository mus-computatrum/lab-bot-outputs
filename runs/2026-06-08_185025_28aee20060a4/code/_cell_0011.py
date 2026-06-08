import gzip, pandas as pd, h5py, numpy as np
base='/work/staged/green-2023-ppc-inhibitory-snatac'
# singlecell.csv
sc1=pd.read_csv(gzip.open(base+'/GSM7317753_biorep1_singlecell.csv.gz','rt'))
print("singlecell.csv shape:",sc1.shape,"\ncols:",list(sc1.columns)[:25])
print(sc1.head(3).to_string())

f1=h5py.File('/work/GSM7317753_biorep1.snap','r')
f2=h5py.File('/work/GSM7317754_biorep2.snap','r')
# peak coordinate check
def peaks(f):
    return (np.array(f['PM/peakChrom']).astype(str), np.array(f['PM/peakStart']), np.array(f['PM/peakEnd']))
c1,s1,e1=peaks(f1); c2,s2,e2=peaks(f2)
print("\nbiorep1 npeaks:",len(c1),"biorep2 npeaks:",len(c2))
print("peak sets identical:", len(c1)==len(c2) and (c1==c2).all() and (s1==s2).all() and (e1==e2).all())
print("idx range b1:", f1['PM/idx'][:].min() if False else 'skip')
print("first peaks:", list(zip(c1[:3],s1[:3],e1[:3])))
