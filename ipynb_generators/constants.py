import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

DEV_EVENT_PATH = os.path.join(THIS_DIR, '..', 'tools', 'out')
PROD_EVENT_PATH = 's3n://net-mozaws-prod-us-west-2-pipeline-analysis/fxa-retention/data/'

DEV_TARGET_PATH = os.path.join(THIS_DIR, '..', 'ipynb', 'dev')
PROD_TARGET_PATH = os.path.join(THIS_DIR, '..', 'ipynb', 'prod')
