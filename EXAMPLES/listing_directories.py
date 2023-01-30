import os

DIRECTORY = '../DATA'

for i, entry_name in enumerate(os.listdir(DIRECTORY)):
    print(entry_name)
    if i == 9:
        break

print('-' * 60)

for i, entry in enumerate(os.scandir(DIRECTORY)):
    print("{:25s} {:6s} {:6s} {:6o}".format(entry.name, str(entry.is_dir()), str(entry.is_file()), entry.stat().st_mode))
    if i == 9:
        break
