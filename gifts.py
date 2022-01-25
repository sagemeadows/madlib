#! /usr/bin/python
#
# gifts.py
#
# Usage:
#     module for madlib.py
#
# When imported by madlib.py: replaces words in story to produce madlib
#

import sys

gifts():
give_a_gift = """
======================================================

How to give a great {gift} to someone

It can be nerve-racking finding a great {gift} for someone. Finding a {gift} that the recipient will {enjoy} takes a bit of {direction}ward {thinking} and an understanding of the recipient's {personality} and {tastes}.

1. Consider how {close} you are to that person.
If you have a {close} relationship with the person, be it {intimate} or {platonic}, you may select a {gift} that is more {personal}. If you are not {close} to the person, you may choose a {gift} that is more useful or {accessible}.

2. Identify items the person may {need}.
Think about any items the person may {need} in their day-to-day life or a big {purchase} that the person needs to do but has been putting off. This could be a new {kitchen} appliance the person has been eyeing or a new {backpack} the person needs for a new year of {school}.

3. Arrange a {experience} as a {gift}.
Often, giving someone a {experience} can be more {impactful} than giving them a {item}. This could be a {couples} massage, a sky diving {date}, or dinner at the person’s favorite {restaurant}. Think of {experience}s that will {surprise} and {excite} the person, as these will often make a lasting impression.

4. Donate your {time} as part of the {gift}. 
If the person is often stressed, overworked, or going through a hard time, offer to gift them your {time}. This could be by {doing} all the {yardwork} for {week} or by {taking} their {kids} out for {day} so they have some free time to themself.

~FIN~

======================================================

Story source: https://www.wikihow.com/Give-a-Great-Gift-to-Someone
Under an Attribution-Noncommercial-Share Alike 3.0 Creative Commons License, wikiHow's text content is free to modify, republish and share.
"""
give_a_gift = give_a_gift.format(gift=input("[1 of 31] Enter a concrete noun: "), 
                                 enjoy=input("[2 of 31] Enter a transitive verb: "), 
                                 direction=input("[3 of 31] Enter a direction: "), 
                                 thinking=input("[4 of 31] Enter an intransitive verb in the progressive: "), 
                                 personality=input("[5 of 31] Enter an abstract noun: "), 
                                 tastes=input("[6 of 31] Enter an abstract noun: "), 
                                 close=input("[7 of 31] Enter an adjective: "), 
                                 intimate=input("[8 of 31] Enter an adjective: "), 
                                 platonic=input("[9 of 31] Enter an adjective: "), 
                                 personal=input("[10 of 31] Enter an adjective: "),
                                 accessible=input("[11 of 31] Enter an adjective: "), 
                                 need=input("[12 of 31] Enter a transitive verb: "), 
                                 purchase=input("[13 of 31] Enter a noun derived from a verb (e.g. destruction): "), 
                                 kitchen=input("[14 of 31] Enter a concrete noun: "), 
                                 backpack=input("[15 of 31] Enter a concrete noun: "), 
                                 school=input("[16 of 31] Enter an activity: "), 
                                 experience=input("[17 of 31] Enter a noun derived from a verb (e.g. destruction): "), 
                                 impactful=input("[18 of 31] Enter an adjective: "), 
                                 item=input("[19 of 31] Enter a concrete noun: "), 
                                 couples=input("[20 of 31] Enter a concrete noun: "), 
                                 date=input("[21 of 31] Enter a concrete noun: "), 
                                 restaurant=input("[22 of 31] Enter a kind of place: "), 
                                 surprise=input("[23 of 31] Enter a transitive verb: "), 
                                 excite=input("[24 of 31] Enter a transitive verb: "), 
                                 time=input("[25 of 31] Enter an abstract noun: "), 
                                 doing=input("[26 of 31] Enter a transitive verb in the progressive: "), 
                                 yardwork=input("[27 of 31] Enter a plural or mass noun: "), 
                                 week=input("[28 of 31] Enter a duration (e.g. 10 seconds): "), 
                                 taking=input("[29 of 31] Enter a transitive verb in the progressive: "), 
                                 kids=input("[30 of 31] Enter a concrete noun (singular or plural): "), 
                                 day=input("[31 of 31] Enter a duration (e.g. 10 seconds): "))
print(give_a_gift)

sys.exit()

