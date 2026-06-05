import subprocess
result = subprocess.run(["pip", "install", "-q", "anndata", "scanpy"], capture_output=True, text=True)
print(result.stdout[-500:] if result.stdout else "")
print(result.stderr[-500:] if result.stderr else "")
print("done")
