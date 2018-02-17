import pandas as pd
import os

data_dir = '../../data/'
write = os.path.join(data_dir, 'tribeca17.csv')
read = os.path.join(data_dir, 'yellow_tripdata_2017-05.csv')

try:
    os.remove(write)
except OSError:
    pass

to_drop = ['VendorID', 'tpep_dropoff_datetime', 'passenger_count',
           'trip_distance', 'RatecodeID', 'store_and_fwd_flag',
           'payment_type', 'fare_amount', 'extra', 'mta_tax',
           'tip_amount', 'tolls_amount', 'improvement_surcharge',
           'total_amount', 'DOLocationID', 'tpep_pickup_datetime']

chunksize = 10 ** 6
for chunk in pd.read_csv(read, chunksize=chunksize):
    chunk.set_index(pd.to_datetime(
        chunk['tpep_pickup_datetime']), inplace=True)
    chunk.drop(to_drop, axis=1, inplace=True)
    chunk = chunk[chunk['PULocationID'] == 231]

    print('Processed chunk:')
    print(chunk.head(10))
    if os.path.exists(write):
        chunk.to_csv(write, mode='a', header=False, index=True)
    else:
        chunk.to_csv(write, mode='w', index=True)
