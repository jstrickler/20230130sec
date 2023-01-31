list1 = list()
list2 = []

# 1. Bernard Madoff
# 3. Kenneth Lay
# 4. Robert Allen Stanford
# 6. Martin Frankel
# 7. Jeffery Skilling
# 8. David Blech
# 9. Sam Israel III
# 10. Raj Rajaratnam
# 'Al Capone', "Jeffrey Dahmer", "Bernie Madoff"
criminals = []

print(f"criminals: {criminals}")
criminals.append('Bernie Madoff')
print(f"criminals: {criminals}")
print(f"criminals[0]: {criminals[0]}")

# INVALID: rivers.append("Potomac")
# INVALID crimimals[3] = "Sam Israel III"
criminals.insert(0, "David Blech")
print(f"criminals: {criminals}")
criminals.insert(0, 'Al Capone')
criminals.append('Raj Rajaratnam')
print(f"criminals: {criminals}")
criminals.insert(3, "Jeffrey Skilling")
print(f"criminals: {criminals}")
more_bad_guys = ["Jeffrey Dahmer", "Kenneth Lay"]
criminals.extend(more_bad_guys)
print(f"criminals: {criminals}")
criminals.append(42)
criminals.append(88.9)
more_junk = ['spam', 50, "wombats"]
criminals.extend(more_junk)
print(f"criminals: {criminals}")
stuff = ['a', 'b', 'c']
criminals.append(stuff)
print(f"criminals: {criminals}")

# LIST.insert(pos, OBJ)  LIST.append(OBJ)  LIST.extend(iterable)

pos = criminals.index(88.9)
print(f"pos: {pos}")
del criminals[pos]
print(f"criminals: {criminals}")
criminals.remove(50)
criminals.remove('spam')
print(f"criminals: {criminals}")

item = criminals.pop()
print(f"item: {item}")
print(f"criminals: {criminals}")

# del LIST[pos]  LIST.remove(obj)   x = LIST.pop()  y = LIST.pop(pos)

item  = criminals.pop(1)
print(f"item: {item}")
print(f"criminals: {criminals}")

criminals.remove(42)
criminals.remove('wombats')

print(f"criminals: {criminals}")


bad_guy = criminals[1]
print(f"bad_guy: {bad_guy}")
print(f"criminals[5]: {criminals[5]}")
print(f"criminals[len(criminals)-1]: {criminals[len(criminals)-1]}")
print(f"criminals[-1]: {criminals[-1]}")

criminals.append("Martin Frankel")
print(f"criminals: {criminals}")

print(f"criminals[0:3]: {criminals[0:3]}")
print(f"criminals[2:4]: {criminals[2:4]}")
print(f"criminals[:3]: {criminals[:3]}")
print(f"criminals[5:]: {criminals[5:]}")
print(f"criminals[:]: {criminals[:]}")

criminals_copy = criminals[:]
criminals_copy = list(criminals)

s = "Securities and Exchange Commission"
print(f"s[10]: {s[:10]}")
print(f"s[15:23]: {s[15:23]}")
print('-' * 60)

for bad_guy in criminals:
    print(bad_guy)

print(criminals)
print()

x = "abc"
for c in x:
    print(c)
print()

y = ["abc"]
for c in y:
    print(c)
print()

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(f"c: {c}")

print(f"a * 5: {a * 5}")

flags = [None] * 25
print(f"flags: {flags}")

zeros = [0] * 10
print(f"zeros: {zeros}")

print(f"criminals: {criminals}")

for bad_guy in 'Jeffrey Skilling', 'Martin Frankel', 'Pretty Boy Floyd':
    print(bad_guy, bad_guy not in criminals)
print()

print(f"min(criminals): {min(criminals)}")
print(f"max(criminals): {max(criminals)}")
print(f"len(criminals): {len(criminals)}")
print(f"sorted(criminals): {sorted(criminals)}")

bad_guys_to_check = 'Jeffrey Skilling', 'Martin Frankel'
print(all(x in criminals for x in bad_guys_to_check))

words = ['dog', 'bites', 'man']
w = reversed(words)
print(f"words: {words}")
print(f"w: {w}")

for word in w:
    print(word)
print()

for i, criminal in enumerate(criminals):
    print(i, criminal)

print(f"list(enumerate(criminals)): {list(enumerate(criminals))}")















