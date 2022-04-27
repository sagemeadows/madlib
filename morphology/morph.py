#! /usr/bin/python
#
# morph.py
#
# Usage:
#     module for madlib.py
#
# Apply morphology to words
#

import re
from morphology.irregs import irreg_nouns, irreg_verbs

# Spelling rule patterns
y_vowel = re.compile("[bcdfghjklmnpqrstvwxyz]y$")
short_vowel = re.compile("[bcdfghjklmnpqrstvwxyz][aeiou][mpbntdg]$")

# Morphology functions

## Noun funct
def pl(noun):
    yv = y_vowel.findall(noun)
    if noun in irreg_nouns:
        plural = irreg_nouns[noun]
    elif yv:
        plural = noun[:-1] + 'ies'
    elif noun.endswith(('s', 'z', 'sh', 'ch', 'o')):
        plural = noun + 'es'
    else:
        plural = noun + 's'
    return plural

## Verb functions
def past(verb):
    yv = y_vowel.findall(verb)
    sv = short_vowel.findall(verb)
    if verb in irreg_verbs:
        past = irreg_verbs[verb]['past']
    elif yv:
        past = verb[:-1] + 'ied'
    elif sv:
        past = verb + verb[-1] + 'ed'
    elif verb.endswith('e'):
        past = verb + 'd'
    else:
        past = verb + 'ed'
    return past

def part(verb):
    yv = y_vowel.findall(verb)
    sv = short_vowel.findall(verb)
    if verb in irreg_verbs:
        part = irreg_verbs[verb]['part']
    elif yv:
        part = verb[:-1] + 'ied'
    elif sv:
        past = verb + verb[-1] + 'ed'
    elif verb.endswith('e'):
        part = verb + 'd'
    else:
        part = verb + 'ed'
    return part

def prog(verb):
    sv = short_vowel.findall(verb)
    if verb in irreg_verbs:
        prog = irreg_verbs[verb]['prog']
    elif verb.endswith('e'):
        prog = verb[:-1] + 'ing'
    elif sv:
        prog = verb + verb[-1] + 'ing'
    else:
        prog = verb + 'ing'
    return prog

def pres(verb):
    yv = y_vowel.findall(verb)
    if verb in irreg_verbs:
        pres = irreg_verbs[verb]['pres']
    elif yv:
        pres = verb[:-1] + 'ies'
    elif verb.endswith(('s', 'z', 'sh', 'ch', 'o')):
        pres = verb + 'es'
    else:
        pres = verb + 's'
    return pres


## Adjective functions
irreg_adj_ends = ('ous', 'ic', 'ex', 'ible', 'able')

def compar(adj):
    yv = y_vowel.findall(adj)
    sv = short_vowel.findall(adj)
    if adj.endswith(irreg_adj_ends):
        superl = 'most ' + adj
    elif adj.endswith('e'):
        compar = adj + 'r'
    elif yv:
        compar = adj[:-1] + 'ier'
    elif sv:
        compar = adj + adj[-1] + 'er'
    else:
        compar = adj + 'er'
    return compar

def superl(adj):
    yv = y_vowel.findall(adj)
    sv = short_vowel.findall(adj)
    if adj.endswith(irreg_adj_ends):
        superl = 'most ' + adj
    elif adj.endswith('e'):
        compar = adj + 'st'
    elif yv:
        superl = adj[:-1] + 'iest'
    elif sv:
        superl = adj + adj[-1] + 'est'
    else:
        superl = adj + 'est'
    return superl

