from timeit import Timer

REPEATS = 100000

setup_code = """
from glob import glob
from os import listdir, scandir
from os.path import join

FOLDER = "DATA"
wild_card = '*.txt'
glob_path = join(FOLDER, wild_card)
"""

code_snippets = [
    """
all_files_glob = glob(glob_path)    
    """,
    """
all_files_listdir = [join(FOLDER, f) for f in listdir(FOLDER) if f.endswith('.txt')]    
    """,
    """
all_files_scandir = [join(FOLDER, f.name) for f in scandir(FOLDER) if f.name.endswith('.txt')]
    """,
]

for code_snippet in code_snippets:
    t = Timer(code_snippet, setup_code)
    print(code_snippet, flush=True)
    print(t.timeit(REPEATS), flush=True)
    print('-' * 60)
