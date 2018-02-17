import os
import pandas as pd
import datetime
import calendar

prd = '2017-05'  # 'yyyy-mm'
datecol = 'tpep_pickup_datetime'

first = datetime.datetime(*[int(x) for x in prd.split('-')], 1)
hrs_in_month = 24 * calendar.monthrange(first.year, first.month)[1]
idx = pd.date_range(first, name=datecol, periods=hrs_in_month, freq='H')

data_dir = '../neighborhood'
for nh in range(1, 266):
    read = os.path.join(data_dir + str(nh), 'data-{}.csv'.format(prd))
    write = os.path.join(data_dir + str(nh), 'ds-data-{}.csv'.format(prd))
    try:
        data = pd.read_csv(read, index_col=[datecol], parse_dates=[datecol])
        data = data.resample('H').count().reindex(
            idx, fill_value=0).to_csv(write, index=True)
    except:
        pd.DataFrame(columns=['PULocationID'],
                     index=idx).fillna(0).to_csv(write)
        print('neighborhood{} has no data'.format(nh))
