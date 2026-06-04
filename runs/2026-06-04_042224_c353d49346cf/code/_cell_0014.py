print("counts.columns[:5]:", counts.columns[:5].tolist())
print("counts.index.name:", counts.index.name)
print("counts.values[:3, :3]:", counts.values[:3, :3])
del counts  # free memory before re-loading