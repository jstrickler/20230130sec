import re
import sys
import os

# invocation:
# python pygrep.py bird  DATA/*.txt
# python pygrep.py PATTERN list-of-file-paths ...

pattern = sys.argv[1]

rx = re.compile(pattern)

for file_path in sys.argv[2:]:
    file_name = os.path.basename(file_path)
    with open(file_path) as file_in:
        for raw_line in file_in:
            if rx.search(raw_line):
                line = raw_line.rstrip()
                print(f"{file_name}: {line}")

