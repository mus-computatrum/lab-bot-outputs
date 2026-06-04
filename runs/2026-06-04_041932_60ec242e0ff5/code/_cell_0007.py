# Verify both output files
import os
for f in ['/work/sst_state_modulation.csv', '/work/sst_state_modulation_bar.png']:
    size = os.path.getsize(f) / 1024
    print(f"{f}  ({size:.1f} KB)")

# Print CSV contents
print()
import pandas as pd
print(pd.read_csv('/work/sst_state_modulation.csv').to_string(float_format='%.4f'))
