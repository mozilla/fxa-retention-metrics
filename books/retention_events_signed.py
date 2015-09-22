from tools.convert_to_book import ConvertToBook

book = ConvertToBook(
    script_file='../metrics/retention_events_signed.py',
    book_title='User Retention using accounts.signed events',
    book_target_path='../ipynb'
)

book.write_book()
