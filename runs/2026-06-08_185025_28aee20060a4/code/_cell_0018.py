import os
m=open('/sys/fs/cgroup/memory.max').read().strip()
lim=float(m)/1e9 if m!='max' else 'unlimited'
print("cgroup mem limit GB:", lim)
cur=open('/sys/fs/cgroup/memory.current').read().strip()
print("current usage GB:", float(cur)/1e9)
