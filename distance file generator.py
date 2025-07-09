import pandas as pd
import numpy as np

# Read sensor IDs from the .h5 file columns
df = pd.read_hdf('data/metr-la.h5')
sensor_ids = df.columns.astype(str).tolist()

rows = []
for i, src in enumerate(sensor_ids):
    for j, dst in enumerate(sensor_ids):
        if src != dst:
            distance = np.random.uniform(50, 100)
            rows.append({'from': src, 'to': dst, 'distance': distance})

distances_df = pd.DataFrame(rows)
distances_df.to_csv('data/sensor_graph/distances_la_2012.csv', index=False)
print("Random distance file generated: data/sensor_graph/distances_la_2012.csv")