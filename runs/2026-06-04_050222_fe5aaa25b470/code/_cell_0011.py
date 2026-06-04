import os, subprocess

# Try to find token files more carefully, avoiding permission errors
result = subprocess.run(
    ["find", "/", "-name", "*cave*", "-o", "-name", "*chunkedgraph*", "-o", "-name", "*daf-apis*"],
    capture_output=True, text=True, timeout=10
)
lines = [l for l in result.stdout.splitlines() if 'Permission' not in l and l.strip()]
print("Token-related files found:")
for l in lines[:20]:
    print(" ", l)

# Check cloudvolume secrets directory
result2 = subprocess.run(["ls", "-la", os.path.expanduser("~/.cloudvolume/")],
                         capture_output=True, text=True)
print("\n~/.cloudvolume/:", result2.stdout or result2.stderr)

# Check network
result3 = subprocess.run(["timeout", "3", "curl", "-s", "https://global.daf-apis.com/"],
                         capture_output=True, text=True)
print(f"\nNetwork test: exit={result3.returncode}, out={result3.stdout[:50]}, err={result3.stderr[:50]}")
