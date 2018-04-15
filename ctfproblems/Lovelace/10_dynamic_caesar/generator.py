try:
    maketrans = ''.maketrans
except AttributeError:
    # fallback for Python 2
    from string import maketrans

def generate(key):
    return ("The Emperor says `%s`--what could it possibly mean? I hear that he 'encrypts' numbers now too, something about appending them to the alphabet..." % caesar("it_is_only_uphill_from_here_%s" % str(key)), "Some say he's an emperor, I say he's a salad.")

def caesar(plaintext, shift=5):
    plaintext = plaintext.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)
