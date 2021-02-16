"""
Insert the bookmarks from bookmarks.txt into the djvu file.
"""

import os

SCAN = "../djv/SCAN_INS_OCR.djvu"
SCAN_BOOK = "../djv/SCAN_INS_OCR_BOOK.djvu"
bookmarks = "bookmarks.txt"
djvuBookmarks = "djvuBookmarks.dsed"


def split_tabs(line):
    tab_num = 0
    for c in line:
        if c == "\t":
            tab_num += 1
        else:
            break
    return tab_num, line[tab_num:]


def prepare_entry(line):
    line, number = line.rsplit("\t", 1)  # split page number
    line = f'"{line}" "#{number}"'  # wrap in quotation marks
    line = "".join(["(", line])  # add left parenthesis
    return line


# delete old files (if they exist)
if os.path.isfile(SCAN_BOOK):
    os.remove(SCAN_BOOK)
if os.path.isfile(djvuBookmarks):
    os.remove(djvuBookmarks)

# read contents
with open(bookmarks, "r") as inputFile:
    input_lines = inputFile.readlines()

output = []

previous_depth = -1
open_parens = 0

# generate output contents
for line in input_lines:
    if not line.strip():  # skip empty lines
        continue

    current_depth, line = split_tabs(line.rstrip())

    if current_depth <= previous_depth:
        for n in range(previous_depth - current_depth + 1):  # add closing parenthesis
            open_parens -= 1
            output.append("\t" * open_parens + ")")

    output.append("\t" * open_parens + prepare_entry(line))
    open_parens += 1

    previous_depth = current_depth  # update previous_depth

for n in range(open_parens):  # close remaining open parenthesis
    open_parens -= 1
    output.append("".join(["\t" * open_parens + ")"]))

with open(djvuBookmarks, "w") as outputFile:  # save output script
    print("set-outline\n(bookmarks", file=outputFile)
    for line in output:
        print(line, file=outputFile)
    print(")\n.", file=outputFile)
    print("save-bundled " + SCAN_BOOK, file=outputFile)

# Call djvused on the bookmarking script.
os.system("djvused " + SCAN + " -f " + djvuBookmarks)
