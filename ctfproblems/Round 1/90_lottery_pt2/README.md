# The Lottery, Part Two: Untwisting Fate
This problem is a very natural extension of the previous lottery problem. Java's RNG, in case you
missed the last README, uses what's called a *linear congruential generator*, with the alarming
property that given nearly any two inputs, you can predict the past and the future of the RNG. The
Mersenne Twister (specifically, MT19937) that Python and many others use is much better, but not
perfect. This problem proves that!

There's a hint in the problem executable ("from the Python Foundation"), but to the practiced eye
the very title is partly a giveaway. This is intentional: it might give some people a nice "aha"
moment which is always fun, and it confirms to the inexperienced that they're on the right
track. It's just a bit too good to be a coincidence. I was considering giving some more hints as to
the RNG ("also brought to you by Ruby, GNU Octave, etc.,"), but I'll skip it. It could make the
problem easier if that's what we need.

You need significantly more inputs to get the state of the RNG, and the math is a bit more
complex. To keep the properties of the last problem (the seed changes every time,
interactivity, etc.), I resort to an inelegant solution: giving the user a ton of lottery numbers
and making them copy and store them. This is not ideal, but it's the best solution that I can see.

(Also note that Python's RNG is theoretically the one I'm using, but it's hard to test. I'm also
using the 32-bit version, which I hoped to evidence from the fact that I'm outputting 32-bit
integers, but that might trip people up.)

Note that the problem might become a bit easier if I gave the user exactly 624 numbers: it's oddly
specific, and might give away what you're supposed to do or what Python's RNG algorithm is. I
specifically don't do that to encourage people to use their noggins a little! 1000 is more than
enough, but it leaves open the possibility of a decoy or some other strategy.

So, how the problem works: you reverse-engineer the RNG state, get the next number, and that's the
flag! I haven't done a solver program for this, mostly because it's laborious to do that sort of
thing in Rust and Rust has an especially nice library for it. The source code of the `main.rs` file
in `lottery-two` has a line that, if uncommented, will show how the state can in fact be
reverse-engineered given the inputs. Further testing would be ideal.

## Correction
As with the other lottery problems, I've removed the executable bit and just given them an
output. This makes a lot more sense here than in the other one.

# Flag
The flag is `4280933789`.
