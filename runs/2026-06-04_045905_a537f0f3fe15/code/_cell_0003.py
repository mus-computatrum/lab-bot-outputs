# Examine the experiments JSON to understand schema
with open('/data/abo-visualcoding-v1/ophys_experiments.json') as f:
    experiments_raw = json.load(f)

print(type(experiments_raw))
if isinstance(experiments_raw, list):
    print(f"Total experiments: {len(experiments_raw)}")
    print("First experiment keys:", list(experiments_raw[0].keys()))
    print("First experiment sample:")
    print(json.dumps(experiments_raw[0], indent=2)[:1000])
elif isinstance(experiments_raw, dict):
    print("Keys:", list(experiments_raw.keys()))
