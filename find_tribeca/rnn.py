import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('busy_intersection.csv', sep=',')
print('data.head(5) =', data.head(5))

np.random.seed(1)
# set replace=True for speed
# subset = np.random.choice(range(data.shape[0]), size=100, replace=True)
_1000_trips = data.loc[:1000, :].drop(
    ['tpep_pickup_datetime'], axis=1
)
lat = _1000_trips['pickup_latitude']
lon = _1000_trips['pickup_longitude']

plt.plot(lat, lon)
plt.show()

# random comment
