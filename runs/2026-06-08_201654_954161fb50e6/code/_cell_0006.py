import subprocess, os
for c in [
 "ls -la /work/staged 2>/dev/null || echo 'NO /work/staged'",
 "ls /work 2>/dev/null",
 "ls -d /data/../* 2>/dev/null",
 "find /data -maxdepth 1 -name '*.yaml' -o -maxdepth 1 -name '*.yml' 2>/dev/null",
]:
    print("$ "+c)
    r=subprocess.run(["bash","-lc",c],capture_output=True,text=True,timeout=20)
    print(r.stdout or "(empty)")
    print("-"*30)
