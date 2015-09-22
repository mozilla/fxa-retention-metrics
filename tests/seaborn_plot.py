"""
This is a plotting playground
"""
# plot = [
#     [557, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 98],
#     [557, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 98],
#     [557, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 98],
#     [557, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 98],
#     [557, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 98],
#     [557, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 98],
#     # [548, 100, 100, 100, 100, 100, 100, 100, 100, 100, 99],
#     # [554, 100, 100, 100, 100, 100, 100, 100, 100, 99],
#     # [539, 100, 100, 100, 100, 100, 100, 100, 99],
#     # [556, 100, 100, 100, 100, 100, 100, 99], [542, 100, 100, 100, 100, 100, 99], [555, 100, 100, 100, 100, 99],
#     #     [560, 100, 100, 100, 99], [553, 100, 100, 99], [549, 100, 99], [544, 99], [520]
#     ]
# import matplotlib.pyplot as plt
# import numpy as np;
#
# np.random.seed(0)
# import seaborn as sns;
#
# sns.set()
# plt.figure(figsize=(10, 10))
# plt.title('User Retention based on "account.signed"')
# ax = sns.heatmap(plot, annot=True, fmt='d')
# plt.show()

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import pandas as pd
from datetime import date, timedelta

STARTING_POINT = '2015-09-21'

today = date.today()
last_monday = today - timedelta(days=-today.weekday(), weeks=1)
data= [[100, 0, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100], [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 0, 0], [100, 100, 100, 100, 100, 100, 100, 100, 100, 0, 0, 0], [100, 100, 100, 100, 100, 100, 100, 100, 0, 0, 0, 0], [100, 100, 100, 100, 100, 100, 100, 0, 0, 0, 0, 0], [100, 100, 100, 100, 100, 100, 0, 0, 0, 0, 0, 0], [100, 100, 100, 100, 100, 0, 0, 0, 0, 0, 0, 0], [100, 100, 100, 100, 0, 0, 0, 0, 0, 0, 0, 0], [100, 100, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0], [100, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
dates = pd.date_range(end=last_monday, periods=12, freq='W-MON')
dates.format(formatter=lambda x: x.strftime('%Y%m%d'))
print dates


df = pd.DataFrame(data, index=dates)

sns.set(style='white')
plt.figure(figsize=(14, 12))
plt.xlabel('time')
plt.ylabel('s1 and s2')
plt.grid(True)

plt.title('User Retention based on "account.signed"')
sns.heatmap(df, annot=True, fmt='d', yticklabels=dates)
locs, labels = plt.yticks()

plt.setp(labels, rotation=0)
font = {'family': 'normal',
        'weight': 'bold',
        'size': 22}
plt.ylabel('Starting Week', **font)
plt.xlabel('Retention Weeks', **font)
plt.show()