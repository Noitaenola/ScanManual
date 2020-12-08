"""
Insert hyperlink in djvu file at set location.
"""

import os

SCAN = "../djv/SCAN_INS_OCR_BOOK_PAG.djvu"
SCAN_HYP = "../djv/SCAN_INS_OCR_BOOK_PAG_HYP.djvu"
hyperlink = "hyperlink.dsed"

# Delete old files (if they exist).
if os.path.isfile(SCAN_HYP):
    os.remove(SCAN_HYP)

if os.path.isfile(hyperlink):
    os.remove(hyperlink)

# Define the rectangle region for the hyperlink according to the
# following rules: in the djvu file the (x,y) = (0,0) is at the LOWER
# LEFT corner. (This is different from the majority of image editors,
# wehere (x,y) = (0,0) is generally at the upper left corner.) The
# rectangle is specified as: rect x0 y0 dx dy.
x0 = 278
y0 = 209
dx = 365
dy = 341

with open(hyperlink, "w") as outputFile:
    print('select "SCAN_001.djvu" # page 1', file=outputFile)
    print("set-ant", file=outputFile)
    print(
        '(maparea (url "http://gen.lib.rus.ec/" "_blank" ) "Ex libris '
        'Noitaenola." (rect '
        + str(x0)
        + " "
        + str(y0)
        + " "
        + str(dx)
        + " "
        + str(dy)
        + " ) (border #000000))",
        file=outputFile,
    )
    print(".", file=outputFile)
    print("save-bundled " + SCAN_HYP, file=outputFile)

# Finally, call djvused on the corrected script.
os.system("djvused " + SCAN + " -f " + hyperlink)
