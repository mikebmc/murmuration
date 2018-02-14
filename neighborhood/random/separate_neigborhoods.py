import pandas as pd
import os


def cleanup(fname):
    try:
        os.remove(fname)
    except OSError:
        pass


def mkcsv(chunk, fname):
    if os.path.exists(fname):
        chunk.to_csv(fname, mode='a', header=False, index=False)
    else:
        chunk.to_csv(fname, mode='w', index=False)


data_dir = '../../data/'
read = os.path.join(data_dir, 'june17.csv')

num_hoods = 265
for hood in range(1, num_hoods + 1):
    write = os.path.join(
        '../neighborhood' + str(hood), 'data.csv')
    cleanup(write)


label = 'tpep_pickup_datetime'
chunksize = 10 ** 6
for chunk in pd.read_csv(read, chunksize=chunksize):
    chunk['count'] = 1
    chunk.index = pd.to_datetime(chunk[label])
    chunk.drop(label, axis=1, inplace=True)
    to_save = chunk.groupby('PULocationID').resample('30T').sum()

    print('to_save.head() =\n{}'.format(to_save.head()))
    quit()
    write = os.path.join(
        '../neighborhood' + str(hood), 'data.csv')
    tosave = chunk.loc[chunk.loc[:, 'PULocationID'] == hood]
    tosave = tosave.resample('30T').sum()
    mkcsv(tosave, write)
