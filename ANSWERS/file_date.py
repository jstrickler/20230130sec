import sys
import os
from datetime import datetime as DateTime

for filename in sys.argv[1:]:
    mtime = os.path.getmtime(filename)
    file_date = DateTime.fromtimestamp(mtime)
    fmt_date = DateTime.strftime(file_date,'%b %d, %Y')
    print("{0:15s} {1}".format(filename, fmt_date))
