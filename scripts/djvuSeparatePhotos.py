# This script uses djvmcvt to unbundle the PHOTOS, generating one djvu file per page.

import os

PHOTOS = '../djv/PHOTOS.djvu'
# tmp folder of DjVu Imager
tmp = 'C:/SOFT/DjVu Imager/tmp/images/'
index = tmp + 'index.djvu'

# Create folder if it doesn't exist.
os.makedirs(tmp, exist_ok=True)

# Call djvmcvt to create indirect djvu with index file index.djvu.
os.system('djvmcvt -i ' + PHOTOS + ' "' + tmp + '" "' + index + '"')