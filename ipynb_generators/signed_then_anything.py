import os, sys
sys.path.append(os.path.realpath(os.curdir))
import constants
from tools.convert_to_book import ConvertToBook

GRAPH_TYPE = os.path.join(constants.THIS_DIR, '..', 'graph_types', 'x_then_y.py')
GRAPHS = []

# All Platforms
GRAPHS.append({
    "COHORT_QUERY": "SELECT C4 FROM %s WHERE C5 = 'account.signed'",
    "REST_QUERY": "SELECT C4 FROM %s",
    "TITLE": "'account.signed' then did 'anything' - All Platforms",
    "FILE_NAME": 'signed_then_anything_by_platform_all'
})

# Android
GRAPHS.append({
    "COHORT_QUERY": "SELECT C4 FROM %s WHERE C5 = 'account.signed' AND C3 = 'Android'",
    "REST_QUERY": "SELECT C4 FROM %s",
    "TITLE": "'account.signed' then did 'anything' - Android",
    "FILE_NAME": 'signed_then_anything_by_platform_android'
})

for g in GRAPHS:
    dev_book = ConvertToBook(
        script_file=GRAPH_TYPE,
        graph_specs=g,
        book_target_path=constants.DEV_TARGET_PATH,
        event_storage=constants.DEV_EVENT_PATH
    )

    dev_book.write_book()

    prod_book = ConvertToBook(
        script_file=GRAPH_TYPE,
        graph_specs=g,
        book_target_path=constants.PROD_TARGET_PATH,
        event_storage=constants.PROD_EVENT_PATH
    )

    prod_book.write_book()
