import pandas as pd
import numpy as np

df = pd.read_hdf('data/metr-la.h5')
sensor_ids = df.columns.astype(str).tolist()
np.savetxt('data/sensor_graph/graph_sensor_ids.txt', sensor_ids, delimiter=',', fmt='%s')
