# Clouds (Skywriting)
## Problem
The contestants are given a link to a `.7z` file holding 20 `.wav` files. They sound pretty much
the exact same, and the task is to find a flag.

(Note: the reason I use 7z is because it saves literally over 150MB compared to zip.)
## Solution
First, see that the files are different (hashes are the easiest way to tell). Then, you might assume
last-bit steganography, so you might try decoding all of them. You can then either use statistical
tests to find the least random last bits and try those (see attached file that does exactly that),
or just try each one in turn. (The correct one is number 15, by the way.)

This gives you a difficult substitution cipher problem (the dictionary used is in `sub_cipher.py` so
you can see for yourself). Lots of homoglyphs, some repeated letters, and differing lengths per
character (although AFAIK it's never ambiguous what something decodes to).

The reason that this is not bad to decode is because there's a complete poem that you can recognize
off of a couple words, which gives you pretty much everything. (At least, I think it's not bad to
decode. It still might be really hard.)

The last part is that there's a coded ID of two files. Because I give you a GDrive link at the start
and I keep talking about clouds, the idea is to use those as Google Drive IDs in links. Doing that
gives you two Google Docs files, one of which gives you the flag and the other of which
congratulates you.

## Flag
The flag is `a_cloud_is_just_someone_else’s_computer`.
