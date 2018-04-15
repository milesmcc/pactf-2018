# The Lottery, Part One: Spill Your Heart Out!
This problem has the often-enjoyable "thing that seems impossible but isn't" structure to it. The
problem gives the user an executable file which repeatedly queries the user for a "lottery number",
which is really just any normal 32-bit integer, and checks it against an RNG that is running
internally. If the user fails, it simply taunts the user with the number they needed to guess. To
get the flag, all you have to do is guess correctly, which can't be that hard, right?  I've exactly
recreated the Java RNG, and so although I actually wrote the thing in Rust the hint about Oracle is
still valid—treating the program as a Java program should work.

The program is (as far as I'm aware) resistant to disassembly or other hackery to get the flag
without satisfying the program with the correct lottery numbers, and because it isn't automated it's
cumbersome to get any more info than three or four outputs. This is no worry: due to the Java RNG,
it is possible to pretty much always get the third lottery number right from the first and
second. This is supposed to be an implication of the title as well: the program doesn't need to be
worked *around*, because it spills its heart out to you already (to borrow Heartbleed's
terminology). All you need to do is use the data it freely gives you.

The hint about Java should (hopefully) lead the problem solver to look up the Java RNG and its
structure. The basic Java RNG (the one in `java.util.Random`) uses what is called a *linear
congruential generator*: essentially just multiplying and adding by two constants in modular
arithmetic. These LCGs are terrible: unlike the better RNG that other programming languages like
Python uses, these numbers are statistically alright for really rudimentary tasks but (as this
example demonstrates!) are trivially insecure even with hurdles.

LCGs have bad bits at the bottom: for example, the last bit simply alternates between 0 and 1, the
next bit has a period of 4, and so on: just like in base-10 math, the units digits rarely seem
random. Thus, the Java RNG discards the last sixteen bits of each generated number, which is already
mod 2^48, to output a 32-bit integer using the `.nextInt()` function.

However, you'll notice that there are 65536 possible states (in essence, you have to guess the last
sixteen bits) and 65536^2 possible next numbers: the full state completely determines the behavior
of the RNG. This means that it's unlikely that you even need more than two numbers to completely
determine the RNG's output: there's a 1 in 65536 chance there's overlap assuming independence.

Therefore, in order to solve the problem, all you need to do is reverse-engineer the RNG state
through brute force, manually input two RNG outputs, and then correctly guess the third one. (Of
course, you have more guesses, so even if the 1 in 65536 happens you can just keep going: you can
even restart the program if for some crazy reason a seed didn't work.)

One last thing: most RNG manipulation in the real world comes from trying to guess the seeds of an
RNG. This actually won't work: I use a cryptographically-secure RNG that Rust provides to seed the
insecure Java RNG mockup, so as far as I'm aware predicting the seed is impossible. You'll just have
to go off the outputs.

## Commentary
I had versions of this that were crazy hard: ones where I gave you Java code that used RNG seeds to
find primes or other keys for a cipher that you then had to break, not giving the Oracle hint, using
my own constants for the LCG so that you'd have to reverse-engineer those, which is current
research, and so on. I settled on this version because it contained the kernel of the problem, that
Java's RNG is really bad and you should use a cryptographically-secure one for anything where
prediction is important, without any of the clutter or trial-and-error. (I still have to work on
more really tough problems: I thought this would be the second one, but I was wrong.) This problem
is tough, don't get me wrong, but it's not *that* difficult.

I really like this problem: I think anyone who does it will learn something, I think it could be
solved very quickly (so it won't bog down really capable teams) but isn't trivial, and has the nice
(at least to me) effect of "wait a second, this is impossible! Unless..." that I've liked about past
PACTF problems.

The two things that I worry about are the executables and the possiblility of unintended solutions
that take the fun out of it (not all unintended solutions suck, but the problem is interesting
enough that reducing it to a standard disassembly problem would irk me). It's a pain to give people
executables, and while I'm happy to try and compile for as many targets as possible I can't deny the
extra work and possibility for error it brings in. I also am not very knowledgeable about
disassembly, so it's hard for me to say if you can divine the flag without making the program spit
it out itself. Using the `strings` command won't work because I obfuscate the string's
initialization (it isn't in memory until you win the lottery), and I've stripped out every symbol I
can, but I still worry about it.

## Correction
The executable bit has been removed. You simply get the number from the output I share. The number
of points has been reduced because of this, as it reduces the amount of things to try.

## Flag
The flag is `-632232200`.
