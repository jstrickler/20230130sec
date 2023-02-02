"""
Search file for weighted words and report their score.
"""
import re
import csv
import sys

weights = {
    r'white\s+rabbit': 10,
    r'mock turtle': 20,
    r'father william': 30,
    r'beautiful soup': 40,
    r'bird': 5,
    r'virginia': 8,
    r'from': 1,
}

with open('scored_words.csv', 'w') as scored_out:
    print("File                          Pattern                 Count  Weight     Score")
    print("------------------------------------------------------------------------------")
    for file_path in sys.argv[1:]:
        with open(file_path) as file_in:
            wtr = csv.writer(scored_out, lineterminator="\n")
            all_text = file_in.read()
            for pattern, weight in weights.items():
                found = re.findall(pattern, all_text, re.I)
                word_count = len(found)
                word_score = word_count * weights[pattern]
                if word_score > 0:
                    print(f"{file_path:30} {pattern:25.25s} {word_count:3d}     {weight:3d}    {word_score:6d}")
                wtr.writerow([file_path, pattern, word_count, weight, word_score])

