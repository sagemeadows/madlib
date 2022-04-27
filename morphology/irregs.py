#! /usr/bin/python
#
# handle_files.py
#
# Usage:
#     module for morph.py
#
# Open and read files of irregular words.
#

import sys
import os

# Irregular word .txt file dictionaries
cwd = os.getcwd()
nouns_filename = f"{cwd}/morphology/irreg_nouns.txt"
verbs_filename = f"{cwd}/morphology/irreg_verbs.txt"
artcls_filename = f"{cwd}/morphology/irreg_artcls.txt"

# Open files and create python dictionaries

irreg_nouns = {}
try:
    file_handle = open(nouns_filename, 'r')
except:
    print(f" ERROR: Failed to open words file '{nouns_filename}'")
    print("  Exiting system from morphology/morph.py\n")
    sys.exit()

while True:
    line = file_handle.readline()
    if not line:
        # at end of file
        break
    # get rid of dashes
    line = line.replace('–', '')
    # split words in line
    words = line.split()
    irreg_nouns[words[0]] = words[1]
#print(f"Irregular nouns: {irreg_nouns}\n")


irreg_verbs = {}
try:
    file_handle = open(verbs_filename, 'r')
except:
    print(f" ERROR: Failed to open words file '{verbs_filename}'")
    print("  Exiting system from morphology/morph.py\n")
    sys.exit()

while True:
    line = file_handle.readline()
    if not line:
        # at end of file
        break
    # get rid of dashes
    line = line.replace('–', '')
    # split words in line
    words = line.split()
    irreg_verbs[words[0]] = {'past':words[1], 'part':words[2], 'prog':words[3], 'pres':words[4]}
#print(f"Irregular verbs: {irreg_verbs}\n")


irreg_artcls = []
try:
    file_handle = open(artcls_filename, 'r')
except:
    print(f" ERROR: Failed to open words file '{artcls_filename}'")
    print("  Exiting system from morphology/morph.py\n")
    sys.exit()

while True:
    line = file_handle.readline()
    if not line:
        # at end of file
        break
    irreg_artcls.append(line[:-1])
#print(f"Words with irregular articles: {irreg_artcls}\n")

