
import pandas as pd
import numpy as np

# Compute spatial stats for proxy genes
proxy_stats = []
for gene in proxy_genes:
    sub = df_proxy[df_proxy["gene"] == gene]
    proxy_stats.append({
        "proxy_gene": gene,
        "n_transcripts": len(sub),
        "mean_x": sub["global_x"].mean(),
        "mean_y": sub["global_y"].mean(),
        "std_x": sub["global_x"].std(),
        "std_y": sub["global_y"].std(),
    })

proxy_df = pd.DataFrame(proxy_stats)
print(proxy_df.to_string(index=False))
