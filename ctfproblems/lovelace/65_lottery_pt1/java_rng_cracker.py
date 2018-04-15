"""This file breaks the Java RNG as a cryptographically-secure one, by showing how to derive the
state from three inputs!

Java's RNG is a linear congruential RNG using a multiplier m and increment i, whose specific values
I omit here. Java simply computes mx + i mod 2 ^ 48, sets that as the state, and then uses the first
32 bits for the output. (Note that the last couple digits really suck in terms of randomness, and
the last one simply alternates, so truncating is a good idea!) Reverse-engineering is trivial given
a single full input, because that's the whole state of the RNG!

With some bits hidden, it becomes different: one has to brute force the ending bits. There are 65536
possible states for the first one, which uniquely determines the second number without needing to
know its state: there are 65536 ^ 2 possible second numbers, so there is unlikely to be major
overlap. Assuming the R in RNG really is right, which is just approximation, there's a roughly 1 /
65536 chance of this, and that multiplies for each subsequent number.
"""

from java_rng import RNG as JavaRNG


# this is to show that it's possible to deduce that we're using a Java RNG once you know we're
# using a linear congruential one
def find_vals(rng):
    """Returns (m, i) for the LCRNG."""
    a = rng.seed
    b = rng.next(a)
    c = rng.next(b)
    print(a, b, c, 2 ** 48)
    return (c - b) / (b - a), (a * c - b ** 2) / (a - b)

rng = JavaRNG()
print(find_vals(rng))
# assert(find_vals(rng) == (rng.MULTIPLIER, rng.INCREMENT))


def reverse_engineer_rng(nums):
    """Given numbers from an RNG, returns a list of possible RNGs that produce possible
    continuations. Nums must have at least 2 elements."""
    # for every possible true seed after the n1 call, determine if n2 would be the next number: get
    # a list of all possible such states
    possible_states = []
    n1 = nums[0]
    n2 = nums[1]
    rng = JavaRNG()  # only using class methods, seed doesn't matter
    for i in range(2 ** 16):
        # 48-bit state: first turn num into 32-bit, then add guessed bits
        if n1 < 0:
            n1 = n1 + 2 ** 32  # two's complement undoing
            
        state = (n1 << 16) + i
        # if a match for the next number
        if rng.state_to_int(rng.next(state)) == n2:
            possible_states.append(state)

    possible_rngs = [JavaRNG.with_seed(state) for state in possible_states]
    for rng in possible_rngs:
        # "fast-forward" output to current num, n3: first output is n2, so we skip it
        rng.nextInt()
    # iteratively refine until only a single state left or we run out of numbers
    ind = 2
    while len(possible_rngs) > 1 and ind < len(nums):
        still_good = []
        for rng in enumerate(possible_rngs):
            output = rng.nextInt()
            if output == nums[ind]:  # still possible
                still_good.append(rng)
        # only track the ones that could still work
        possible_rngs = still_good
        ind += 1

    # fast-forward to end of list if the whole list wasn't used
    while ind < len(nums):
        ind += 1
        for rng in possible_rngs:
            rng.nextInt()
    return possible_rngs

# RNG(5) produces this output, both in this implementation and Java
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

# test code that demonstrates this works
# nums = [-1157408321, 758500184, 379066948]
# possible = reverse_engineer_rng(nums)
# print([x.seed for x in possible])
# print()
# print([x.nextInt() for x in possible])
