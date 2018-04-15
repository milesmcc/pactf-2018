"""This is an implementation of the Java RNG in Python. That's when you know someone really hates a
programming language!

The Java RNG algorithm is two lines, so it's pretty easy. Given an internal seed, and a parameter
bits that is how many bits to output, it executes the following:

seed = (seed * 0x5DEECE66DL + 0xBL) & ((1L << 48) - 1);
return (int) (seed >>> (48 - bits));
"""

def unsigned_right_shift(a, b):
    """Computes a >>> b in Java, or an unsigned right shift. Assumes longs, e.g., 64-bit integers."""
    if a >= 0:
        return a >> b
    else:
        return ((a + 2 ** 64) >> b)

class RNG:
    """Port of Java's RNG nextInt() function."""
    # idk how this was chosen, to me it's a complete magic number
    MULTIPLIER = 0x5DEECE66D  # equals 25214903917 in base 10
    # as far as I know this was just a small number that wasn't susceptible to tricks
    INCREMENT = 11
    
    def __init__(self, seed=0):
        # truncates to 48 bits after XORing, not sure why the XOR is used but w/e
        self.seed = seed ^ self.MULTIPLIER & ((1 << 48) - 1)

    @classmethod
    def with_seed(cls, seed=0):
        """Initializes the seed without any XOR BS."""
        rng = cls()
        rng.seed = seed
        return rng

    def nextInt(self):
        """Returns a "random" 32-bit signed integer, taken as 32 bits from the next PRNG value in
        two's-complement form."""
        # update seed: simple multiplication, addition, then take 48 bits
        self.seed = self.next(self.seed)
        return self.state_to_int(self.seed)

    @classmethod
    def next(cls, state):
        """Returns the next state from the given 48-bit one."""
        return (state * cls.MULTIPLIER + cls.INCREMENT) & ((1 << 48) - 1)

    @staticmethod
    def state_to_int(state):
        """Returns the int form of the 48-bit state, in Java's rules."""
        # get the last 32 bits of this in two's complement form by removing 16 from the right
        truncated = unsigned_right_shift(state, 16)
        # "cast" to an integer: convert to two's complement, take the last 32 bits
        if truncated < 0:
            truncated += 2 ** 64
        truncated %= 2 ** 32
        if truncated >= 2 ** 31:
            truncated = -(2 ** 32 - truncated)
        return truncated
        

# test code
# rng = RNG(5)
# for i in range(10):
#     print(rng.nextInt())

# list from online Java compiler, matches
# -> -1157408321
# -> 758500184
# -> 379066948
# -> -1667228448
# -> 2099829013
# -> -236332086
# -> 1983575708
# -> -745993913
# -> 1926715444
# -> 1836354642
