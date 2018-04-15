# Book Cipher
A classic old-school crytography technique, made especially nice as a step up from the Caesar Cipher
but not actual modern computer crypto. I picked something famous enough that online copies exist
with numbered lines, which makes your life a lot easier, and something famous enough for people to
possibly recognize the quote (or at least the coy hint in the title). 

To make the solution explicit: each pair `a:b` is a line number and a word number in *Julius
Caesar*, the Shakespeare play. The code reads out in plaintext "the answer is Cassius".
## Commentary
I'd be interested to get people to test this blind and see if they can both efficiently find the
lines in *Julius Caesar* and speed through it fairly quickly. I don't want it to get tedious, and I
expect that for pro teams this will take seconds: go Google an open source Shakespeare play with
line numbers, find the last word because you guess that the first three are "the answer is" or
variations thereof. (Unfortunately, "flag" does not appear in the text of *Julius Caesar*, so
"answer" will have to do.)

Note that you should expect that specific format (instead of act:chapter:paragraph: or something
like that) because I cite the quote using the line number and not the act or anything else, so I
think it's pretty sensible.
## Flag
As of now, the flag is `cassius`, but the grader checks for any case version of that: if you want it
to be a single string, `Cassius` is the most natural choice.
