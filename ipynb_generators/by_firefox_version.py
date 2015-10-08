import os, sys
sys.path.append(os.path.realpath(os.curdir))

from tools.convert_to_book import ConvertToBook
import constants

SEGMENTS = [
    '37',
    '38',
    '39',
    '40',
    '41',
    '42',
    '43',
    '44',
    '45'
]

GRAPH_TYPE = os.path.join(constants.THIS_DIR, '..', 'graph_types', 'x_then_y.py')

# prepare segments
GRAPHS = []
for p in SEGMENTS:
    GRAPHS.append({
        "COHORT_QUERY": "SELECT C4 FROM %s WHERE C5 = 'account.created' AND C1 = 'Firefox' AND C2 = '%s'" % ('%s', p),
        "REST_QUERY": "SELECT C4 FROM %s",
        "TITLE": "'created' then did 'anything' - Firefox v%s" % p,
        "FILE_NAME": 'created_then_anything_by_firefox_version_%s' % p
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
