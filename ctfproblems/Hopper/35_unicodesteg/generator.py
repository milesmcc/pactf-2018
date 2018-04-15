"""This file generates a bunch of words, of which a few read, in order, "th​e fl﻿ag i‌s i‍n pla‌in
sight". There's a bunch of randomly generated words in the middle, so it's pretty much impossible to
get that bit from it unless you realize that each of those words has a Unicode invisible character
in it."""


import random

LENGTH = 100_000  # having a ton of text helps emphasize the needle-in-a-haystack part

# having only common words makes the words themselves hide better: more repeats, Ctrl+F won't find
# "the flag is" as the only small words which looks suspicious, as when I did this before with a lot
# more words
words = []
with open("google-10000-english-no-swears.txt", 'r') as words_file:
    for line in words_file:
        words.append(line.strip().lower())

# generate indices for the actual message
indices = list(range(LENGTH))
random.shuffle(indices)
message_indices = sorted(indices[:6])
print(message_indices)  # so we can make sure they aren't all in order or something dumb

# add special chars with escape codes for visibility
# they are, in order: zero-width joiner, zero-width non-joiner, zero-width space, zero-width
# non-breaking space, zero-width non-breaking space, and zero-width non-breaking space
message = ["th\u200de", "fla\u200cg", "i\u200bs", "i\ufeffn", "p\ufefflain", "sigh\ufefft"]

haystack = [random.choice(words) for i in range(LENGTH)]
for word, loc in zip(message, message_indices):
    haystack[loc] = word

# The reason I don't just put everything on one line is that some text editors really don't like
# long lines: if you store things as a list of lines it totally messes with everything.
with open("static/haystack.txt", 'w') as out:
    for i in range(0, LENGTH, 20):  # 20 words a line
        out.write("{}\n".format(' '.join(haystack[i:i+20])))
