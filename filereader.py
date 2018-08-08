# Import the module
from docx import *

# Open the .docx file
document = opendocx('07-001 Comu Tortugas MArinas.docx')

# Search returns true if found
print(search(document,'Environment'))
