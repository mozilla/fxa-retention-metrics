import os, sys
sys.path.append(os.path.realpath(os.curdir))
import constants
from tools.convert_to_book import ConvertToBook

GRAPH_TYPE = os.path.join(constants.THIS_DIR, '..', 'graph_types', 'weekly_percentage.py')

# prepare segments
GRAPHS = []

TOTAL_QUERY = "SELECT C4 FROM %s WHERE C5 = 'account.created'"
CHUNK_QUERIES = [
    ("Android", TOTAL_QUERY + " AND C3 = 'Android'"),
    ("Desktop", TOTAL_QUERY + " AND " + constants.SQL_ALL_DESKTOP_ENVS),
    ("Firefox for iOS", TOTAL_QUERY + " AND C1 = 'FxiOS'")
]

GRAPHS.append({
    "TOTAL_QUERY": TOTAL_QUERY,
    "CHUNK_QUERIES": CHUNK_QUERIES,
    "TITLE": "% 'account.created' on various platforms",
    "FILE_NAME": 'weekly_created_percentage'
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
