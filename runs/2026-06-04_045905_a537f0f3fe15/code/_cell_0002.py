import json

# Look at manifest
with open('/data/abo-visualcoding-v1/manifest.json') as f:
    manifest = json.load(f)
print(json.dumps(manifest, indent=2)[:3000])
