import os
import random
from datetime import timedelta
from random import randint

random.seed(os.urandom(64))


def random_event():
    return random.choice([
        'account.signed',
        'account.signed',
        'account.signed',
        'account.signed',
        'account.signed',
        'account.signed',
        'account.signed',
        'account.signed',
        'account.signed',
        'account.signed',
        'account.signed',
        'account.signed',
        'account.created',
        'account.created',
        'account.login',
        'account.login',
        'account.login',
        'account.login',
        'avatar.get',
        'avatar.get',
        'avatar.post',
        'avatar.post',
    ])


def random_service():
    return random.choice(['', '', '', '', '', '', '', '', '', '', 'sync', 'sync', 'sync', 'sync', '749818d3f2e7857f', '7377719276ad44ee', 'a8b39c2b1cab722e', '0a42ac8a73be8762'])


def random_browser():
    return random.choice(['Firefox', 'Firefox', 'Firefox', 'Firefox', 'Firefox', 'Firefox', 'Firefox', 'Chrome', 'Safari'])


def random_version():
    return random.choice(['37', '38', '39', '40', '41', '42'])


def random_os():
    return random.choice(['Windows 7', 'Macintosh', 'Windows 8', 'Windows 8.1', 'Windows 10', 'Macintosh', 'Android', 'Linux'])

def random_date_range(start):
    end = start + timedelta(weeks=1)
    rand_date = start + timedelta(seconds=randint(0, int((end - start).total_seconds())))

    return int(rand_date.strftime("%s"))


def random_uid(week_number):
    # simulate retention decrease using week_number
    return 'uid' + str(random.randint(1, week_number * 1000))
