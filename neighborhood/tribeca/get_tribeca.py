import pandas as pd
import numpy as np
from scipy.linalg import circulant
import os

tribeca = pd.read_csv('tribeca_boundries.csv').values.astype('float32').T

edges = tribeca.dot(circulant([-1, 1, 0, 0]))
orths = np.array([[0, 1], [-1, 0]]).dot(edges)
struct = (edges, orths)

# print('circulant([-1, 1, 0, 0]) =\n{}'.format(circulant([-1, 1, 0, 0])))
# print('tribeca.T =\n{}'.format(tribeca.T))
# print('edges =\n{}'.format(edges))
# print('orths =\n{}'.format(orths))
# print('np.sum(orths * edges, axis=0) =\n{}'.format(np.sum(orths * edges,
# axis=0)))

data_dir = '../../data/'

write_data = os.path.join(data_dir, 'tribeca_data_2016-06.csv')
read_data = os.path.join(data_dir, 'yellow_tripdata_2016-06.csv')

try:
    os.remove(write_data)
except OSError:
    pass


def process(chunk, tup, verbose=False):
    # Drop unwanted data and filter away points not inside a convex polygon
    # Inputs:
    #  - chunk   -- dataframe containing lat lon
    #  - tup     -- tuple containing polygon-edges and inward-orth-vectors
    #  - verbose -- print chunk.head() if true
    edg, ort = tup
    latlon = chunk[['pickup_latitude', 'pickup_longitude']
                   ].values.astype('float32')

    index = np.all(latlon.dot(ort) - np.sum(ort * tribeca, axis=0) > 0, axis=1)
    chunk = chunk.loc[index]

    if verbose:
        print("Processed chunk:")
        print(chunk.head())

    if os.path.exists(write_data):
        chunk.to_csv(write_data, mode='a', header=False, index=False)
    else:
        chunk.to_csv(write_data, mode='w', index=False)


to_drop = ['VendorID', 'tpep_dropoff_datetime', 'passenger_count',
           'trip_distance', 'RatecodeID', 'store_and_fwd_flag',
           'dropoff_longitude', 'dropoff_latitude',
           'payment_type', 'fare_amount', 'extra', 'mta_tax',
           'tip_amount', 'tolls_amount', 'improvement_surcharge',
           'total_amount']

chunksize = 10 ** 6
for chunk in pd.read_csv(read_data, chunksize=chunksize):
    chunk.drop(to_drop, axis=1, inplace=True)
    process(chunk, struct, verbose=True)
