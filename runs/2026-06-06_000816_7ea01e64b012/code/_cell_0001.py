
import os, json, glob

# 1. Check if the token file exists
secret_dir = "/home/sandbox/.cloudvolume/secrets"
print("Secret dir exists:", os.path.isdir(secret_dir))

if os.path.isdir(secret_dir):
    files = glob.glob(os.path.join(secret_dir, "**", "*"), recursive=True)
    for f in files:
        print(" ", f)
        # Show content only for token-like files (mask sensitive bits)
        try:
            with open(f) as fh:
                raw = fh.read(200)
            if raw.strip():
                print("    content preview:", raw[:60].replace('\n','\\n'), "...")
        except Exception as e:
            print("    (binary or unreadable)", e)
else:
    print("Secret dir NOT found.")
