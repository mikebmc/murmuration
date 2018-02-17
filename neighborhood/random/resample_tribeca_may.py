import os
import pandas as pd

data_dir = '../../data/'
write = os.path.join(data_dir, 'tribeca_resample17.csv')
read = os.path.join(data_dir, 'tribeca17.csv')

tribeca = pd.read_csv(read, index_col='tpep_pickup_datetime',
                      parse_dates=['tpep_pickup_datetime'])
# print('tribeca.head(10) =\n{}'.format(tribeca.head(10)))
tribeca = tribeca.resample('H').count()

# print('tribeca.head(10) =\n{}'.format(tribeca.head(10)))

tribeca.to_csv(write)
