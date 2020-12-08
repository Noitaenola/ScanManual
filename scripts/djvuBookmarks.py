"""
Insert the bookmarks from bookmarks.txt into the djvu file.
"""

import os, re, shutil

SCAN = "../djv/SCAN_INS_OCR.djvu"
SCAN_BOOK = "../djv/SCAN_INS_OCR_BOOK.djvu"
bookmarks = "bookmarks.txt"
djvuBookmarks = "djvuBookmarks.dsed"
temp = "temp.tmp"

# Delete old files (if they exist).
if os.path.isfile(SCAN_BOOK):
    os.remove(SCAN_BOOK)
if os.path.isfile(djvuBookmarks):
    os.remove(djvuBookmarks)

# Replace last TAB in each line by a space (required by bookm).
with open(bookmarks, "r") as outputFile:
    content = outputFile.read()
    content = re.sub(r"(.+)\t(\d+)", r"\1 \2", content, flags=re.M)
with open(djvuBookmarks, "w") as outputFile:
    outputFile.write(content)

# Call bookm to generate djvused bookmark script.
os.system("bookm " + djvuBookmarks + " " + temp)
shutil.copy(temp, djvuBookmarks)
os.remove(temp)

# Add set-outline to the beggining. Add . and save-bundled to the end.
with open(djvuBookmarks, "r") as outputFile:
    content = outputFile.read()
with open(djvuBookmarks, "w") as outputFile:
    print("set-outline", file=outputFile)
    outputFile.write(content)
    print(".", file=outputFile)
    print("save-bundled " + SCAN_BOOK, file=outputFile)

# Call djvused on the bookmarking script.
os.system("djvused " + SCAN + " -f " + djvuBookmarks)
