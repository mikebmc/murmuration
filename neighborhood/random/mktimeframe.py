import io
import os
import re
import pandas as pd


def natsorted(a_list):
    '''
    Return a_list naturally sorted. See natural sorting.
    '''
    def convert(e): return int(e) if e.isdigit() else e.lower()

    def key(e): return [convert(c) for c in re.split('([0-9]+)', e)]
    return sorted(a_list, key=key)


prd = '2017-05'
neighborhoods = natsorted([dir for dir in os.listdir(
    '../') if 'neighborhood' in dir])
linum = 10

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
