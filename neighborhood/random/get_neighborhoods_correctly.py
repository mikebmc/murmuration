import pandas as pd
import os


def cleanup(fname):
    try:
        os.remove(fname)
    except OSError:
        pass


neighborhood_dir = '../neighborhood'
data_dir = '../../data/'
read = os.path.join(data_dir, 'yellow_tripdata_2017-05.csv')

for nh in range(1, 266):
    write = os.path.join(neighborhood_dir + str(nh), 'data.csv')
    cleanup(write)

to_drop = ['VendorID', 'tpep_dropoff_datetime', 'passenger_count',
           'trip_distance', 'RatecodeID', 'store_and_fwd_flag',
           'payment_type', 'fare_amount', 'extra', 'mta_tax',
           'tip_amount', 'tolls_amount', 'improvement_surcharge',
           'total_amount', 'DOLocationID']

count = 1
chunksize = 10 ** 6
for chunk in pd.read_csv(read, chunksize=chunksize):
    chunk.drop(to_drop, axis=1, inplace=True)
    groupS = chunk.groupby('PULocationID')
    for name, group in groupS:
        write = os.path.join(neighborhood_dir + str(name), 'data.csv')
        if os.path.exists(write):
            group.to_csv(write, mode='a', header=False, index=False)
        else:
            group.to_csv(write, mode='w', index=False)

    print("Processed {}:".format(count))
    count += 1
