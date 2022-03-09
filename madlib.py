#! /usr/bin/python
#
# madlib.py
#
# Usage:
#     madlib.py --option
#
# Given user input: replaces words in stories to produces madlibs
#

import re
import sys
import optparse
import random
import os
import morphology.morph as morph

# Get list of current stories
path = "./stories/"
filenames = os.listdir(path)
list(filenames)

stories = []

for f in filenames:
    if f.endswith('.py'):
        keyword = f.replace('.py', '')
        stories.append(keyword)

## Choose to sort stories alphabetically
#stories.sort()

stories_help = str(stories)

## Change format of stories in help message
stories_help = stories_help.replace("'", '')
#stories_help = stories_help.replace('[', '')
#stories_help = stories_help.replace(']', '')


# Parse the options
parser = optparse.OptionParser()
parser.add_option("-r", "--random",
                  action="store_true", dest="select_random", default=False,
                  help="pick a random story to madlib")
parser.add_option("-s", "--story", dest="select_story",
                  help="pick specific story to madlib by name. current stories: {}".format(stories_help), 
                  metavar="STORY")
(options, args) = parser.parse_args()

# instructions
instructions = """                        _____ __                 
   ____ ___  ____ _____/ / (_) /_    ____  __  __
  / __ `__ \/ __ `/ __  / / / __ \  / __ \/ / / /
 / / / / / / /_/ / /_/ / / / /_/ / / /_/ / /_/ / 
/_/ /_/ /_/\__,_/\__,_/_/_/_.___(_) .___/\__, /  
                                 /_/    /____/   

Welcome to madlib.py, the free open-source offline madlib generator!

Instructions:
  To see a random madlib: `python3 madlib.py -r`
  To see a specific madlib: `python3 madlib.py -s [story name]`
  To see all your madlib options, including the names of current stories: `python3 madlib.py -h`
"""

import_story = 'from stories.{} import story'
cwd = os.getcwd()
# Compute the constraint (if any)
if options.select_random == True:
    exec(import_story.format(random.choice(stories)))
elif options.select_story:
    story_file = options.select_story
    try:
        exec(import_story.format(story_file))
    except ModuleNotFoundError:
        print(f" ERROR: Could not find '{cwd}/stories/{story_file}.py'")
        print("  Exiting madlib.py\n")
        sys.exit()
else:
    print(instructions)
    proceed = input("Continue to example? Y/n: ")
    yes = ["", "Y", "y"]
    if proceed in yes:
        exec(import_story.format("example"))
    else:
        print("  Exiting madlib.py\n")
        sys.exit()

# Create a list of templates
pattern = r"\{[-_a-zA-Z0-9]+=[_A-Za-z]+\}"
regex_program = re.compile(pattern)
templates = regex_program.findall(story)
#print(f" DEBUG: templates={templates}")
#print(len(templates))

# Create a list of unique templates (remove duplicates)
# while maintaining the template order
uniq_templates = []
cap_templates = []
for t in templates:
    if t.lower() not in uniq_templates:
        uniq_templates.append(t.lower())
    if t.lower() != t:
        cap_templates.append(t)
#print(f" DEBUG: uniq_templates={uniq_templates}")
total = len(uniq_templates)
#print(len(uniq_templates))
#print(f" DEBUG: cap_templates={cap_templates}")

# Create a dictionary of desciptions from the templates where:
#    key = full template string
#    value = description string with underscores replaced with spaces
replacements = {}
value_pattern = r"\{.*=(.*)\}"
for ut in uniq_templates:
    #print(f" DEBUG: uniq_template={ut}")
    v = re.search(value_pattern, ut)
    key = ut
    value = v.group(1)
    replacements[key] = value
#print(f" DEBUG: replacements={replacements}")

# For each element of uniq_templates: ask User for replacement phrase
# (e.g. the 'answer' to the prompt) and add it to a new dictionary
# using the original template as the key.
count = 0
for key in replacements:
    count += 1
    exec("from mssgs import {}_mssg".format(replacements[key]))
    exec("message = '[{} of {}]' + {}_mssg".format(str(count), str(total), replacements[key]))
    replacements[key] = input(message)
#print(f" DEBUG: new replacements={replacements}")

# Replace unique templates in story
for key,value in replacements.items():
    story = story.replace(key, value)
