
fruit = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon", "Kiwi", "ORANGE",
         "lime", "Watermelon", "guava", "papaya", "FIG", "pear", "banana", "Tamarind",
         "persimmon", "elderberry", "peach", "BLUEberry", "lychee", "grape"
         ]

fruit.sort(key=str.lower)  # List is sorted in place; cannot be undone

print(" ".join(fruit))
