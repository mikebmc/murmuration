import io
import os
import re
import datetime
import pandas as pd
from utils import natsorted
from pymongo import MongoClient

min_interval = 60
prd = '2017-02'

# get the date from 1 year ago ignoring leap years
dt = datetime.datetime.now() - datetime.timedelta(days=365)

# round down to the nearest minute divisible by min_interval
num_minutes = dt.minute // min_interval
dt = dt.replace(minute=num_minutes * min_interval,
                second=0).strftime('%Y-%m-%d %H:%M:%S')

# get a naturally sorted list of the neighborhood# directories
neighborhoods = natsorted([dir for dir in os.listdir('../') if 'neigh' in dir])

# aggregate the data from all our csv's
agg = []
for nbh in neighborhoods:
    read = os.path.join('../', nbh, 'ds-data-{}.csv'.format(prd))
    s = io.StringIO()
    with open(read, 'r') as ff:
        s.write(next(ff))
        s.write(next(line for line in ff if re.search('^{}'.format(dt), line)))
        s.seek(0)
    agg.append(pd.read_csv(s, usecols=['PULocationID']))

# combine all of the data matching today's datetime and drop date info
timeframe = pd.concat(agg, axis=0, ignore_index=True)

# the new index is a range beginning at 1
timeframe.index += 1
timeframe.index.name = 'n_id'
timeframe.rename(columns={'PULocationID': 'count'}, inplace=True)

# open a connection to mongodb
client = MongoClient('mongodb://localhost:27017')
db = client.layer_bank

# and replace what's currently inside of the toplayer collection
post_id = db.toplayer.update(
    {}, timeframe.reset_index().to_dict(orient='list'),
    upsert=True)

# tell me the datetime used to collect the data
print('dt =\n{}'.format(dt))
