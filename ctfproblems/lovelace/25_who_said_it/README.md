# Who Said It?

This problem presents the competitor with a PGP signed text. The competitor uses a signature verification system (like GPG Tools) to determine that the fingerprint of the signing key is `4CD0 3F6E FD23 E1E9`. The competitor then searches for this PGP key in all the major key servers, and then eventually find the [key](https://pgp.surfnet.nl/pks/lookup?op=vindex&fingerprint=on&search=0xA0A07E95911CDA5F). They notice that the key has the comment `the_real_answer_is_always_in_the_comments`. This is the flag.

The flag is `the_real_answer_is_always_in_the_comments`.
