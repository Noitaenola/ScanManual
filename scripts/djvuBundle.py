# This script inserts the body of the djvu file between the covers, starting at page startPage.

import os, shutil

SCAN = '../djv/SCAN.djvu'
BODY = '../djv/BODY.djvu'
COVERS = '../djv/COVERS.djvu'

# First page after the front cover.
startPage = '2'

# Delete old file (if it exists).
if os.path.isfile(SCAN):
	os.remove(SCAN)

shutil.copy(COVERS, SCAN)

# Call djvm to insert BODY in between the covers.
os.system('djvm -i ' + SCAN + ' ' + BODY + ' ' + startPage)