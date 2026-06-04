import numpy as np

base = '/data/bugeon2022-v1'

# Check state names
states_names = open(f'{base}/states.names.txt').read()
print("State names:", states_names)

# Sample one session
sample_dir = f'{base}/SB025/2019-10-04'
ttypes = open(f'{sample_dir}/neuron.ttype.txt').read().splitlines()
print(f"\nn_neurons: {len(ttypes)}")
print("Sample ttypes:", ttypes[:10])
print("SST count:", sum(1 for t in ttypes if t.startswith('Sst')))

# Sample one recording
rec_dir = f'{sample_dir}/Drifting Gratings/01'
activity = np.load(f'{rec_dir}/frame.neuralActivity.npy')
states = np.load(f'{rec_dir}/frame.states.npy')
print(f"\nActivity shape: {activity.shape}  (frames x neurons)")
print(f"States shape: {states.shape}")
print(f"Unique states: {np.unique(states)}")
print(f"State counts: { {s: (states==s).sum() for s in np.unique(states)} }")
print(f"Activity dtype: {activity.dtype}, range: [{activity.min():.3f}, {activity.max():.3f}]")
