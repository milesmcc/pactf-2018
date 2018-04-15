"""This file demonstrates a solution to the problem: a full plaintext recovery without using the
private/ folder with the actual key data, using only data that any competitor would be able to
access."""


import math

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa

PUB_EXP = 65537  # known from public key

# first import keys
keys = []
for i in range(20):
    with open(f"public/key{i}.pem", 'rb') as key_file:
        keys.append(serialization.load_pem_public_key(key_file.read(), default_backend()))

moduli = [key.public_numbers().n for key in keys]
# these are completely unfactorable unless we use GCD

# get pairs that share a factor
pairs = []
for i in range(len(moduli)):
    for j in range(i):
        a, b = moduli[i], moduli[j]
        if math.gcd(a, b) != 1:
            pairs.append((i, j))


# now, check that everything got in a pair
assert(len(pairs) == 10)
assert(all([any([x in pair for pair in pairs]) for x in range(len(moduli))]))

# factor each one using its associated partner
# the distinction between p and q is arbitrary: here, as in the encoder, p is the GCD one
p_list = [0 for i in range(len(moduli))]
q_list = [0 for i in range(len(moduli))]

for i, j in pairs:
    n1 = moduli[i]
    n2 = moduli[j]
    p = math.gcd(n1, n2)
    q1 = n1 // p
    q2 = n2 // p
    p_list[i] = p
    p_list[j] = p
    q_list[i] = q1
    q_list[j] = q2


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


    
# now get keys from p and q
# again, this one requires a little bit of math
def gen_key(e, p, q):
    # n = pq
    n = p * q
    # d = e^-1 mod (p-1)(q-1)
    d = mulinv(e, (p - 1) * (q - 1))
    dmp1 = rsa.rsa_crt_dmp1(d, p)
    dmq1 = rsa.rsa_crt_dmq1(d, q)
    iqmp = rsa.rsa_crt_iqmp(p, q)
    public_nums = rsa.RSAPublicNumbers(e, n)
    private_nums = rsa.RSAPrivateNumbers(
        public_numbers=public_nums,
        p=p,
        q=q,
        d=d,
        dmp1=dmp1,
        dmq1=dmq1,
        iqmp=iqmp,
    )
    return private_nums.private_key(default_backend())


# this is it! the private keys!
keys = [gen_key(PUB_EXP, p, q) for p, q in zip(p_list, q_list)]

# now decrypt message, working in reverse
with open("ciphertext", 'rb') as code:
    flag = int.from_bytes(code.read(), byteorder="big")
    for key in reversed(keys):
        # manually decode like we manually encoded to avoid padding
        # use big-endian order for consistency
        # note this is the whole point of RSA: raising our ciphertext to the d power gives us the
        # original, because m^(ed) mod n = m
        d = key.private_numbers().d
        n = key.public_key().public_numbers().n
        flag = pow(flag, d, n)
    flag = flag.to_bytes(math.ceil(n.bit_length() / 8), byteorder="big")

print(flag.decode().replace('\x00', ''))
# prints the flag
