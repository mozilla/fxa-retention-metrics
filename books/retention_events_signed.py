import os, sys
sys.path.append(os.path.realpath(os.curdir))
from tools.convert_to_book import ConvertToBook

# dev event storage
books_dir = os.path.dirname(os.path.abspath(__file__))
dev_event_path = os.path.join(books_dir, '..', 'tools', 'out')

# prod event storage
prod_event_path = 's3://telemetry-private-analysis/fxa-retention/data/'

dev_book = ConvertToBook(
    script_file=os.path.join(books_dir, '..', 'metrics', 'retention_events_signed.py'),
    book_title='User Retention using accounts.signed events DEVELOPMENT',
    book_target_path=os.path.join(books_dir, '..', 'ipynb', 'dev'),
    event_storage=dev_event_path
)

dev_book.write_book()

prod_book = ConvertToBook(
    script_file=os.path.join(books_dir, '..', 'metrics', 'retention_events_signed.py'),
    book_title='User Retention using accounts.signed events',
    book_target_path=os.path.join(books_dir, '..', 'ipynb', 'prod'),
    event_storage=prod_event_path
)

prod_book.write_book()
