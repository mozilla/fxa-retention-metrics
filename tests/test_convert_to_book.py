import hashlib
import os, sys
sys.path.append(os.path.realpath(os.curdir))

from unittest import TestCase
from tools.convert_to_book import ConvertToBook

def fileMd5(full_path):
    return hashlib.md5(open(full_path, 'rb').read()).hexdigest()

class TestConvertToBook(TestCase):
    def test_init(self):
        fixture_file = './fixtures/script_file.py'
        expected_file = './expected/script_file.ipynb'

        try:
            os.remove('./out/script_file.ipynb')
        except OSError:
            pass

        b = ConvertToBook(
            script_file=fixture_file,
            book_title='Test Book',
            book_target_path='./out'
        )

        b.write_book()
        self.assertEqual(fileMd5(expected_file), fileMd5('./out/script_file.ipynb'))
