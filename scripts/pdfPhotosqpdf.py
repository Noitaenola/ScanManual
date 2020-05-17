# This script pastes the separated photos in the PDF.

import os, shutil, glob, re

backgroundDir = '../SCAN/out/background/'
SCAN = '../djv/SCAN.pdf'
SCAN_INS = '../djv/SCAN_INS.pdf'
TEMP = '../djv/TEMP.pdf'

# Create new SCAN_INS.pdf to work with (eventually overwriting the old one).
shutil.copy(SCAN, SCAN_INS)

namesList = [os.path.basename(x) for x in glob.glob(backgroundDir + '*.tif')];

for filename in namesList:
	# Call ImageMagick to create the transparent-white pdf of the page.
	os.system('magick convert ' + backgroundDir + filename + ' -resample 300 -transparent white -compress jpeg -quality 40 ' + backgroundDir + filename + '.pdf')
	print(filename + '.pdf created!')
	# Call qpdf to paste that pdf in the corresponding page of SCAN_INS, but save it as TEMP (can't specify the same file as both the input and the output, thus the need for TEMP).
	os.system('qpdf --overlay ' + backgroundDir + filename + '.pdf --from=1 --to=' + re.search(r'\d+', filename).group(0) + ' -- ' + SCAN_INS + ' ' + TEMP)
	# Make TEMP the new SCAN_INS and delete the old TEMP and pdf files.
	shutil.copy(TEMP, SCAN_INS)
	os.remove(TEMP)
	os.remove(backgroundDir + filename + '.pdf')
	print(filename + '.pdf inserted!')