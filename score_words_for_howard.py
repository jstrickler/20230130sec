"""
Search file for weighted words and report their score.
"""
import re

weights = {
    r'white\s+rabbit': 10,
    r'mock turtle': 20,
    r'father william': 30,
    r'beautiful soup': 40,
}

with open("DATA/alice.txt") as alice_in:
    all_text = alice_in.read()
    for pattern, weight in weights.items():
        found = re.findall(pattern, all_text, re.I)
        word_count = len(found)
        word_score = word_count * weights[pattern]
        print(f"{pattern} Word count: {word_count} Weight: {weight} Score: {word_score}")
