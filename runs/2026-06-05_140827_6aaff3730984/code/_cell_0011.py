
# Check for repeated stimulus clips (needed for noise correlation)
with h5py.File(nwb_path, 'r') as f:
    movie_names = f['intervals/Clip/movie_name'][:]
    cond_hash = f['intervals/Clip/condition_hash'][:]
    start_times = f['intervals/Clip/start_time'][:]
    
    movie_names_str = [m.decode() if isinstance(m, bytes) else m for m in movie_names]
    cond_hash_str = [h.decode() if isinstance(h, bytes) else h for h in cond_hash]

print(f"Total clip trials: {len(movie_names_str)}")
from collections import Counter
name_counts = Counter(movie_names_str)
hash_counts = Counter(cond_hash_str)

n_unique_clips = len(name_counts)
n_repeated = sum(1 for c in name_counts.values() if c > 1)
print(f"Unique movie clips: {n_unique_clips}")
print(f"Clips shown >1 time: {n_repeated}")
print(f"\nTop repeated clips:")
for name, cnt in sorted(name_counts.items(), key=lambda x: -x[1])[:10]:
    print(f"  n={cnt}: {name[:80]}")

# Check condition hashes
print(f"\nUnique condition hashes: {len(hash_counts)}")
n_rep_hash = sum(1 for c in hash_counts.values() if c > 1)
print(f"Hashes shown >1 time: {n_rep_hash}")
