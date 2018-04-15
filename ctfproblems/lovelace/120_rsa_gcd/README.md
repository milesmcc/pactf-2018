# Trial By RSA: GCD Attack On Multiple Keys
The problem is to decode a message encoded with not just one, but twenty RSA-4096 keys. As far as I
know, each individual key is completely secure: if it isn't, that needs to be fixed. Thus we have
quite the paradox. How can adding more RSA problems make the overall code insecure?

The `static` folder contains everything you need, zipped up (the `unzipped_static` folder contains
all of the data so it's easier to look at), and it's what the contestants get. The zip has a folder
of 20 public keys, an encoded message, and a basic guide on the format I used to encode it. (You
could take this out, and it would make it harder I guess, but if someone gets stuck because they're
missing the little-endian byte order or something I'd feel pretty badly about it. It's hard enough
as it is.) The task is simple: decode the message and read it. Decoding it simply yields ASCII text
that is the flag.

RSA, as a reminder, depends on the putative hardness of integer factorization: to be specific, the
keys I have rely on the fact that the sum total of all human computing power could not possibly
factor a 4096-bit number at the present day, even if given a million years.

Integer factorization is hard, but getting the greatest common factor of two numbers is linear via
Euclid's Algorithm! Herein lies the trick: the 20 keys actually share 10 primes in common, a pair
sharing each prime in a randomized configuration (manual inspection of the first two keys, for
example, won't reveal the trick). There are only 45 possible pairs, so after only 45 GCDs (which is
less time than generating a single key takes!) you should have factored every single key. Of course,
this requires knowing how to interconvert between RSA as it is used and RSA as a mathematical
construct: taking a PEM file back to these numbers is not trivial, and neither is unravelling the
onion layers of the encrypted file. Teams will need both scripting/coding ability and math/crypto
background to solve this. After factoring, one can then create private keys and decode the message,
layer by layer. There's no padding for the encryption, but it is big-endian which might throw some
people off: I'm not sure how to fix that. I also am vaguely sure that the no padding doesn't
introduce vulnerabilities, but I could be wrong.

Note that RSA is so widely supported that this is still platform-agnostic, although certainly mature
languages lke Python are a solid choice.

Note that, to prove this works in a reasonable timeframe (*cough* *cough* the RSA problem two years
ago), this folder has in it a Python script, `solution.py`, that operates only on the public
information and works in less than a second. You can also redo the problem creation as much as
desired with the `problem_creator.py` file, or mess around with how it's done.

## Commentary
This one is pretty brutal compared to my other submissions and the average difficulty of PACTF. The
trick is fairly rare (mention of it is made on Wikipedia, but it doesn't come up often), and it's
certainly a bit more daunting to solve even if you have an idea how it will play out. You really
aren't supposed to ever roll your own RSA, so libraries fight you tooth and nail. I think it's still
perfectly fair, but it's something to watch for.

One thing to possibly tweak is the hintiness of the hints and title. (In case my musings didn't
communicate very effectively, "siblings" is supposed to reference numbers with the same prime
factor.) It could get a bit easier, and it could get a lot harder. Right now it's definitely hard,
but I think fairly doable. If you give no hints whatsoever (make the title "RSA #1" or something
like that, no useful hint text) then it would be substantially harder, and if you gave a more
helpful hint it could get easier, although the implementation will still be tricky (e.g.,
"Generating 600-digit primes is a lot of work! What if you wanted to cut down on the number you
needed...").

## Flag
The flag is `t00 many c00ks sp0il the br0th`. I was planning to include some reference to the
saying, but I didn't. The 133t-speak prevents dumb brute forcing, I guess: keep in mind anyone can
run as many encryptions as they want, because we give them the public keys. The flag should be too
long anyways, but you never know. Plus it adds a bit of a programmer vibe! 
