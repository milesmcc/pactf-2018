# RC4 Reused Key
This is a simpler version of a problem I was going to write implementing the Fluhrer-Mantin-Shamir
attack, but that isn't feasible without a server.

The problem simply asks you to recognize that the given encryption program uses a stream
cipher. Once you know that, all you have to do is just XOR the given messages, and then XOR the
hex code of the first plaintext and convert back to ASCII. (Specifically, it uses RC4, but that's
not important to the problem: it might aid in recognition, however.)

Here's the output of the given encryptor program that I used:

```
Please enter a key (ASCII text): 
pactf-key31415
Message to encrypt: 
TheCodeSamurai subscribed for 3 months! Thank you, TheCodeSamurai!
Your coded message (in hexadecimal) is:
C1D7B5D06DD88D0F894E592B0A5FDB93C4F151C04BC2540D8626E5B0017D604E33ABC51334662B8ED8CCADE9B039AE4FB5F363EA9EDD32D551C32A892B058CDE8B0B
Please enter a key (ASCII text): 
pactf-key31415
Message to encrypt: 
a_waterfall_is_just_a_stream_on_its_side
Your coded message (in hexadecimal) is:
F4E0A7F276D99A3A894F40060245A48AC4E056FC58F4451C9063E2B22C323D3137B0D8382F7C6ECB
```

## Flag
The flag is `a_waterfall_is_just_a_stream_on_its_side`.

