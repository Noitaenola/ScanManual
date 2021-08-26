"""
Rotate all the landscapePages by 90 degrees.
"""

import os

# fmt: off
landscapePages = [
    128, 161, 210, 213, 214, 224, 377, 379, 381, 382,
    384, 385, 386, 387, 388, 407, 435, 438, 439, 440,
]
# fmt: on

for x in landscapePages:
    os.system("mogrify -compress LZW -rotate 90 ../SCAN/out/SCAN_" + str(x) + ".tif")
    print("SCAN_" + str(x) + ".tif" + " rotated!")
