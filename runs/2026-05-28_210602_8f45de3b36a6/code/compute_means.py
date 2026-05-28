# Synthetic /code output. Computes per-cluster means.
import pandas as pd
df = pd.DataFrame({'cluster':[0,0,1,1], 'x':[1.0,2.0,3.0,4.0]})
print(df.groupby('cluster').mean())
