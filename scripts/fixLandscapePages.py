# This script rotates all the landscapePages by 180 degrees.

import os

landscapePages = [128, 161, 210, 213, 214, 224, 377, 379, 381, 382, 384, 385, 386, 387, 388, 407, 435, 438, 439, 440]

for x in landscapePages:
	os.system('mogrify -rotate 180 ../SCAN/out/SCAN_' + str(x) + '.tif')
	print('SCAN_' + str(x) + '.tif' + ' rotated!')