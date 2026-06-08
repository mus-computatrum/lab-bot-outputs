import subprocess
cmds = [
 "ls -la /work/staged 2>/dev/null || echo 'no /work/staged'",
 "find / -path /proc -prune -o -type d -name 'dataset-registry' -print 2>/dev/null",
 "find / -path /proc -prune -o -type d -name 'cards' -print 2>/dev/null | grep -iv site-packages | head",
 "grep -rl 'tasic2018-v1' / 2>/dev/null | grep -v proc | grep -iv site-packages | head",
]
for c in cmds:
    print("$ "+c)
    print(subprocess.run(["bash","-lc",c],capture_output=True,text=True).stdout or "(empty)")
    print("-"*40)
