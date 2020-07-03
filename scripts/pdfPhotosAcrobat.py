# This script generates an new Adobe JavaScript script that will be applied with Acrobat to paste the separated photos in the PDF.

import os, re, glob

backgroundDir = '../SCAN/out/background/'
insertPhotos = 'PdfPhotos.js'
SCAN_INS = '../djv/SCAN_INS.pdf'

# Delete old file (if it exists).
if os.path.isfile(insertPhotos):
	os.remove(insertPhotos)

namesList = [os.path.basename(x) for x in glob.glob(backgroundDir + '*.tif')]

with open(insertPhotos, 'w') as outputFile:
	for filename in namesList:
		# Call ImageMagick to create the transparent-white pdf of the page.
		os.system('magick convert ' + backgroundDir + filename + ' -transparent white -resample 300 -compress jpeg -quality 40 ' + backgroundDir + filename + '.pdf')
		print(filename + '.pdf created!')
		# Save the correspinding line to the script.
		print('this.addWatermarkFromFile({cDIPath: "/C/Project/SCAN/out/background/' + filename + '.pdf", nSourcePage: 0, nStart:', str(int(re.search(r'\d+', filename).group(0))-1) + '});', file=outputFile)
	print('this.saveAs("' + SCAN_INS + '");', file=outputFile)
