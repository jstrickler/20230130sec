import os

START_DIR = "EXAMPLES"
MIN_SIZE = 1024

for folder, subfolders, files in os.walk(START_DIR):
    # print(folder)
    for file_name in files:
        file_path = os.path.join(folder, file_name)
        abs_path = os.path.abspath(file_path)
        file_size = os.path.getsize(file_path)
        if file_size >= MIN_SIZE:
            print(f"{file_size:5d} {abs_path}")
