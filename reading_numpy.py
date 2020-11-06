import numpy as np  

a = np.load('Data/features_label.npy', allow_pickle=True)

print(a.size)

print(len(a[0]))
