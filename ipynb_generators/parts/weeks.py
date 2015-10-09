import os
from datetime import date, timedelta, datetime
import pandas

IN_IPYTHON = True
try:
    __IPYTHON__
except NameError:
    IN_IPYTHON = False

today = datetime.strptime('2015-09-28', '%Y-%m-%d').date()
last_monday = today - timedelta(days=-today.weekday(), weeks=1)

WEEK_RANGE = pandas.date_range(end=last_monday, periods=15, freq='W-MON')
# TODO for now: from events-2015-06-15.csv to events-2015-09-21.csv
WEEKS = WEEK_RANGE.map(lambda x: x.strftime('%Y-%m-%d'))

if not IN_IPYTHON:
    EVENT_STORAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools', 'out')

OUT_DATA = []
VOLUME_DATA = []

for v in range(0, len(WEEKS)):
    VOLUME_DATA.append([0] * len(WEEKS))

for x in range(0, len(WEEKS)):
    OUT_DATA.append([0] * len(WEEKS))

def week_file(storage, week):
    return os.path.join(storage, 'events-' + week + '.csv')
