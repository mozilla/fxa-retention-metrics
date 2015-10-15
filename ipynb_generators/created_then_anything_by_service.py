import os, sys
sys.path.append(os.path.realpath(os.curdir))
import constants
from tools.convert_to_book import ConvertToBook

GRAPH_TYPE = os.path.join(constants.THIS_DIR, '..', 'graph_types', 'x_then_y.py')

# prepare segments
GRAPHS = []

GRAPHS.append({
    "COHORT_QUERY": "SELECT C4 FROM %s WHERE C5 = 'account.created' AND C6 = 'a8b39c2b1cab722e'",
    "REST_QUERY": "SELECT C4 FROM %s",
    "TITLE": "'created' then did 'anything' - Hello",
    "FILE_NAME": 'created_then_anything_by_service_hello'
})

GRAPHS.append({
    "COHORT_QUERY": "SELECT C4 FROM %s WHERE C5 = 'account.created' AND C6 = '0a42ac8a73be8762'",
    "REST_QUERY": "SELECT C4 FROM %s",
    "TITLE": "'created' then did 'anything' - Marketplace",
    "FILE_NAME": 'created_then_anything_by_service_marketplace'
})

GRAPHS.append({
    "COHORT_QUERY": "SELECT C4 FROM %s WHERE C5 = 'account.created' AND (C6 = '749818d3f2e7857f' OR C6 = '7377719276ad44ee')",
    "REST_QUERY": "SELECT C4 FROM %s",
    "TITLE": "'created' then did 'anything' - Pocket",
    "FILE_NAME": 'created_then_anything_by_service_pocket'
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
