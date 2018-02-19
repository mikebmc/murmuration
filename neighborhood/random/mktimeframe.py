import io
import os
import pandas as pd
from utils import natsorted

linum = 10
prd = '2017-05'
neighborhoods = natsorted([dir for dir in os.listdir(
    '../') if 'neighborhood' in dir])

agg = []
for nbh in neighborhoods:
    read = os.path.join('../', nbh, 'ds-data-{}.csv'.format(prd))
    s = io.StringIO()
    with open(read, 'r') as ff:
        lines = ff.readlines()
        s.write(lines[0])
        s.write(lines[linum])
        s.seek(0)

    agg.append(pd.read_csv(s, usecols=['PULocationID']))

timeframe = pd.concat(agg, axis=0, ignore_index=True)
timeframe.index += 1
timeframe.index.name = 'n_id'
timeframe.rename(columns={'PULocationID': 'count'}, inplace=True)

print('timeframe =\n{}'.format(timeframe))
