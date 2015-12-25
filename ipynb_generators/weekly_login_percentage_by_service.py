import os, sys
sys.path.append(os.path.realpath(os.curdir))
import constants
from tools.convert_to_book import ConvertToBook

GRAPH_TYPE = os.path.join(constants.THIS_DIR, '..', 'graph_types', 'weekly_percentage.py')

# prepare segments
GRAPHS = []

TOTAL_QUERY = "SELECT C4 FROM %s WHERE C5 = 'account.login'"
CHUNK_QUERIES = [
    ("Sync", TOTAL_QUERY + " AND (C6 = 'sync' OR C6 = '')"),
    ("Pocket", TOTAL_QUERY + " AND (C6 = '749818d3f2e7857f' OR C6 = '7377719276ad44ee')"),
    ("Hello", TOTAL_QUERY + " AND C6 = 'a8b39c2b1cab722e'"),
    ("Marketplace", TOTAL_QUERY + " AND C6 = '0a42ac8a73be8762'")
]

GRAPHS.append({
    "TOTAL_QUERY": TOTAL_QUERY,
    "CHUNK_QUERIES": CHUNK_QUERIES,
    "TITLE": "% 'account.login' on various services",
    "FILE_NAME": 'weekly_login_percentage_by_service'
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
