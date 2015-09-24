import os, sys
sys.path.append(os.path.realpath(os.curdir))

from datetime import date, timedelta
import csv
from tools.csv_random import random_event, random_service, random_date_range, random_uid

class GenerateMockCsv:
    """
    This class generates several weeks of dummy event data
    """
    def __init__(self, target_file, week, week_number):
        self.week = week
        self.week_number = week_number
        self.target_file = target_file

    def write_csv(self):
        headers = [
            'event',
            'userAgent',
            'service',
            'Timestamp',
            'uid'
        ]

        with open(self.target_file, 'wb') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(headers)

            for x in range(0, 5000):
                userAgent = 'Mozilla/5.0 (Windows NT 6.0; rv:40.0) Gecko/20100101 Firefox/40.0'

                event = [
                    random_event(),
                    userAgent,
                    random_service(),
                    random_date_range(starting_week),
                    random_uid(self.week_number)
                ]

                writer.writerow(event)

if __name__ == '__main__':
    today = date.today()
    last_monday = today + timedelta(days=-today.weekday(), weeks=1)
    for x in range(2, 14):
        starting_week = last_monday - timedelta(days=7 * x)
        formatted_week = starting_week.strftime('%Y-%m-%d')
        tool_dir = os.path.dirname(os.path.abspath(__file__))

        mock_csv = GenerateMockCsv(os.path.join(tool_dir, 'out', 'events-' + formatted_week + '.csv'), starting_week, 14 - x)
        mock_csv.write_csv()
