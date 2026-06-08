import os, glob, yaml
# Find the registry
candidates = glob.glob('/data/**/registry.yaml', recursive=True) + glob.glob('/data/registry.yaml') + glob.glob('/work/**/registry.yaml', recursive=True)
print("registry candidates:", candidates)
print("--- /data listing ---")
print(sorted(os.listdir('/data')))
print("--- /work/staged listing ---")
print(os.listdir('/work/staged') if os.path.exists('/work/staged') else "no /work/staged")
