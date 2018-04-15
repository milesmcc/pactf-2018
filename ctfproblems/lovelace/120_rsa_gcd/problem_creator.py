"""This file creates a problem case for a problem that utilizes Euclid's algorithm to "crack" RSA
when the keys are poorly chosen. It generates a given amount of RSA keys, such that each one
individually is secure but if you take the GCD of all of the moduli you are able to solve it: that
is, each private key's has one of its factors appear in another key. The end "problem" is decrypting
a nested encryption using all of the keys!

Note: at least for now, you can only use an even number of keys to make life easier.

Second note: this can take a while! Generation of keys can be hard, especially with 4096-bit RSA."""

import math
from random import shuffle

# tricks like this CTF problem are why hazmat is in the name!
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
# for progress bars
from tqdm import tqdm

# This uses the pip library cryptography 2.1.4


# use 20 keys: it might seem like overkill, but it more or less guarantees you need to write a
# script and you can't just do it by hand, which is good to practice and increases the difficulty to
# where I want it to be

N_KEYS = 20

# use 4096-bit RSA: this makes it completely impossible to do any other way, even if you're the
# NSA
KEYSIZE = 4096

# this doesn't matter as long as it doesn't introduce other security vulnerabilities. I don't think
# it even needs to be constant: this is just for convenience. It shouldn't affect the problem
# difficulty at all. The given value is standard because it's really fast to exponentiate
# 10000000000001 in binary
PUB_EXPONENT = 65537

# the light at the end of the tunnel! you should know this is the flag without a "The Flag Is: " or equivalent
FLAG = b"t00 many c00ks sp0il the br0th"

# we need to generate 3 primes for every 2 keys: one that they share, and two that they don't.

# I could code the edge cases, but there's no point
assert(N_KEYS % 2 == 0)

NUM_SHARED = N_KEYS // 2  # each key pair shares a single key
NUM_UNIQUE = N_KEYS  # each key has one unique prime: once you get one the other is trivial

# getting OpenSSL or anything else to generate primes like it normally would by themselves is not
# easy, so it's easier to literally just make a private key for every prime we need to generate and
# just take the first one
def gen_prime_pair(keysize=KEYSIZE):
    """Generates a key and, as a corollary, a random prime pair (p, q) such that pq = n where n has the
    given amount of bits, or close, as a tuple (key, (p, q)).
    """
    key = rsa.generate_private_key(
        public_exponent=PUB_EXPONENT,
        key_size=KEYSIZE,
        backend=default_backend()
    )
    # now just return (p, q)
    secret = key.private_numbers()
    return (key, (secret.p, secret.q))

# Generate keys, and take the first prime from each and put them in the shared, and take the second
# one and put it in the unique bin. Then, add more randomly generated primes, chosen so that they
# don't create keys that are larger than they should be (smaller is fine).
SHARED_PRIMES = []
UNIQUE_PRIMES_A = []
UNIQUE_PRIMES_B = []
KEYS = []

for i in tqdm(range(N_KEYS // 2)):
    key, primes = gen_prime_pair()
    p, q = primes
    SHARED_PRIMES.append(p)
    UNIQUE_PRIMES_A.append(q)
    KEYS.append(key)

for shared, unique in tqdm(zip(SHARED_PRIMES, UNIQUE_PRIMES_A)):
    # find a prime that is less than or equal to the corresponding secret prime
    key, primes = gen_prime_pair()
    p, q = primes
    # this could infinite loop in super weird edge cases, idk
    # loop until you find a suitable prime
    while min(p, q) > unique:
        key, primes = gen_prime_pair()
        p, q = primes
    # we now have a prime, add it to the second list of q primes
    UNIQUE_PRIMES_B.append(min(p, q))

# we need some actual math, so I'm just gonna steal from wikibooks
# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def xgcd(b, a):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0

# x = mulinv(b) mod n, (x * b) % n == 1
def mulinv(b, n):
    g, x, _ = xgcd(b, n)
    if g == 1:
        return x % n



    
# we now have a list of p1s, q1s, p1s which are p2s, and q2s: make keys
# we just save the keys from earlier, but we have to make some new ones as well
for p, q in tqdm(zip(SHARED_PRIMES, UNIQUE_PRIMES_B)):
    # recompute everything from p and q: rather good intro to RSA!
    n = p * q
    e = PUB_EXPONENT
    public_nums = rsa.RSAPublicNumbers(e, n)
    # we could use Euler's totient but it doesn't matter
    d = mulinv(e, (p-1) * (q-1))
    dmp1 = rsa.rsa_crt_dmp1(d, p)
    dmq1 = rsa.rsa_crt_dmq1(d, q)
    iqmp = rsa.rsa_crt_iqmp(p, q)
    private_nums = rsa.RSAPrivateNumbers(
        public_numbers=public_nums,
        p=p,
        q=q,
        d=d,
        dmp1=dmp1,
        dmq1=dmq1,
        iqmp=iqmp,
    )
    key = private_nums.private_key(default_backend())
    KEYS.append(key)

# now KEYS is a list [a1, a2, a3, ..., b1, b2, b3, ...] such that a1 and b1 share a factor, a2 and b2,
# etc.

# you shouldn't need to use the fact that 1 matches with 11 and so on, so I won't allow it
shuffle(KEYS)

# write each public key to a file in the public directory, write each to a private key as well
# (purely for verification/etc, this isn't given to competitors)
for i, key in tqdm(enumerate(KEYS)):
    pub_pem = key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    priv_pem = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )
    with open(f"public/key{i}.pem", 'wb') as out:
        out.write(pub_pem)
    with open(f"private/key{i}.pem", 'wb') as out:
        out.write(priv_pem)


# now generate an encrypted message that nests: key1 is used first, then key2, etc.
ciphertext = FLAG

for key in tqdm(KEYS):
    # manually encrypt so it doesn't use padding: also good RSA intro
    pub_nums = key.public_key().public_numbers()
    e = pub_nums.e
    n = pub_nums.n
    keylength = math.ceil(n.bit_length() / 8)
    message = int.from_bytes(ciphertext, byteorder='big')
    # cool thing I didn't know: pow(a, b, c) is a ^ b mod c
    encrypted = pow(message, e, n)
    ciphertext = encrypted.to_bytes(keylength, byteorder='big')
    

with open("ciphertext", 'wb') as out:
    out.write(ciphertext)

print("Complete!")
