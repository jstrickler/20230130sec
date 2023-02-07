# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 13:10:59 2023

@author: jstrick
"""

"""
Search file for weighted words and report their score.
"""
import re
import csv
import sys
import os

weights = {
    r'white\s+rabbit': 10,
    r'mock turtle': -10,
    r'father william': 30,
    r'beautiful soup': 40,
    r'bird': 5,
    r'virginia': 8,
    r'from': 1,
}

# path to folder containing files to process
# should probably be absolute path:  "C:/what/ever" or "//what/ever"
FOLDER = r"c:\Users\jstrick\Desktop\20230130sec\howard_files"   # could be  "c:/foo/bar/mydata"

# for PDF files, need to extract text with 
# https://pypi.org/project/PyPDF2/
# rather than opening as text files

with open('scored_words.csv', 'w') as scored_out:
    wtr = csv.writer(scored_out, lineterminator="\n")

    print("File                          Pattern                 Count  Weight     Score")
    print("------------------------------------------------------------------------------")

    files_in_folder = os.listdir(FOLDER)    
    
    for file_name in files_in_folder:
        # if not file_name.endswith('.txt'):
        #     continue
        file_path = os.path.join(FOLDER, file_name)
        # if ext is pdf
        #   all_text = parse_pdf(file_path)
        # elif ext is txt
        #   all_text = read_text()
        
        with open(file_path) as file_in:
            try:
                all_text = file_in.read()
            except Exception as err:
                print(err)
                file_in.close()
                continue
            for pattern, weight in weights.items():
                found = re.findall(pattern, all_text, re.I)
                word_count = len(found)
                word_score = word_count * weights[pattern]
                print(f"{file_name:30} {pattern:25.25s} {word_count:3d}     {weight:3d}    {word_score:6d}")
                wtr.writerow([file_name, pattern, word_count, weight, word_score])

