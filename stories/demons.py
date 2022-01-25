#! /usr/bin/python
#
# demons.py
#
# Usage:
#     module for madlib.py
#
# When imported by madlib.py: replaces words in story to produce madlib
#

import sys

get_rid_of_demons = """
======================================================

How to Get Rid of {demons}

If you believe that you have {demons}, you might feel {scared} and {helpless}. But you can take your {power} back. Many {religious} {groups} and {spiritualists} believe {demons} get their {power} from {negative} {energy}. It’s easy to fight back by controlling your {negative} {energy}, {thoughts}, and {emotions}. Using a few {simple} {tools} and the proper rituals, you can expel {demons} from your home too. With these basic rituals, you can keep yourself and your home {demon}-free.

1. Burn {sage} to clear out demons.
Make sure all the doors and windows are open so the demons can get out, then light the {sage} and let burn for {number} seconds before you blow the flame out. Allow the {sage} to smolder and the smoke to cleanse the space of {negative} {energy}.

2. Say a prayer to get rid of the {demons}.
Whatever your religion, praying out loud can help you get rid of them. Say the prayer over and over as you move about the space so the {demons} are driven out.

3. Bang {pots} and {pans} to scare away any {demons} in your home.
Some people bang pots and pans together at the beginning of a new year to scare away the ghosts from the previous year. But you can also drive out any {demons} in your home by walking around the entire place banging {pots} and {pans} loudly.

4. Sprinkle {holy} {water} around your home.
Many people believe {holy} {water} will drive away {demons}. Call your local {church} and ask them if you can have a bottle of {holy} {water}. Sprinkle some of the {water} all over your home, making sure you get the {corners} and {windows}.

5. Call a professional to help you get rid of the {demons}.
If you’re unable to drive the {demons} away on your own, you can call a {priest} or {spiritual} {healer} to come help you. They can come to your home or meet with you to discuss possible causes and remedies.

~FIN~

======================================================

Story source: https://www.wikihow.com/Get-Rid-of-Demons
Under an Attribution-Noncommercial-Share Alike 3.0 Creative Commons License, wikiHow's text content is free to modify, republish and share.
"""
get_rid_of_demons = get_rid_of_demons.format(demon=input("[1 of 26] Enter a concrete noun: "), 
                                             demons=input("[2 of 26] Enter the plural of the previous noun: "), 
                                             scared=input("[3 of 26] Enter an adjective: "), 
                                             helpless=input("[4 of 26] Enter an adjective: "), 
                                             power=input("[5 of 26] Enter an abstract noun: "), 
                                             religious=input("[6 of 26] Enter an adjective: "), 
                                             groups=input("[7 of 26] Enter a plural noun: "), 
                                             spiritualists=input("[8 of 26] Enter a kind of person or profession in the plural: "), 
                                             negative=input("[9 of 26] Enter an adjective: "), 
                                             energy=input("[10 of 26] Enter an abstract noun: "), 
                                             thoughts=input("[11 of 26] Enter an abstract noun: "), 
                                             emotions=input("[12 of 26] Enter an abstract noun: "), 
                                             simple=input("[13 of 26] Enter an adjective: "), 
                                             tools=input("[14 of 26] Enter a plural noun: "), 
                                             sage=input("[15 of 26] Enter a concrete noun: "), 
                                             number=input("[16 of 26] Enter a number: "), 
                                             pots=input("[17 of 26] Enter a plural noun: "), 
                                             pans=input("[18 of 26] Enter a plural noun: "), 
                                             holy=input("[19 of 26] Enter an adjective: "), 
                                             water=input("[20 of 26] Enter a mass noun: "), 
                                             church=input("[21 of 26] Enter a kind of person or profession: "), 
                                             corners=input("[22 of 26] Enter a plural noun: "), 
                                             windows=input("[23 of 26] Enter a plural noun: "), 
                                             priest=input("[24 of 26] Enter a kind of person or profession: "), 
                                             spiritual=input("[25 of 26] Enter an adjective: "), 
                                             healer=input("[26 of 26] Enter a kind of person or profession: "))
print(get_rid_of_demons)

sys.exit()

