import os
from base64 import encodestring
import nbformat as nbf
import codecs

from nbformat.v4.nbbase import (
    new_code_cell, new_markdown_cell, new_notebook,
    new_output, new_raw_cell
)

myFile = open('../scripts/retention_events_signed.py', 'r')
fileContent = myFile.read()

# some random base64-encoded *text*
png = encodestring(os.urandom(5)).decode('ascii')
jpeg = encodestring(os.urandom(6)).decode('ascii')

cells = []
cells.append(new_markdown_cell(
    source='Some NumPy Examples',
))

cells.append(new_code_cell(
    source=fileContent,
    execution_count=1,
))

nb0 = new_notebook(cells=cells,
    metadata={
        'language': 'python',
    }
)

f = codecs.open('test.ipynb', encoding='utf-8', mode='w')
nbf.write(nb0, f, 4)
f.close()