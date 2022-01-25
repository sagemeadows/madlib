#! /usr/bin/python
#
# god.py
#
# Usage:
#     module for madlib.py
#
# When imported by madlib.py: replaces words in story to produce madlib
#

import sys

talk_to_god = """
======================================================

How to Talk to {God}

Talking to {God} involves a very {spiritual}, {personal}, often {private}, relationship. With so many opinions about relating to {God}, figuring out how you should talk to {God} may seem complicated. But it doesn’t have to be. How you choose to connect and talk to {God} will simply boil down to what seems right to you. No matter your {spiritual} preference or {religion}, learning how to communicate effectively with {God} can be achieved with the following tips.

1. Determine how you see {God}.
You’ll need to determine who {God} is to you in order to confidently talk to {God}. Who is, and how do you define, {God}? Do you know {God} as a fatherly or motherly figure, a {teacher}, a distant -- or a close {friend}, sticking closer than a {sister} or {brother}? Or, is {God} an abstract {spiritual} guide? Is your connection to {God} rooted in a {personal}, {spiritual} relationship you have with {God}? Or, do you follow the form and order of your {religion} to understand who {God} is to you? Whichever is true for you will dictate how you view and talk to {God}. And, however you see {God} determines how you will approach {God} to talk to {God} as you see them.

2. Talk to {God} as you would a {close}, {loving} but {allpowerful} {friend}.
Talking to {God} as a tremendous {friend} is different from just praying to {God} as a need or duty. As with a {friend}, you expect back-and-forth communication by noticing how {God} answers, helps or teaches you. While prayer may be more of a one-way transaction, talking implies a conversation.

3. Have a talk with {God}.
Talk to {God} similarly as you would, if a {physical} {person} were standing in front of you. You can talk to {God} about your daily troubles, your thoughts at the moment, your hopes and dreams, and even tell them (and tell yourself) the things for which you’re {thankful}. You can tell {God} about {casual} or {hard} topics just as you would with a {concerned} {friend}.

4. Watch for and pay attention to possible feedback.
You may not get an audible response like you would, if a {friend} were physically standing in front of you. But you can receive a response from {God} in the written word of {God} or from the {sermon} of a {minister}. Anticipate it to also come in the form of a {intuition}, a {inspiration}, a {scripture}, a {situation} or an event that directly or indirectly relates to what you’ve been talking about to {God}.

~FIN~

======================================================

Story source: https://www.wikihow.com/Talk-to-God
Under an Attribution-Noncommercial-Share Alike 3.0 Creative Commons License, wikiHow's text content is free to modify, republish and share.
"""
talk_to_god = talk_to_god.format(God=input("[1 of 24] Enter a proper name: "), 
                                 spiritual=input("[2 of 24] Enter an adjective: "), 
                                 personal=input("[3 of 24] Enter an adjective: "), 
                                 private=input("[4 of 24] Enter an adjective: "), 
                                 religion=input("[5 of 24] Enter an abstract noun: "), 
                                 teacher=input("[6 of 24] Enter a kind of person or profession: "), 
                                 friend=input("[7 of 24] Enter a kind of person or profession: "), 
                                 sister=input("[8 of 24] Enter a kind of person or profession: "), 
                                 brother=input("[9 of 24] Enter a kind of person or profession: "), 
                                 close=input("[10 of 24] Enter an adjective: "), 
                                 loving=input("[11 of 24] Enter an adjective: "), 
                                 allpowerful=input("[12 of 24] Enter an adjective: "), 
                                 physical=input("[13 of 24] Enter an adjective: "), 
                                 person=input("[14 of 24] Enter a concrete noun: "), 
                                 thankful=input("[15 of 24] Enter an adjective: "), 
                                 casual=input("[16 of 24] Enter an adjective: "), 
                                 hard=input("[17 of 24] Enter an adjective: "), 
                                 concerned=input("[18 of 24] Enter an adjective: "), 
                                 sermon=input("[19 of 24] Enter an abstract noun: "), 
                                 minister=input("[20 of 24] Enter a kind of person or profession: "), 
                                 intuition=input("[21 of 24] Enter an abstract noun: "), 
                                 inspiration=input("[22 of 24] Enter an abstract noun: "), 
                                 scripture=input("[23 of 24] Enter a concrete noun: "), 
                                 situation=input("[24 of 24] Enter a concrete noun: "))
print(talk_to_god)

sys.exit()

