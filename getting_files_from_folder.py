from glob import glob
from os import listdir, scandir
from os.path import join

FOLDER = "DATA"

# scenario 1: file-name wildcards with glob()

wild_card = '*.txt'

glob_path = join(FOLDER, wild_card)
print(f"glob_path: {glob_path}")
all_files_glob = glob(glob_path)

print(f"all_files_glob: {all_files_glob}\n")

# scenario 2: selecting filenames with listdir() and a list comprehension

all_files_listdir = [join(FOLDER, f) for f in listdir(FOLDER) if f.endswith('.txt')]
print(f"all_files_listdir: {all_files_listdir}\n")

# scenario 3: selecting filenames with scandir() and a list comprehension
all_files_scandir = [join(FOLDER, f.name) for f in scandir(FOLDER) if f.name.endswith('.txt')]
print(f"all_files_scandir: {all_files_scandir}\n")

# scenario 4: selecting filenames with scandir() and a generator expression
all_files_scandir_gen = (join(FOLDER, f.name) for f in scandir(FOLDER) if f.name.endswith('.txt'))
print(f"all_files_scandir_gen: {all_files_scandir_gen}\n")
