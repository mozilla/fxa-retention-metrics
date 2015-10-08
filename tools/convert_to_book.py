import os
import nbformat as nbf
import codecs
from nbformat.v4.nbbase import (new_code_cell, new_markdown_cell, new_notebook)

tools_dir = os.path.dirname(os.path.abspath(__file__))
WEEK_RANGE_SCRIPT = os.path.join(tools_dir, '..', 'ipynb_generators', 'parts', 'weeks.py')
GRAPH_SCRIPT = os.path.join(tools_dir, '..', 'ipynb_generators', 'parts', 'graph.py')

class ConvertToBook:
    """
    This class takes Python (script_file)s and converts them to .ipynb notebooks

    This isolates the scripts for development and testing purposes
    """
    def __init__(self, script_file, book_target_path, graph_specs, event_storage, matplotlib=True):
        self.script_file = script_file
        self.book_target_path = book_target_path
        self.matplotlib = matplotlib
        self.graph_specs = graph_specs
        self.event_storage = event_storage

    def write_book(self):
        specs = self.graph_specs
        # heading
        cells = [new_markdown_cell(source=self.graph_specs["TITLE"])]

        if self.matplotlib:
            # enable matplotlib IPython magic that inlines plots
            cells.append(new_code_cell(source='%matplotlib inline', execution_count=1))

        # add query
        if specs["COHORT_QUERY"]:
            cells.append(new_code_cell(source="COHORT_QUERY = \"" + specs["COHORT_QUERY"] + "\"", execution_count=1))

        if specs["REST_QUERY"]:
            cells.append(new_code_cell(source="REST_QUERY = \"" + specs["REST_QUERY"] + "\"", execution_count=1))

        if specs["TITLE"]:
            cells.append(new_code_cell(source="TITLE = \"" + specs["TITLE"] + "\"", execution_count=1))

        if specs["TITLE"]:
            cells.append(new_code_cell(source="EVENT_STORAGE = \"" + self.event_storage + "\"", execution_count=1))

        # setup week ranges
        cells.append(new_code_cell(source=self.get_source(WEEK_RANGE_SCRIPT), execution_count=1))

        # append the script file to the .ipynb book
        cells.append(new_code_cell(source=self.get_source(self.script_file), execution_count=1))

        # setup graphs
        cells.append(new_code_cell(source=self.get_source(GRAPH_SCRIPT), execution_count=1))

        # code below to save the book
        nb0 = new_notebook(cells=cells, metadata={'language': 'python'})
        file_name = self.graph_specs["FILE_NAME"] + '.ipynb'
        book_file_path = os.path.join(self.book_target_path, file_name)
        f = codecs.open(book_file_path, encoding='utf-8', mode='w')
        nbf.write(nb0, f, 4)
        f.close()

    def get_source(self, script):
        script_file_source = open(script, 'r')
        return script_file_source.read()

