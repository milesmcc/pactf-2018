"""This file simply translates a message into the Navajo phonetic used during WWII. Note that this
is a simplified version: the actual Navajo language is very complicated, this is just 26 words that
are associated with each English letter."""

import string

# from Wikipedia: https://en.wikipedia.org/wiki/Code_talker#Navajo_code_talkers

# list of words from A-Z
# Modern spelling used
PHONETIC = [
    "Wóláchííʼ",
    "Shash",
    "Mósí",
    "Bįįh",
    "Dzeeh",
    "Mąʼii",
    "Tłʼízí",
    "Łį́į́ʼ",
    "Tin",
    "Téliichoʼí",
    "Tłʼízí yázhí",
    "Dibé yázhí",
    "Naʼastsʼǫǫsí",
    "Neeshchʼííʼ",
    "Néʼéshjaaʼ",
    "Bisóodi",
    "kʼaaʼ yeiłtįįh",
    "Gah",
    "Dibé",
    "Tązhii",
    "Nóódaʼí",
    "Akʼehdidlíní",
    "Dlǫ́ʼii",
    "Ałnáʼázdzoh",
    "Tsáʼásziʼ",
    "Béésh dootłʼizh"
]


def encode(message):
    """Leaving punctuation alone, translates every letter to its word equivalent and separates
    individual letters with commas."""
    ciphertext = []
    for i, char in enumerate(message):
        if char in string.ascii_letters:
            ciphertext.append(PHONETIC[string.ascii_lowercase.find(char.lower())])
            if i != len(message) - 1 and message[i+1] in string.ascii_letters:
                ciphertext[-1] += ', '
        else:
            ciphertext.append(char)
    return ''.join(ciphertext)

encode('The\nflag\nis\nchesternez')
# returns the following:
# Tązhii, Łį́į́ʼ, Dzeeh
# Mąʼii, Dibé yázhí, Wóláchííʼ, Tłʼízí
# Tin, Dibé
# Mósí, Łį́į́ʼ, Dzeeh, Dibé, Tązhii, Dzeeh, Gah, Neeshchʼííʼ, Dzeeh, Béésh dootłʼizh
