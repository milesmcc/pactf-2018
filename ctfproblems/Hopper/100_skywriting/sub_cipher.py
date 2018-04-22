"""This file encodes given English text in a substitution cipher that uses variable-length
substitutions to reduce the effectiveness of frequency analysis. However, certain characters only
appear in certain patterns, which is enough to deduce the breakup and then apply standard
substitution cipher techniques."""

from string import ascii_letters as alphabet

# just the letters A-Z
CIPHER = [
    "∫∇",
    "=",
    "𝗑",
    "𝝘",
    "⅞𝝽",
    "=x",
    "xx",
    "½",
    "λ𒀪",
    "++",
    "--",
    "//",
    "✕✕",
    "⊻⊻⊻",
    "<<",
    "<>",
    "<=>",
    ">>",
    "🞇🞑",
    "🞐🞐",
    "🢛🢙",
    "🢛🢚",
    "Λ𝞼",
    "𝚺𝚺",
    "𝞢𝞢",
    "𝞢𝞂Δ",
]

def encode(text):
    """Removes punctuation, maps each character to the substitution cipher, and then returns the
    full thing, with newlines preserved."""
    ans = []
    for char in text:
        if char == '\n':
            ans.append('\n')
        elif char in alphabet:
            ans.append(CIPHER[alphabet.find(char) % 26])
        elif char in "0123456789-_":
            ans.append(char)
    return ''.join(ans)


ciphertext = encode("""
You have done well to get here so far! Sadly, you are not done yet. Here is a poem to get you in the
right frame of mind.

I wandered lonely as a cloud
That floats on high o'er vales and hills
When all at once I saw a cloud
A host, of golden daffodils.
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze.

Continuous as the stars that shine
and twinkle on the Milky Way,
They stretched in never-ending line
along the margin of a bay:
Ten thousand saw I at a glance,
tossing their heads in sprightly dance.

The waves beside them danced; but they
Out-did the sparkling waves in glee:
A poet could not but be gay,
in such a jocund company:
I gazed—and gazed—but little thought
what wealth the show to me had brought:

For oft, when on my couch I lie
In vacant or in pensive mood,
They flash upon that inward eye
Which is the bliss of solitude;
And then my heart with pleasure fills,
And dances with the daffodils.

-- William Wordsworth

Keep going.

Don't be evil.

Here are two clues to the documents you will need. Keep your head in the clouds.

1H7kFQ2ozQI_3qm4-HoxDEL_1jnMrC3b8WlCjJv-rtok
1YwNxq0cd-cs6fPykiqbyDkGhzkQ3MBtfuBjk8ciPzz8
""")
