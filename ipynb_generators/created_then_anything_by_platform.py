import os, sys
sys.path.append(os.path.realpath(os.curdir))
import constants
from tools.convert_to_book import ConvertToBook

SEGMENTS = [
    'Windows XP',
    'Windows Vista',
    'Windows 7',
    'Windows 10',
    'Linux',
    'Macintosh',
    'Android'
]

GRAPH_TYPE = os.path.join(constants.THIS_DIR, '..', 'graph_types', 'x_then_y.py')

# prepare segments
GRAPHS = []
for p in SEGMENTS:
    GRAPHS.append({
        "COHORT_QUERY": "SELECT C4 FROM %s WHERE C5 = 'account.created' AND C3 = '%s'" % ('%s', p),
        "REST_QUERY": "SELECT C4 FROM %s",
        "TITLE": "'created' then did 'anything' - %s" % p,
        "FILE_NAME": 'created_then_anything_by_platform_%s' % p.lower().replace (" ", "_")
    })

# All Platforms
GRAPHS.append({
    "COHORT_QUERY": "SELECT C4 FROM %s WHERE C5 = 'account.created'",
    "REST_QUERY": "SELECT C4 FROM %s",
    "TITLE": "'created' then did 'anything' - All Platforms",
    "FILE_NAME": 'created_then_anything_by_platform_all'
})

# All Windows
windows_platforms = "(C3 = 'Windows 7' OR C3 = 'Windows 8' OR C3 = 'Windows 8.1' OR C3 = 'Windows Vista' OR C3 = 'Windows XP' OR C3 = 'Windows 10')"

GRAPHS.append({
    "COHORT_QUERY": "SELECT C4 FROM %s WHERE C5 = 'account.created' AND " + windows_platforms,
    "REST_QUERY": "SELECT C4 FROM %s",
    "TITLE": "'created' then did 'anything' - All Windows",
    "FILE_NAME": 'created_then_anything_by_platform_all_windows'
})

# Windows 8
GRAPHS.append({
    "COHORT_QUERY": "SELECT C4 FROM %s WHERE C5 = 'account.created' AND (C3 = 'Windows 8' OR C3 = 'Windows 8.1')",
    "REST_QUERY": "SELECT C4 FROM %s",
    "TITLE": "'created' then did 'anything' - Windows 8 and 8.1",
    "FILE_NAME": 'created_then_anything_by_platform_windows_8'
})

# FxiOS
# special case, see https://github.com/mozilla-services/puppet-config/pull/1639/files#diff-2dc4fee1b6fdec50c40bbdef11693018R90
GRAPHS.append({
    "COHORT_QUERY": "SELECT C4 FROM %s WHERE C1 = 'FxiOS'",
    "REST_QUERY": "SELECT C4 FROM %s",
    "TITLE": "'anything' then did 'anything' - FxiOS",
    "FILE_NAME": 'anything_then_anything_by_platform_fxios'
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
