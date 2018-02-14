import pandas as pd
import os

data_dir = '../../data/'
write = os.path.join(data_dir, 'june17.csv')
read = os.path.join(data_dir, 'yellow_tripdata_2017-06.csv')

to_drop = ['VendorID', 'tpep_dropoff_datetime', 'passenger_count',
           'trip_distance', 'RatecodeID', 'store_and_fwd_flag',
           'payment_type', 'fare_amount', 'extra', 'mta_tax',
           'tip_amount', 'tolls_amount', 'improvement_surcharge',
           'total_amount', 'DOLocationID']

chunksize = 10 ** 6
for chunk in pd.read_csv(read, chunksize=chunksize):
    chunk.drop(to_drop, axis=1, inplace=True)
    if os.path.exists(write):
        chunk.to_csv(write, mode='a', header=False, index=False)
    else:
        chunk.to_csv(write, mode='w', index=False)
