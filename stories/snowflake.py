#! /usr/bin/python
#
# snowflake.py
#
# Usage:
#     module for madlib.py
#
# When imported by madlib.py: replaces words in story to produce madlib
#

import sys

make_3d_snowflake = """
======================================================

How to make a 3D {paper} {snowflake}

Three dimensional {paper} {snowflakes} look {magnificent} hanging in a window or on a wall. Fun for kids or adults, they are easy to make. Some like them for {Christmas}, but you may like them any time!

1. Gather the materials. You'll need {six} (or {eight} for a fuller {snowflake}) pieces of {paper}. {White} {copy} {paper} will do, although you can use more elaborate types of {paper} like {construction} {paper} or {origami} {paper}. You'll also need a {scissors}, {clear} {tape}, and a stapler or some double-sided {tape}.

2.  Fold each of the {six} pieces of {paper} in half diagonally, and then in half again diagonally. If the {paper} you are using does not make a perfect {triangle}, cut off the edge that sticks out to make the sides align perfectly. You should end up with a {square} folded into a {triangle}. Fold the {triangle} in half, noting where the folded "bottom" of the {triangle} is.

3. Cut three slits in the {triangle}. Position the {scissors} along the bottom fold, and parallel to one of the edges going up to the top. Cut almost all the way up to the double folded crease, but not quite. Keep about the same distance between each cut. (This might not be suitable for thicker {paper}, since the number of layers makes it difficult to cut through.)

4. Unfold the {paper} so that it is flat. Position it so that one of the points of the {square} faces you. It should look like a {picture}.

5. Keeping your {paper} {diamond} side-up, roll the first two innermost {paper} lines together to form a tube. Stick these two pieces together with {tape}. You should see {triangle} shapes on each side of the roll.

6. Turn the {diamond} over to the other side of the {paper}. Take the next two {paper} lines and pull them together on the opposite side of the tube and stick together as before. This will be a more rounded shape and wider than the first tube.

7. Keep turning the {paper} and joining the {paper} lines together on opposite side in the same fashion until all {paper} lines have been joined.

8. Repeat Steps 2 to 7 with the remaining pieces of {paper}.

9. Join {three} of the completed rolled pieces together at one end and staple together using the other hand. Do the other pieces the same way. Now you will have {two} pieces consisting of {three} strands or "arms" each. (For smaller {snowflakes}, it may be easier to use double-sided {tape} or {white} glue in place of staples.)

10. Staple the {two} new pieces together in the middle.

11. Staple where each of the {six} arms meet. This ensures that the {snowflake} shape is pulled into place.

12. Hang them up, use them to make a center piece or use them to decorate in your own way in places where they can be admired.

~FIN~

======================================================

Story source: https://www.wikihow.com/Make-a-3D-Paper-Snowflake
Under an Attribution-Noncommercial-Share Alike 3.0 Creative Commons License, wikiHow's text content is free to modify, republish and share.
"""
make_3d_snowflake = make_3d_snowflake.format(paper=input("[1 of 21] Enter a kind of material: "), 
                                             snowflake=input("[2 of 21] Enter a concrete noun: "), 
                                             snowflakes=input("[3 of 21] Enter the plural of the previous noun: "), 
                                             magnificent=input("[4 of 21] Enter an adjective: "), 
                                             Christmas=input("[5 of 21] Enter a holiday: "), 
                                             six=input("[6 of 21] Enter a number: "), 
                                             eight=input("[7 of 21] Enter a number that's higher than the previous one: "), 
                                             White=input("[8 of 21] Enter an adjective (capitalize first letter): "), 
                                             copy=input("[9 of 21] Enter a concrete noun: "), 
                                             construction=input("[10 of 21] Enter a concrete noun: "), 
                                             origami=input("[11 of 21] Enter a concrete noun: "), 
                                             scissors=input("[12 of 21] Enter a sharp object in the plural: "), 
                                             clear=input("[13 of 21] Enter an adjective: "), 
                                             tape=input("[14 of 21] Enter something sticky: "), 
                                             triangle=input("[15 of 21] Enter a shape: "), 
                                             square=input("[16 of 21] Enter a shape: "), 
                                             picture=input("[17 of 21] Enter a concrete noun: "), 
                                             diamond=input("[18 of 21] Enter a shape: "), 
                                             three=input("[19 of 21] Enter a number that's smaller than your first number: "), 
                                             two=input("[20 of 21] Divide your first number by your previous number: "), 
                                             white=input("[21 of 21] Enter a color: "))
print(make_3d_snowflake)

sys.exit()

