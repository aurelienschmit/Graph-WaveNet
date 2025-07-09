import pandas as pd
import numpy as np
"""df = pd.read_hdf('data/metr-la.h5')
df.to_csv('data/metr-la.csv')
print("Exported to data/metr-la.csv")
print(df.head())"""

file_type = 'npz'

name = 'METR-LA/val'

directory = 'data/' + name + '.' + file_type

if file_type == 'h5':
    df = pd.read_hdf(directory)
    print(df.head())
    print(df.columns)
    print(df.shape)
else :
    npz = np.load(directory)
    #df= pd.DataFrame.from_dict({item: npz[item] for item in npz.files}, orient='index')
    print(npz['x'])