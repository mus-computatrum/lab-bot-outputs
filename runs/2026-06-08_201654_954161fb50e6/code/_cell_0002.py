import subprocess
print(subprocess.run(["bash","-lc","find / -name 'registry*.y*ml' 2>/dev/null; echo '---'; find / -iname 'registry*' 2>/dev/null | grep -v proc | head -50"],capture_output=True,text=True).stdout)
