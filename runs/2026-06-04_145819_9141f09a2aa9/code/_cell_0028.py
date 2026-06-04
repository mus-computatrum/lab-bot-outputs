
# Let me check the full file listing again to see what other metadata might be available
import subprocess
result = subprocess.run(['find', '/data/yao2023-wmb-10x/_abc_cache', '-name', '*.csv', '-o', '-name', '*.parquet'],
                      capture_output=True, text=True)
for line in sorted(result.stdout.strip().split('\n')):
    print(line)
