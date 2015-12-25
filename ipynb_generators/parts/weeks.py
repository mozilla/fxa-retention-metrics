import os
from datetime import date, timedelta, datetime
import pandas

IN_IPYTHON = True
try:
    __IPYTHON__
except NameError:
    IN_IPYTHON = False

today = date.today()
# today = datetime.strptime('2015-11-08', '%Y-%m-%d').date()
last_monday = today - timedelta(days=-today.weekday(), weeks=2)

WEEK_RANGE = pandas.date_range(end=last_monday, periods=15, freq='W-MON')
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
