"""
Rotate odd- or even-named files from the SCAN directory by 180 degrees.
"""

import os, glob

pages = []
oddEven = input("Rotate odd or even pages? -> ").lower()

if oddEven == "odd":  # odd pages
    pages = [os.path.basename(x) for x in glob.glob("../SCAN/*[13579].tif")]
elif oddEven == "even":  # even pages
    pages = [os.path.basename(x) for x in glob.glob("../SCAN/*[02468].tif")]
else:
    print("Wrong option! Try again.")

for x in pages:
    os.system("mogrify -compress LZW -rotate 180 " + x)
    print(x + " rotated!")
