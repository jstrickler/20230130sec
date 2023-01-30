
set1 = {'red', 'blue', 'green', 'purple', 'green'}  # create literal set
set2 = {'green', 'blue', 'yellow', 'orange'}

set1.add('taupe')  # add element to set (ignored if already in set)

print(set1)
print(set2)
print(set1 & set2)  # intersection of two sets
print(set1 | set2)  # union of two sets
print(set1 ^ set2)  # XOR (symmetric difference); items in one set but not both
print(set1 - set2)  # Remove items in right set from left set
print(set2 - set1)
print()

food = 'spam ham ham spam spam spam ham spam spam eggs cheese spam'.split()
food_set = set(food)  # Create set from iterable (e.g., list)
print(food_set)
