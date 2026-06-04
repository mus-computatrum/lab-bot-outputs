import os, pathlib, subprocess

# Check standard CAVE token locations
token_paths = [
    "~/.cloudvolume/secrets/cave-secret.json",
    "~/.cloudvolume/secrets/chunkedgraph-secret.json",
    "~/.cave-secret.json",
    "~/.config/cave-client/token",
    "/etc/cave-secret.json",
]
for p in token_paths:
    fp = pathlib.Path(p).expanduser()
    if fp.exists():
        print(f"FOUND: {fp}")
    else:
        print(f"      missing: {fp}")

# Also check env vars
for k, v in os.environ.items():
    if 'cave' in k.lower() or 'token' in k.lower() or 'chunked' in k.lower():
        print(f"ENV {k}={v[:20]}...")
        
# Check network connectivity
result = subprocess.run(["curl", "-s", "--connect-timeout", "3",
                         "https://global.daf-apis.com/info/api/v2/"],
                        capture_output=True, text=True)
print(f"\ncurl global.daf-apis.com: exit={result.returncode}, stderr={result.stderr[:100]}")
