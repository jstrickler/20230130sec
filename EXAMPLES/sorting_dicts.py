
count_of = dict(red=5, green=18, blue=1, pink=0, grey=27, yellow=5)

# sort by key
for color, num in sorted(count_of.items()):  # No special sort needed to sort by key
    print(color, num)

print()

# sort by value
for color, num in sorted(count_of.items(), key=lambda e: e[1]): # Sorting by value uses second element of nested (key, value) pairs returned by items()
    print(color, num)
