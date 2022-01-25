#! /usr/bin/python
#
# madlib.py
#
# Usage:
#     madlib.py --option
#
# Given user input: replaces words in stories to produces madlibs
#

import sys
import optparse
import random
import os

# default story
def example():
    madlibs = """
======================================================

The History of Mad Libs

Mad Libs is a {phrasal} template {word} game. It consists of one {player} prompting others for a list of {words} to substitute for {blanks} in a story before reading aloud. The game is frequently played as a {party} game or as a pastime.

Mad Libs was invented in {_1953} by {Stern} and {Price}. {Stern} and {Price} created the game, but could not agree on a name for their invention. No name was chosen until {five} years later ({_1958}), when {Stern} and {Price} were eating {Eggs_Benedict} at a/n {restaurant} in {NYC}. While eating, the two overheard an argument at a neighboring table between a/n {agent} and a/n {actor}. According to {Price} and {Stern}, during the overheard argument, the {actor} said that they wanted to "ad-lib" an upcoming {interview}. The {agent}, who clearly disagreed with the {actor}'s suggestion, retorted that ad-libbing a/n {interview} would be "mad". {Stern} and {Price} used that eavesdropped conversation to create, at length, the name "Mad Libs". In {_1958}, the duo released the first book of Mad Libs, which resembled the earlier games of Consequences and {Exquisite} Corpse.

~FIN~

======================================================

Story source: Wikipedia (https://en.wikipedia.org/wiki/Mad_Libs), accessed 5 Jan 2022
"""
    madlibs = madlibs.format(phrasal=input("[1 of 18] Enter a noun: "), 
                             word=input("[2 of 18] Enter a noun: "), 
                             player=input("[3 of 18] Enter a kind of person or occupation: "), 
                             words=input("[4 of 18] Enter a plural noun: "), 
                             blanks=input("[5 of 18] Enter a plural noun: "), 
                             party=input("[6 of 18] Enter a noun: "), 
                             Stern=input("[7 of 18] Enter a proper name: "), 
                             Price=input("[8 of 18] Enter a proper name: "), 
                             _1953=input("[9 of 18] Enter a year: "), 
                             five=input("[10 of 18] Enter a number: "), 
                             _1958=input("[11 of 18] Enter the sum of the year and the number: "), 
                             Eggs_Benedict=input("[12 of 18] Enter a type of food: "), 
                             restaurant=input("[13 of 18] Enter a kind of business: "), 
                             NYC=input("[14 of 18] Enter a location (either a name, like 'Australia', or a description, like 'a store' or 'the park'): "), 
                             agent=input("[15 of 18] Enter a kind of person or occupation: "), 
                             actor=input("[16 of 18] Enter a kind of person or occupation: "), 
                             interview=input("[17 of 18] Enter a noun related to talking (e.g. 'conversation'): "), 
                             Exquisite=input("[18 of 18] Enter an adjective with capitalization: "))
    print(madlibs)

# get list of current stories
filenames = os.listdir()
list(filenames)

stories = []

for f in filenames:
    if f.endswith('.py'):
        keyword = f.replace('.py', '')
        stories.append(keyword)

stories.remove('madlib')
## choose to sort stories alphabetically
#stories.sort()

stories = str(stories)

## change format of stories in help message
stories = stories.replace("'", '')
#stories = stories.replace('[', '')
#stories = stories.replace(']', '')


# parse the options
parser = optparse.OptionParser()
parser.add_option("-r", "--random",
                  action="store_true", dest="select_random", default=False,
                  help="pick a random story to madlib")
parser.add_option("-s", "--story", dest="select_story",
                  help="pick specific story to madlib by name. current stories: {}".format(stories), 
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

# compute the constraint (if any)
if options.select_random == True:
    random.choice(list(stories.values()))()
elif options.select_story:
    story = options.select_story
    import_story = 'import {}'.format(story)
    #exec(import_story)
    try:
        exec(import_story)
    except ModuleNotFoundError:
        print("\nERROR: Could not find story '{}.py' in current directory".format(story))
        print("  Exiting madlib.py\n")
        sys.exit()
else:
    print(instructions)
    proceed = input("Continue to example? Y/n: ")
    yes = ["", "Y", "y"]
    if proceed in yes:
        example()
    else:
        print("  Exiting madlib.py\n")
        sys.exit()

