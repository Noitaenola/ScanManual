# File djvuOCR.dsed is the core of the whole operation. It does not only contain the OCR information, but it's also a script for djvused to run. This Python script creates that script, makes some modifications to it and then calls djvused to apply it, generating an OCRed djvu.

import os, re

OCR = '../djv/OCR.djvu'
SCAN = '../djv/SCAN_INS.djvu'
SCAN_OCR = '../djv/SCAN_INS_OCR.djvu'
djvuOCR = 'djvuOCR.dsed'

# Delete old files (if they exist).
if os.path.isfile(SCAN_OCR):
	os.remove(SCAN_OCR)

if os.path.isfile(djvuOCR):
	os.remove(djvuOCR)

# Call djvused to generate a text file (the script) with the OCR information from OCR.djvu. We accomplish this by using the ">" symbol in the command line, which outputs everything to a file. There are certainly more pythonic ways to get it done.
os.system('djvused ' + OCR + ' -e output-txt > ' + djvuOCR)


with open(djvuOCR, 'r') as outputFile:
	content = outputFile.read()

	# First, replace lines:
	# select "page0001.djvu" # page X
	# with:
	# select X
	content = re.sub(r'"page\d+\.djvu\" # page ', '', content, flags = re.M)

	# Now, delete many lines corresponding to spurious space characters. The result of not doing it can be seen by selecting text from the ABBYY-created OCR.djvu. Since DjVu viewers automatically introduce a space in between words, copying text with some viewers will result un doubly spaced words. Besides, I find it more pleasing to the eye this way.
	content = re.sub(r' \(char \d+ \d+ \d+ \d+ " "\)\n', '', content, flags = re.M)

with open(djvuOCR, 'w') as outputFile:
	outputFile.write(content)
	# Append the line "save-bundled" to the end of the script. This line makes djvused save the file as SCAN_OCR.djvu when it reads the script.
	print('save-bundled ' + SCAN_OCR, file=outputFile)

# Finally, call djvused on the corrected script.
os.system('djvused ' + SCAN + ' -f ' + djvuOCR)