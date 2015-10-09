"""
This is a plotting playground
"""

import matplotlib.pyplot as plt
import seaborn
import pandas as pd
from datetime import date, datetime, timedelta

STARTING_POINT = '2015-09-21'

today = date.today()
last_monday = today - timedelta(days=-today.weekday(), weeks=1)
data = [[100, 44, 22, 24, 17, 15, 17, 12, 11, 12, 7, 5, 8, 7, 6], [100, 30, 22, 20, 15, 8, 14, 13, 11, 8, 9, 3, 11, 10, 0], [100, 22, 14, 18, 12, 12, 15, 9, 7, 9, 5, 7, 9, 0, 0], [100, 23, 15, 20, 13, 16, 7, 5, 5, 7, 8, 6, 0, 0, 0], [100, 16, 13, 8, 8, 6, 10, 12, 9, 7, 3, 0, 0, 0, 0], [100, 24, 14, 10, 9, 9, 10, 5, 7, 6, 0, 0, 0, 0, 0], [100, 16, 13, 17, 13, 5, 9, 9, 3, 0, 0, 0, 0, 0, 0], [100, 9, 7, 4, 8, 9, 5, 4, 0, 0, 0, 0, 0, 0, 0], [100, 11, 10, 7, 6, 7, 5, 0, 0, 0, 0, 0, 0, 0, 0], [100, 9, 6, 2, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0], [100, 7, 5, 12, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [100, 9, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [100, 11, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [100, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# dates = pd.date_range(end=last_monday, periods=12, freq='W-MON')
# dates.format(formatter=lambda x: x.strftime('%Y%m%d'))
# print dates


# df = pd.DataFrame(data, index=dates)
#
# seaborn.set(style='white')
# plt.figure(figsize=(14, 12))
# plt.xlabel('time')
# plt.ylabel('s1 and s2')
# plt.grid(True)
#
# plt.title('User Retention based on "account.signed"')
# seaborn.heatmap(df, annot=True, fmt='d', yticklabels=dates)
# locs, labels = plt.yticks()
#
# plt.setp(labels, rotation=0)
# font = {'family': 'normal',
#         'weight': 'bold',
#         'size': 22}
# plt.ylabel('Starting Week', **font)
# plt.xlabel('Retention Weeks', **font)
# plt.show()
today = datetime.strptime('2015-09-28', '%Y-%m-%d').date()
last_monday = today - timedelta(days=-today.weekday(), weeks=1)

WEEK_RANGE = pd.date_range(end=last_monday, periods=15, freq='W-MON')
# TODO for now: from events-2015-06-15.csv to events-2015-09-21.csv
WEEKS = WEEK_RANGE.map(lambda x: x.strftime('%Y-%m-%d'))
df2 = pd.DataFrame(data, columns=WEEKS)
plt.figure()
df2.plot()
plt.show()