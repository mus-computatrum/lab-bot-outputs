# Check which sessions have SST cells and what ttype names look like
import os

base = '/data/bugeon2022-v1'
all_sst = set()

for mouse in sorted(os.listdir(base)):
    mouse_path = os.path.join(base, mouse)
    if not os.path.isdir(mouse_path):
        continue
    for session in sorted(os.listdir(mouse_path)):
        sess_path = os.path.join(mouse_path, session)
        ttype_file = os.path.join(sess_path, 'neuron.ttype.txt')
        if not os.path.exists(ttype_file):
            continue
        ttypes = open(ttype_file).read().splitlines()
        sst_types = [t for t in ttypes if t.startswith('Sst')]
        if sst_types:
            print(f"{mouse}/{session}: {len(sst_types)} SST cells, types: {sorted(set(sst_types))}")
            all_sst.update(sst_types)
        else:
            print(f"{mouse}/{session}: 0 SST cells")

print(f"\nAll unique SST t-types across dataset:")
for t in sorted(all_sst):
    print(f"  {t}")
