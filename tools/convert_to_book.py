import os
import nbformat as nbf
import codecs
from nbformat.v4.nbbase import (new_code_cell, new_markdown_cell, new_notebook)


class ConvertToBook:
    """
    This class takes Python (script_file)s and converts them to .ipynb notebooks

    This isolates the scripts for development and testing purposes
    """
    def __init__(self, script_file, book_target_path, book_title='Retention Metrics', matplotlib=True):
        self.script_file = script_file
        self.book_target_path = book_target_path
        self.book_title = book_title
        self.matplotlib = matplotlib

    def write_book(self):
        script_file_source = open(self.script_file, 'r')
        script_file_contents = script_file_source.read()

        cells = []
        cells.append(new_markdown_cell(source=self.book_title))

        if self.matplotlib:
            # enable matplotlib IPython magic that inlines plots
            cells.append(new_code_cell(source='%matplotlib inline', execution_count=1))

        # append the script file to the .ipynb book
        cells.append(new_code_cell(source=script_file_contents,execution_count=1))

        # code below to save the book
        nb0 = new_notebook(cells=cells, metadata={'language': 'python'})
        file_name = os.path.splitext(os.path.basename(self.script_file))[0] + '.ipynb'
        book_file_path = os.path.join(self.book_target_path, file_name)
        f = codecs.open(book_file_path, encoding='utf-8', mode='w')
        nbf.write(nb0, f, 4)
        f.close()
