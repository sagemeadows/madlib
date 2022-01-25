#! /usr/bin/python
#
# santa.py
#
# Usage:
#     module for madlib.py
#
# When imported by madlib.py: replaces words in story to produce madlib
#

import sys

write_to_santa = """
======================================================

How to write a letter to {Santa}

Writing a letter to {Santa} is a fun {Christmas} tradition. A well written letter shows {Santa} you are {polite}. Plus, it makes it easier for them to get you the {presents} you want. After all, with millions of {children} (and {children}-at-heart) asking for {presents}, you could say they are a pretty {busy} {guy}. Start by thinking about what you want to ask for in advance. Then, write a {polite} letter, {decorate} it, and give it to your {parents} to send off to {NorthPole}.

1. Pick what you'll write on. You can keep it simple with a {plain} {white} piece of {paper} or you can go for something a little bolder. {Colorful} {construction} {paper} works well. Whatever {paper} you pick, make sure to grab a couple of pieces in case of mess-ups.

2. Choose something to write with. You can use a pen or a pencil, but feel free to use {crayons}, {colored_pencils}, and {markers}, too. You can even combine different writing tools, like {markers} and {colored_pencils}, to make a super {colorful} letter.

3. Begin your letter with "{Dear} {Santa}."

4. Tell {Santa} who you are. {Santa} knows you, of course – they have been watching you all year. However, they get lots of letters, so they need to know which one is yours.

5. Ask {Santa} how they are doing. It is always {polite} to ask the person you are writing to how they are and {Santa} is no exception. You could ask them how the weather has been in {NorthPole}, how {MrsClaus} is doing, or if the {reindeer} enjoyed the {food} you left out for them last year.

6. Tell {Santa} the {good} things you have done this year. They are a {busy} {guy}, so they may need a little reminder about how {good} you have been. Tell them about your {accomplishments} at {school}, the {good} things you have done for your family and friends, and how {well} you have listened to your {parents}. Remember to be {honest}. {Santa}'s had their eye on you, so they will know if you are being {truthful}.

7. Ask {Santa} {politely} for the things on your list. Take a look at the list you wrote {days} ago, which should have a few {presents} that you really love. Then {politely} ask {Santa} for these things in your letter; remember to say {please}.

8. Finish up by thanking {Santa}. It is a lot of work delivering millions of {presents} to {children} all over {the_world} in a {single} night, so thank {Santa} for their {kindness}.

~FIN~

======================================================

Story source: https://www.wikihow.com/Write-a-Letter-to-Santa-Claus
Under an Attribution-Noncommercial-Share Alike 3.0 Creative Commons License, wikiHow's text content is free to modify, republish and share.
"""
write_to_santa = write_to_santa.format(Santa=input("[1 of 35] Enter a proper name: "), 
                                       Christmas=input("[2 of 35] Enter a holiday: "), 
                                       polite=input("[3 of 35] Enter an adjective: "), 
                                       presents=input("[4 of 35] Enter a plural noun: "), 
                                       children=input("[5 of 35] Enter a kind of person or profession in the plural: "), 
                                       busy=input("[6 of 35] Enter an adjective: "), 
                                       guy=input("[7 of 35] Enter a kind of person or profession: "), 
                                       decorate=input("[8 of 35] Enter a transitive verb: "), 
                                       parents=input("[9 of 35] Enter a kind of person or profession (singular or plural): "), 
                                       NorthPole=input("[10 of 35] Enter a location (either a name, like 'Australia', or a description, like 'a store' or 'the park'): "), 
                                       paper=input("[11 of 35] Enter a kind of material: "), 
                                       plain=input("[12 of 35] Enter an adjective: "), 
                                       white=input("[13 of 35] Enter a color: "), 
                                       Colorful=input("[14 of 35] Enter an adjective (capitalize first letter): "), 
                                       construction=input("[15 of 35] Enter a noun derived from a verb (e.g. destruction): "), 
                                       crayons=input("[16 of 35] Enter a plural noun: "), 
                                       colored_pencils=input("[17 of 35] Enter a plural noun: "), 
                                       markers=input("[18 of 35] Enter a plural noun: "), 
                                       colorful=input("[19 of 35] Enter an adjective: "), 
                                       Dear=input("[20 of 35] Enter an interjection or exclamation with capitalization (e.g. 'Oh'): "), 
                                       MrsClaus=input("[21 of 35] Enter a proper name: "), 
                                       reindeer=input("[22 of 35] Enter a plural noun: "), 
                                       food=input("[23 of 35] Enter a plural or mass noun: "), 
                                       good=input("[24 of 35] Enter an adjective: "), 
                                       accomplishments=input("[25 of 35] Enter an abstract noun (in the plural if it has a plural): "), 
                                       school=input("[26 of 35] Enter an activity: "), 
                                       well=input("[27 of 35] Enter an adverb: "), 
                                       honest=input("[28 of 35] Enter an adjective: "), 
                                       truthful=input("[29 of 35] Enter a synonym or antonym of the previous adjective, or an otherwise related adjective: "), 
                                       politely=input("[30 of 35] Enter an adverb: "), 
                                       days=input("[31 of 35] Enter a duration (e.g. 10 seconds): "), 
                                       please=input("[32 of 35] Enter a phrase you might say to someone: "), 
                                       the_world=input("[33 of 35] Enter a location (either a name, like 'Australia', or a description, like 'a store' or 'the park'): "), 
                                       single=input("[34 of 35] Enter an adjective: "), 
                                       kindness=input("[35 of 35] Enter an abstract noun: "))
print(write_to_santa)

sys.exit()

