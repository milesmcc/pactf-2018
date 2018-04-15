# Navajo Code Talkers
So many CTF problems are callbacks to pre-modern cryptography techniques, like the Polybius
square. I wanted to do one of these problems, but one that calls back to one of the most successful
such codes, never broken during warfare, that played a pivotal role in one of the most important
wars of all time. I'm talking about the Navajo code talkers and their role in World War II.

The code I use in the problem is a version of it that has the added simplification of removing any
of the actual Navajo words used to describe things (so for example, instead of spelling out
"destroyer" the real Navajo code talkers would just say the Navajo for "shark"). This message only
uses the phonetic that they would use for more general communication, using 26 Navajo words that
correspond to a word in English phonetic. (Navajo hadn't been written down when this was first used:
I use the modern spellings, which have *tons* of Unicode and are also fairly hard to Google, which
adds some nice difficulty in my view.)

All one has to do to solve the problem is go to the Wikipedia page on [Navajo code
talkers](https://en.wikipedia.org/wiki/Code_talker#Navajo_code_talkers), go look at the modern
spellings for each letter, and map them out. You don't really need a computer program. That'll give
you the flag, who was the last original Navajo code talker, Chester Nez.

This is tough to Google directly, but it isn't that bad if you take the hints I give. The problem
makes multiple references to the speed of transmission, which is an allusion to how fast the Navajo
code talkers were and a hint that they aren't just using nonsense words. If you miss the problem, I
tell you you're wrong in multiple languages to drive home the point. I also mention "history books"
in the hint, and that might help you out too. It's definitely not the easiest (hence a relatively
high point count for a problem with no coding required), but it's doable and quite easy if you
happen to know your WWII crytography.
# Flag
The flag is `chesternez`. Because the phonetic destroys case, I have the `grader.py` file accept any
cased version of that flag.
