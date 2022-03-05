#! /usr/bin/python
#
# morph.py
#
# Usage:
#     module for madlib.py
#
# Apply morphology to words
#

import sys
import os
import re

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

num_lines = 0
while True:
    num_lines += 1
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

num_lines = 0
while True:
    num_lines += 1
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

num_lines = 0
while True:
    num_lines += 1
    line = file_handle.readline()
    if not line:
        # at end of file
        break
    irreg_artcls.append(line[:-1])
#print(f"Words with irregular articles: {irreg_artcls}\n")

#sys.exit()

# Spelling rule patterns
y_vowel = re.compile("[bcdfghjklmnpqrstvwxyz]y$")
short_vowel = re.compile("[bcdfghjklmnpqrstvwxyz][aeiou][mpbntdg]$")

# Morphology functions
def pl(noun):
    yv = y_vowel.findall(noun)
    #print(yv)
    if noun in irreg_nouns:
        plural = irreg_nouns[noun]
        return plural
    elif yv:
        plural = noun[:-1] + 'ies'
        return plural
    elif noun.endswith(('s', 'z', 'sh', 'ch', 'o')):
        plural = noun + 'es'
        return plural
    else:
        plural = noun + 's'
        return plural

def past(verb):
    yv = y_vowel.findall(verb)
    sv = short_vowel.findall(verb)
    if verb in irreg_verbs:
        past = irreg_verbs[verb]['past']
        return past
    elif yv:
        past = verb[:-1] + 'ied'
        return past
    elif sv:
        past = verb + verb[-1] + 'ed'
        return past
    elif verb.endswith('e'):
        past = verb[:-1] + 'd'
        return past
    else:
        past = verb + 'ed'
        return past

def part(verb):
    yv = y_vowel.findall(verb)
    sv = short_vowel.findall(verb)
    if verb in irreg_verbs:
        part = irreg_verbs[verb]['part']
        return part
    elif yv:
        part = verb[:-1] + 'ied'
        return part
    elif sv:
        past = verb + verb[-1] + 'ed'
        return past
    elif verb.endswith('e'):
        part = verb + 'd'
        return part
    else:
        part = verb + 'ed'
        return part

def prog(verb):
    sv = short_vowel.findall(verb)
    if verb in irreg_verbs:
        prog = irreg_verbs[verb]['prog']
        return prog
    elif verb.endswith('e'):
        prog = verb[:-1] + 'ing'
        return prog
    elif sv:
        prog = verb + verb[-1] + 'ing'
        return prog
    else:
        prog = verb + 'ing'
        return prog

def pres(verb):
    yv = y_vowel.findall(verb)
    if verb in irreg_verbs:
        pres = irreg_verbs[verb]['pres']
        return pres
    elif yv:
        pres = verb[:-1] + 'ies'
        return pres
    elif verb.endswith(('s', 'z', 'sh', 'ch', 'o')):
        pres = verb + 'es'
        return pres
    else:
        pres = verb + 's'
        return pres

