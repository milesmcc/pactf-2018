# Unicode Steganography
The contestants are given a single large text file full of apparent gibberish. The task is to
somehow determine some subset of those words that are a meaningful message. In this case, the six
special words read "the flag is in plain sight". The flag is, true to that, "in plain sight".

The thing that makes these words special, despite not looking any different than any others, is the
inclusion of special Unicode characters that are usually invisible: zero-width joiners and
spaces. These aren't always completely invisible, but especially in a file this large you're not
going to be able to manually inspect. (There are the four such characters I used after this period.﻿‌​‍)

There's no included solution script, but to be honest this problem doesn't even need a script: just
a text editor that can search for arbitrary Unicode characters will do. Each hidden word has a
zero-width character in the middle of it somewhere, and in order the six words selected read the
message above.

## Commentary
This problem, unfortunately, falls in the category of "you either know it or you don't": if you're
generally unfamiliar with Unicode, even after the hint and the helpful failure message (which I'm
not a huge fan of, because it incentivizes you to just submit randomness to each problem at least
once, but it's been done before in PACTF and isn't super game-changing as far as hints go), there's
really not much else you can do with the problem. Unlike other problems where it's obvious once you
have the answer, the given haystack could spell out so many flags that there's no way of going
forward unless you search for zero-width characters. It's also big enough that manual inspection
won't reveal anything: the first "the" that is in the message appears after 10,000 words.

The nature of the problem makes it hard to assess difficulty: I don't want to give too few points
for it because I fully expect otherwise very good teams not to get it, which is discouraging if it's
supposedly super easy, but on the other hand it requires no coding ability and, if you know the
trick, is extremely simple. The given text helps you steer off of laborious dead ends as well:
you're searching for specially-marked words, and there's only so many ways to do that in plain text,
as the hint says. Because of this, I think it's not that bad, and so I'm reluctant to give it a ton
of points as well. This is up for discussion.

## Flag
The flag is `in plain sight`. It's a bit on the nose, but still probably not guessable: without
solving the problem, it would appear that the flag could be virtually anything.
