print("binary columns:", list(binr.columns))
import numpy as np
lay=atac.layers['binary'].toarray()
print("binary layer NaN frac:", np.isnan(lay).mean())
