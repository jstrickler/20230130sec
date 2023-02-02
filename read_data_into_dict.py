from pprint import pprint

knight_data = {}
with  open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        if quest == '':
            quest = None
        knight_data[name] = (title, color, quest, comment)

pprint(knight_data)
print('-' * 60)
for knight, data in knight_data.items():
    print(data[0], knight)
print()
