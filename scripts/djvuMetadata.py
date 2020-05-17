# This script uses djvused to insert the metadata in the djvu file.

import os

SCAN = '../djv/SCAN_INS_OCR_BOOK_PAG_HYP.djvu'
SCAN_MET = '../djv/SCAN_INS_OCR_BOOK_PAG_HYP_MET.djvu'
djvuMetadata = 'djvuMetadata.dsed'

# Delete old files (if they exist).
if os.path.isfile(SCAN_MET):
	os.remove(SCAN_MET)
if os.path.isfile(djvuMetadata):
	os.remove(djvuMetadata)

# Define metadata fields
fields=['author B.A. Gregory',
	'title An Introduction to Electrical Instrumentation and Measurement Systems',
	'subtitle A guide to the use, selection, and limitations of electrical instruments and measurement systems',
	'publisher Halsted Press; John Wiley & Sons',
	'year 1981',
	'edition 2',
	'series ',
	'isbn 0470270926',
	'isbn13 9780470270929',
	'note Ex libris Noitaenola',
	'url http://gen.lib.rus.ec/']

# Create the script.
with open(djvuMetadata, 'w') as outputFile:
	print('select', file=outputFile)
	print('set-meta', file=outputFile)
	for x in fields:
		print(x, file=outputFile)
	print('.', file=outputFile)
	print('save-bundled ' + SCAN_MET, file=outputFile)

# Call djvused on the generated script to save the metadata.
os.system('djvused ' + SCAN + ' -f ' + djvuMetadata)