# This script replaces a B&W page in an ABBYY FineReader 14 project with a new one from the out folder.

import os, shutil

print('Which page should I replace?')
page = input()

oldFile = '../ABBYY/' + page.zfill(4) + '/Image/bwPage.frdat'
newFile = '../SCAN/out/SCAN_' + page.zfill(3) + '.tif'

# Copy (and overwrite) the new file.
shutil.copy(newFile, oldFile)