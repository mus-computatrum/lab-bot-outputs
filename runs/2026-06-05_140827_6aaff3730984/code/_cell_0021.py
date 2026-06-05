
# Step A2: Identify repeated "Mad Max" clips for noise correlation analysis
with h5py.File(nwb_path, 'r') as f:
    clip_movie = np.array([m.decode() if isinstance(m, bytes) else m 
                           for m in f['intervals/Clip/movie_name'][:]])
    clip_hash  = np.array([h.decode() if isinstance(h, bytes) else h 
                           for h in f['intervals/Clip/condition_hash'][:]])
    clip_start = f['intervals/Clip/start_time'][:]
    clip_stop  = f['intervals/Clip/stop_time'][:]

# Find all Mad Max trials - use condition hash to find exact repeats
madmax_mask = np.array(['Mad Max' in m for m in clip_movie])
madmax_hashes = clip_hash[madmax_mask]
from collections import Counter
hash_counts = Counter(madmax_hashes)
print(f"Mad Max trials: {madmax_mask.sum()}")
print(f"Unique Mad Max condition hashes: {len(hash_counts)}")
print("Hash counts:", sorted(hash_counts.values(), reverse=True)[:10])

# Find the most repeated hash (same clip segment repeated many times)
best_hash = max(hash_counts, key=hash_counts.get)
best_trials = np.where(clip_hash == best_hash)[0]
print(f"\nBest repeated hash: {best_hash[:16]}... ({hash_counts[best_hash]} repeats)")
print(f"Trial indices: {best_trials}")
print(f"Movie names for these trials: {np.unique(clip_movie[best_trials])}")
print(f"Start times: {clip_start[best_trials][:5]}")
print(f"Duration: {(clip_stop[best_trials] - clip_start[best_trials]).mean():.2f} s")

# Use these trials for noise correlation
repeat_starts = clip_start[best_trials]
repeat_stops  = clip_stop[best_trials]
n_repeats = len(best_trials)
print(f"\nNumber of repeats for noise correlation: {n_repeats}")
