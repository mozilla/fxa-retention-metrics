import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

DEV_EVENT_PATH = os.path.join(THIS_DIR, '..', 'tools', 'out')
PROD_EVENT_PATH = 's3n://net-mozaws-prod-us-west-2-pipeline-analysis/fxa-retention/data/'

DEV_TARGET_PATH = os.path.join(THIS_DIR, '..', 'ipynb', 'dev')
PROD_TARGET_PATH = os.path.join(THIS_DIR, '..', 'ipynb', 'prod')

SQL_ALL_DESKTOP_ENVS = "(C3 = 'Linux' OR C3 = 'Macintosh' OR C3 = 'Windows 7' OR C3 = 'Windows 8' OR C3 = 'Windows 8.1' OR C3 = 'Windows Vista' OR C3 = 'Windows XP' OR C3 = 'Windows 10')"