#print(" DEBUG: " + f"{story}")


# Get morphologically-complex word templates
morph_pattern = "\{[-_a-zA-Z0-9]+=[_A-Za-z]+\+[-_a-zA-Z0-9]+\}"
morph_program = re.compile(morph_pattern)
morph_templates = morph_program.findall(story)
#print(f"DEBUG: morphology templates={morph_templates}")
#print(len(morph_templates))

# Get list of unique morphologically-complex templates
uniq_morphs = []
for mt in morph_templates:
    if mt.lower() not in uniq_morphs:
        uniq_morphs.append(mt.lower())
    if mt.lower() != mt:
        cap_templates.append(mt)
#print(f" DEBUG: uniq_morphs={uniq_morphs}")

# Dict of morphology functions
morph_functs = {'pl':morph.pl, 'plural':morph.pl, 
                'past':morph.past, 'pres':morph.pres, 
                'prog':morph.prog, 'ing':morph.prog,
                'part':morph.part, 'perf':morph.part}
# Regex pattern for morphologically-complex templates
morph_value_pattern = r"\{.*=(.*)\+(.*)\}"
for um in uniq_morphs:
    v = re.search(morph_value_pattern, um)
    funct = v.group(2)
    word = v.group(1)
    key = um
    value = morph_functs[funct](word)
    replacements[key] = value
#print(f" DEBUG: replacements={replacements}")

# Create dictionary for capitalized keys
# for which the values are the 
# capitalized values of replacements
capitals = {}
for ct in cap_templates:
    sibling = ct.lower()
    key = ct
    value = replacements[sibling][0].upper() + replacements[sibling][1:]
    capitals[key] = value
#print(f" DEBUG: capitals={capitals}")

# Second round of template replacement in story
for key,value in replacements.items():
    story = story.replace(key, value)
for key,value in capitals.items():
    story = story.replace(key, value)

# Replace 'a(n)' with 'a' or 'an' appropriately
an_pattern = re.compile("a\(n\) [-_a-zA-Z0-9]+")
artcl_word_combos = an_pattern.findall(story)
uniq_artcl_word_combos = []
for combo in artcl_word_combos:
    if combo not in uniq_artcl_word_combos:
        uniq_artcl_word_combos.append(combo)

for combo in uniq_artcl_word_combos:
    article_and_following_word = combo
    following_word_pattern = r"a\(n\) ([-_a-zA-Z0-9]+)"
    a = re.search(following_word_pattern, combo)
    following_word = a.group(1)
    
    if following_word.upper() == following_word:
    # if the following word is an acronym
        if following_word[0] in 'AEFHILMNORSX':
        # if the acronym starts with a letter that starts with a vowel sound
            if following_word in morph.irreg_artcls:
            # if the acronym is in morphology/irreg_artcls because it
            # starts with a consonant and is read like a word
                replacement = 'a ' + following_word
                story = story.replace(article_and_following_word, replacement)
            else:
            # the acronym starts with a vowel sound
                replacement = 'an ' + following_word
                story = story.replace(article_and_following_word, replacement)
        else:
        # the acronym starts with letter that starts with a consonant sound
            replacement = 'a ' + following_word
            story = story.replace(article_and_following_word, replacement)
    
    elif following_word[0] in 'AaEeIiOoUu':
    # if the word is not an acronym and is spelled starting with a vowel
        if following_word in morph.irreg_artcls:
        # if the word is in morphology/irreg_artcls.text because it is 
        # pronounced like it starts with a consonant
            replacement = 'a ' + following_word
            story = story.replace(article_and_following_word, replacement)
        else:
        # the word starts with a vowel sound
            replacement = 'an ' + following_word
            story = story.replace(article_and_following_word, replacement)
    
    else:
    # the word is not an acronym and is spelled starting with a consonant
        if following_word in morph.irreg_artcls:
        # if the word is in morphology/irreg_artcls.txt because it 
        # starts with a silent 'h'
            replacement = 'an ' + following_word
            story = story.replace(article_and_following_word, replacement)
        else:
        # the word starts with a consonant sound
            replacement = 'a ' + following_word
            story = story.replace(article_and_following_word, replacement)

# Print the story
print(story)

# BONUS Bell or whistle:
# reformat the paragraphs of the story to have max line length
# Note: there is a module named 'textwrap' that can help us here

