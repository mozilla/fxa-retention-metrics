import os, sys
sys.path.append(os.path.realpath(os.curdir))
import constants
from tools.convert_to_book import ConvertToBook

GRAPH_TYPE = os.path.join(constants.THIS_DIR, '..', 'graph_types', 'weekly_percentage.py')

# prepare segments
GRAPHS = []

TOTAL_QUERY = "SELECT C4 FROM %s WHERE (C5 = 'account.created' OR C5 = 'account.login')"
CHUNK_QUERIES = [
    ("Created", TOTAL_QUERY + " AND C5 = 'account.created'"),
    ("Login", TOTAL_QUERY + " AND C5 = 'account.login'"),
]

GRAPHS.append({
    "TOTAL_QUERY": TOTAL_QUERY,
    "CHUNK_QUERIES": CHUNK_QUERIES,
    "TITLE": "% 'account.created' vs 'account.login'",
    "FILE_NAME": 'weekly_created_vs_login_percentage'
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
