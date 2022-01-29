#! /usr/bin/python
#
# input_mssgs.py
#
# Usage:
#     module for madlib.py
#
# Provides messages for various inputs
#

# people inputs
name_mssg = " Enter a proper name: "
person_mssg = " Enter a kind of person or profession: "

# noun inputs
noun_mssg = " Enter a noun: "
plural_noun_mssg = " Enter a plural noun: "
abstract_noun_mssg = " Enter an abstract noun: "
mass_noun_mssg = " Enter a mass noun: "
plural_or_mass_mssg = " Enter a plural or mass noun: "
liquid_mssg = " Enter a kind of liquid: "
food_mssg = " Enter a kind of food: "
sharp_noun_mssg = " Enter a sharp object: "
material_mssg = " Enter a kind of material: "
sticky_noun_mssg = " Enter something sticky: "
noun_from_verb_mssg  = " Enter a noun derived from a verb (e.g. destruction): "

# adjective & adverb inputs
adjective_mssg = " Enter an adjective: "
color_mssg = " Enter a color: "
adverb_mssg = " Enter an adverb: "

# verb inputs
verb_i_mssg = " Enter an intransitive verb: "
verb_t_mssg = " Enter a transitive verb: "
verb_d_mssg = " Enter a ditransitive verb: "

# morphology
#
## nouns
plural = " in the plural: "
plural_person_mssg = person_mssg[:-2] + plural
plural_sharp_noun_mssg = sharp_noun_mssg[:-2] + plural

## verbs
#
### past tense
past = " in the past tense: "
verb_i_past_mssg = verb_i_mssg[:-2] + past
verb_t_past_mssg = verb_t_mssg[:-2] + past
verb_d_past_mssg = verb_d_mssg[:-2] + past
### 3sg form
pres_3sg = " in the 3rd-person present form: "
verb_i_3sg_mssg = verb_i_mssg[:-2] + pres_3sg
verb_t_3sg_mssg = verb_t_mssg[:-2] + pres_3sg
verb_d_3sg_mssg = verb_d_mssg[:-2] + pres_3sg
### progressive aspect
ing = " in the progressive: "
verb_i_ing_mssg = verb_i_mssg[:-2] + ing
verb_t_ing_mssg = verb_t_mssg[:-2] + ing
verb_d_ing_mssg = verb_d_mssg[:-2] + ing
### perfective form
perfect = " in the perfective form: "
verb_i_perf_mssg = verb_i_mssg[:-2] + perfect
verb_t_perf_mssg = verb_t_mssg[:-2] + perfect
verb_d_perf_mssg = verb_d_mssg[:-2] + perfect

## previous word references
previous = " Enter the {} of the previous {}: "
previous_noun_plural_mssg = previous.format("plural", "noun")
synonym_mssg = previous.format("synonym", "adjective")
antonym_mssg = previous.format("antonym", "adjective")
related_adjective_mssg = " Enter a synonym or antonym of the previous adjective, or an otherwise related adjective: "
previous_verb_past_mssg = previous.format("past tense", "verb")
previous_verb_past_mssg = previous.format("3rd-person singular form", "verb")
previous_verb_ing_mssg = previous.format("progressive", "verb")
previous_verb_perf_mssg = previous.format("perfective form", "verb")
previous_verb_inf_mssg = previous.format("infinitive form (e.g. 'to swim', 'to bring')", "verb")
position = " Enter the {} of the {} {}: "
position_noun_sg_mssg = previous.format("singular", "first", "noun")
position_noun_plural_mssg = previous.format("plural", "first", "noun")

# miscellaneous inputs
year_mssg = " Enter a year: "
month_mssg = " Enter a month: "
week_day_mssg = " Enter a day of the week: "
duration_mssg = " Enter a duration (e.g. 10 seconds): "
holiday_mssg = " Enter a holiday: "
shape_mssg = " Enter a shape: "
place_mssg = " Enter a location (either a name, like 'Australia', or a description, like 'a store' or 'the park'): "
business_mssg = " Enter a kind of business: "
activity_mssg = " Enter a kind of activity: "
event_mssg = " Enter a kind of event: "
direction_mssg = " Enter a direction (e.g. 'up', 'North'): "
exclam_mssg = " Enter an interjection or exclamation with capitalization (e.g. 'Oh'): "
phrase_mssg = " Enter a phrase you might say to someone: "

# math
number_mssg = " Enter a number: "
addition_mssg = " Add the previous two numbers: "
multiplication_mssg = " Multiply the previous two numbers: "
subtraction_mssg = " Subtract the previous number from the one before it: "
division_mssg = " Use your previous number to divide the one before it: "

