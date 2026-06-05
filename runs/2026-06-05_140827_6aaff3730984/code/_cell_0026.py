
# Save functional analysis results
np.save('/work/noise_corr_p3.npy', noise_corr)
np.save('/work/signal_corr_p3.npy', signal_corr)
np.save('/work/total_corr_p3.npy', total_corr)
np.save('/work/roi_dist_p3.npy', roi_dist)
np.save('/work/nc_null.npy', nc_null)

# Save proofreading table with positions
pr.to_csv('/work/proofreading_neurons.csv', index=False)

print("All intermediate results saved.")
print(f"Files in /work:")
import os
for f in sorted(os.listdir('/work')):
    sz = os.path.getsize(f'/work/{f}')
    print(f"  {f}: {sz/1e6:.1f} MB")
