#! /usr/bin/python
#
# cults.py
#
# Usage:
#     module for madlib.py
#
# When imported by madlib.py: replaces words in story to produce madlib
#

import sys

identify_cults = """
======================================================

How to Tell if a {church} is a {cult}

{religious} {cults} are groups of {people} who adhere to a {strict} belief system and organize around a {charismatic} {leader}. Unlike a {church}, a {religious} {cult} is {destructive} and uses {fear} and {manipulation} to command their {membership}. If you evaluate their {doctrine}, examine their {practices}, and take your time to look at the {church} {objectively}, you can determine whether an organization is a legitimate {church} or a {cult}.

1. Read the {church}'s {rules}.
{cults} thrive on the {unquestioning} {obedience} of their {membership}. Often, a {cult}'s {rules} will be {arbitrary} and many of them will {benefit} the {leader} of the {cult}. Also, there are often {harsh} punishments for {breaking} the {rules}, such as mandatory physical labor.

2. Determine what would happen if you {left} the {church}.
{cults} will often have {severe} punishments in place for those who decide to {leave} the {church}. Common consequences could include a punishment directly from {God} or being prevented from talking to {family} and {friends} within the {church}.

3. Beware of {denunciation} {sessions}.
{denunciation} {sessions} are displays of {public} {humiliation}, where the {leader} of the {church} will {humiliate} you in front of other members. If the {church} mandates group activities like this, it's a sign it could be a {cult}.

4. Avoid {churches} that obsess over {prophecy} or that talk of {mass} {suicide}.
Many {cults} will obsess over a {fabricated} {prophecy} that doesn't align with {churches} in the same region or talk about {mass} {suicide}. If the {church} preaches about scary {unavoidable} {prophecies} or {suicide}, it is probably a {cult}.

5. Determine if they have an elitist {thing}.
Many {cults} will have an elitist {thing} that sees itself as superior to those outside of the {cult}. {cults} will often convince members that they are an elite group of {people} who were born to {save} the world or {change} the course of {human} history. If you notice an elitist or {arrogant} {personality} from the members, it could be a {cult}.

~FIN~

======================================================

Story source: https://www.wikihow.com/Tell-if-a-Church-is-a-Cult
Under an Attribution-Noncommercial-Share Alike 3.0 Creative Commons License, wikiHow's text content is free to modify, republish and share.
"""
identify_cults = identify_cults.format(church=input("[1 of 46] Enter a concrete noun: "), 
                                       churches=input("[2 of 46] Enter the plural of the previous noun: "), 
                                       cult=input("[3 of 46] Enter a concrete noun: "), 
                                       cults=input("[4 of 46] Enter the plural of the previous noun: "), 
                                       people=input("[5 of 46] Enter a plural noun: "), 
                                       strict=input("[6 of 46] Enter an adjective: "), 
                                       charismatic=input("[7 of 46] Enter an adjective: "), 
                                       leader=input("[8 of 46] Enter a kind of person or profession: "), 
                                       religious=input("[9 of 46] Enter an adjective: "), 
                                       destructive=input("[10 of 46] Enter an adjective: "), 
                                       fear=input("[11 of 46] Enter an abstract noun: "), 
                                       manipulation=input("[12 of 46] Enter an abstract noun: "), 
                                       membership=input("[13 of 46] Enter a kind of person or profession in the plural: "), 
                                       doctrine=input("[14 of 46] Enter an abstract noun: "), 
                                       practices=input("[15 of 46] Enter a plural noun: "), 
                                       objectively=input("[16 of 46] Enter an adverb: "), 
                                       rules=input("[17 of 46] Enter a plural noun: "), 
                                       unquestioning=input("[18 of 46] Enter an adjective: "), 
                                       obedience=input("[19 of 46] Enter an abstract noun: "), 
                                       arbitrary=input("[20 of 46] Enter an adjective: "), 
                                       benefit=input("[21 of 46] Enter a transitive verb: "), 
                                       harsh=input("[22 of 46] Enter an adjective: "), 
                                       breaking=input("[23 of 46] Enter a transitive verb in the progressive: "), 
                                       left=input("[24 of 46] Enter a transitive verb in the past tense: "), 
                                       severe=input("[25 of 46] Enter an adjective: "), 
                                       leave=input("[26 of 46] Enter the present tense of the previous verb: "),
                                       God=input("[27 of 46] Enter a proper name: "), 
                                       family=input("[28 of 46] Enter a kind of person or profession in the plural: "), 
                                       friends=input("[29 of 46] Enter a kind of person or profession in the plural: "), 
                                       denunciation=input("[30 of 46] Enter an abstract noun: "), 
                                       sessions=input("[31 of 46] Enter a plural noun: "), 
                                       public=input("[32 of 46] Enter an adjective: "), 
                                       humiliation=input("[33 of 46] Enter an abstract noun: "), 
                                       humiliate=input("[34 of 46] Enter a transitive verb: "), 
                                       prophecy=input("[35 of 46] Enter a concrete noun: "), 
                                       mass=input("[36 of 46] Enter an adjective: "), 
                                       suicide=input("[37 of 46] Enter an abstract noun: "), 
                                       fabricated=input("[38 of 46] Enter a transitive verb in the past tense: "), 
                                       unavoidable=input("[39 of 46] Enter an adjective: "), 
                                       prophecies=input("[40 of 46] Enter a plural noun: "), 
                                       thing=input("[41 of 46] Enter a concrete noun: "), 
                                       save=input("[42 of 46] Enter a transitive verb: "), 
                                       change=input("[43 of 46] Enter a transitive verb: "), 
                                       human=input("[44 of 46] Enter a concrete noun: "), 
                                       arrogant=input("[45 of 46] Enter an adjective: "), 
                                       personality=input("[46 of 46] Enter an abstract noun: "))
print(identify_cults)

sys.exit()

