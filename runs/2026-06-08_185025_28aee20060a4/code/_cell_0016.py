import subprocess
print(subprocess.run(['free','-g'],capture_output=True,text=True).stdout)
print(subprocess.run(['bash','-c','cat /sys/fs/cgroup/memory.max 2>/dev/null || cat /sys/fs/cgroup/memory/memory.limit_in_bytes 2>/dev/null'],capture_output=True,text=True).stdout)
