# This script uses djvused to generate the page labels for the djvu file.

import os

SCAN = '../djv/SCAN_INS_OCR_BOOK.djvu'
SCAN_PAG = '..\djv\SCAN_INS_OCR_BOOK_PAG.djvu'
djvuPageLabels = 'djvuPageLabels.dsed'

# Delete old files (if they exist).
if os.path.isfile(SCAN_PAG):
	os.remove(SCAN_PAG)
if os.path.isfile(djvuPageLabels):
	os.remove(djvuPageLabels)

# Define the page labels for the different parts.
frontMatter = ['Cover', 'FFEP']#, 'FFEP2', 'FFEP3']
romans = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x']#, 'xi', 'xii', 'xiii', 'xiv', 'xv', 'xvi', 'xvii', 'xviii', 'xix', 'xx', 'xxi', 'xxii', 'xxiii', 'xxiv', 'xxv', 'xxvi', 'xxvii', 'xxviii', 'xxix', 'xxx']
backMatter = ['RFEP', '"Back cover"', 'Spine']

# Total number of pages in the book.
total = 461;

# Calculate some indices.
fmlen = len(frontMatter) + len(romans);
pPages = total - fmlen - len(backMatter);
lastpPage = total - len(backMatter);

# Generate the script and save it.
with open(djvuPageLabels, 'w') as outputFile:
	for p, title in enumerate(frontMatter+romans, start=1):
		print('select', p, file=outputFile)
		print('set-page-title', title, file=outputFile)

	for p in range(1, pPages+1):
		print('select', p+fmlen, file=outputFile)
		print('set-page-title', p, file=outputFile)

	for p, title in enumerate(backMatter, start=lastpPage+1):
		print('select', p, file=outputFile)
		print('set-page-title', title, file=outputFile)

	print('save-bundled ' + SCAN_PAG, file=outputFile)

# Call djvused on the created script.
os.system('djvused ' + SCAN + ' -f ' + djvuPageLabels)