import os, sys
sys.path.append(os.path.realpath(os.curdir))
from tools.convert_to_book import ConvertToBook

# dev event storage
books_dir = os.path.dirname(os.path.abspath(__file__))
dev_event_path = os.path.join(books_dir, '..', 'tools', 'out')

# prod event storage
prod_event_path = 's3n://net-mozaws-prod-us-west-2-pipeline-analysis/fxa-retention/data/'

# Android

dev_book = ConvertToBook(
    script_file=os.path.join(books_dir, '..', 'metrics', 'account_created_android.py'),
    book_title='User Retention using account.created events DEVELOPMENT Android',
    book_target_path=os.path.join(books_dir, '..', 'ipynb', 'dev'),
    event_storage=dev_event_path
)

dev_book.write_book()

prod_book = ConvertToBook(
    script_file=os.path.join(books_dir, '..', 'metrics', 'account_created_android.py'),
    book_title='User Retention using account.created events Android',
    book_target_path=os.path.join(books_dir, '..', 'ipynb', 'prod'),
    event_storage=prod_event_path
)

prod_book.write_book()

# Linux

dev_book = ConvertToBook(
    script_file=os.path.join(books_dir, '..', 'metrics', 'account_created_linux.py'),
    book_title='User Retention using account.created events DEVELOPMENT Linux',
    book_target_path=os.path.join(books_dir, '..', 'ipynb', 'dev'),
    event_storage=dev_event_path
)

dev_book.write_book()

prod_book = ConvertToBook(
    script_file=os.path.join(books_dir, '..', 'metrics', 'account_created_linux.py'),
    book_title='User Retention using account.created events Linux',
    book_target_path=os.path.join(books_dir, '..', 'ipynb', 'prod'),
    event_storage=prod_event_path
)

prod_book.write_book()


# Mac

dev_book = ConvertToBook(
    script_file=os.path.join(books_dir, '..', 'metrics', 'account_created_mac.py'),
    book_title='User Retention using account.created events DEVELOPMENT Mac',
    book_target_path=os.path.join(books_dir, '..', 'ipynb', 'dev'),
    event_storage=dev_event_path
)

dev_book.write_book()

prod_book = ConvertToBook(
    script_file=os.path.join(books_dir, '..', 'metrics', 'account_created_mac.py'),
    book_title='User Retention using account.created events Mac',
    book_target_path=os.path.join(books_dir, '..', 'ipynb', 'prod'),
    event_storage=prod_event_path
)

prod_book.write_book()


# Windows

dev_book = ConvertToBook(
    script_file=os.path.join(books_dir, '..', 'metrics', 'account_created_windows.py'),
    book_title='User Retention using account.created events DEVELOPMENT Windows',
    book_target_path=os.path.join(books_dir, '..', 'ipynb', 'dev'),
    event_storage=dev_event_path
)

dev_book.write_book()

prod_book = ConvertToBook(
    script_file=os.path.join(books_dir, '..', 'metrics', 'account_created_windows.py'),
    book_title='User Retention using account.created events Windows',
    book_target_path=os.path.join(books_dir, '..', 'ipynb', 'prod'),
    event_storage=prod_event_path
)

prod_book.write_book()

