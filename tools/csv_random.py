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
        'avatar.get',
        'avatar.get',
    ])


def random_service():
    return random.choice(['', '', '', '', '', '', '', '', '', '', 'sync', 'sync', 'sync', 'sync', 'foo', 'bar'])


def random_date_range(start):
    end = start + timedelta(weeks=1)
    rand_date = start + timedelta(seconds=randint(0, int((end - start).total_seconds())))

    return int(rand_date.strftime("%s"))


def random_uid(week_number):
    # simulate retention decrease using week_number
    return 'uid' + str(random.randint(1, week_number * 1000))
