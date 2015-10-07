"""
This is a plotting playground
"""

import matplotlib.pyplot as plt
import seaborn
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

seaborn.set(style='white')
plt.figure(figsize=(14, 12))
plt.xlabel('time')
plt.ylabel('s1 and s2')
plt.grid(True)

plt.title('User Retention based on "account.signed"')
seaborn.heatmap(df, annot=True, fmt='d', yticklabels=dates)
locs, labels = plt.yticks()

plt.setp(labels, rotation=0)
font = {'family': 'normal',
        'weight': 'bold',
        'size': 22}
plt.ylabel('Starting Week', **font)
plt.xlabel('Retention Weeks', **font)
plt.show()