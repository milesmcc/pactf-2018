# Victor

The [VIC cipher](https://en.wikipedia.org/wiki/VIC_cipher) was a hand cipher used by a Soviet spy named Reino Häyhänen (whose codename was VICTOR).

This problem provides competitors with the decoding table, the secret key, and the encoded message. Because no trial and error is required—that is, provided contestants recognize that this is indeed a VIC cipher, the problem is immediately solvable (there is no frequency analysis necessary, for example)—the problem is not very difficult.

Competitors know that this is a VIC cipher because its creator—Reino, codename Victor—is mentioned in the problem description. (In Russian, which they can easily use Google Translate to translate.) The competitor should then read its Wikipedia page, where the encryption process—and therefore the decryption process—is explained.

The competitor knows that during the encryption process, the secret was _added_ (прибавление means 'addition'). They know that this was modulus addition on the expanded secret because they read the Wikipedia page.

We start by performing a modulus subtraction from the encoded message with the expanded secret:

```
  7264160199640987865519282923616105
- 1226199112261991122619911226199112
= 6048071087489096743900371707527093
```

This yields the encoded message. By consulting the table provided in the image and knowledge of how the cipher works, the competitor tokenizes and then decodes the message:

`6048071087489096743900371707527093` becomes `6 04 8 07 1 08 74 8 90 96 74 3 90 03 71 70 75 2 70 93`

`6 04 8 07 1 08 74 8 90 96 74 3 90 03 71 70 75 2 70 93` becomes `сделайте_это_вручную`.

`сделайте_это_вручную` is the flag.
