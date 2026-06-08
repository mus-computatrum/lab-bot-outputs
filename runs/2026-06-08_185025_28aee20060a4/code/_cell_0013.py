import numpy as np
for lbl,f in [('b1',f1),('b2',f2)]:
    idx=f['PM/idx'][:]; idy=f['PM/idy'][:]
    print(lbl,
          "| idx min/max:",idx.min(),idx.max(),
          "| idy min/max:",idy.min(),idy.max(),
          "| n peakStart:",f['PM/peakStart'].shape[0],
          "| n BD/name:",f['BD/name'].shape[0])
# how many idy values exceed peak array len?
idy=f1['PM/idy'][:]
npk=f1['PM/peakStart'].shape[0]
over=(idy>npk).sum()
print("\nb1 idy>npeak count:",over, "unique over vals:", np.unique(idy[idy>npk])[:20], "...n=",len(np.unique(idy[idy>npk])))
