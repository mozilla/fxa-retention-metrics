import os, sys
sys.path.append(os.path.realpath(os.curdir))
import constants
from tools.convert_to_book import ConvertToBook

GRAPH_TYPE = os.path.join(constants.THIS_DIR, '..', 'graph_types', 'x_with_y_then_z.py')

# prepare segments
GRAPHS = []

GRAPHS.append({
    "COHORT_QUERY": "SELECT C4 FROM %s WHERE C5 = 'account.created'",
    "COHORT_QUERY_SECONDARY": "SELECT C4 FROM %s WHERE C5 = 'account.login'",
    "REST_QUERY": "SELECT C4 FROM %s",
    "TITLE": "'created' and 'login' in the same week then 'anything' - Multi Device",
    "FILE_NAME": 'created_then_login_multi_device'
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
