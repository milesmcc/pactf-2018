def hash_it(string):
    q = 0
    z = 127
    for i in [int(byte) for byte in bytearray(string, "utf-8")]:
        q += i
        z *= i
    return (((q << 3)+1)*z) % (2**32 - 1)

def grade(key, submission):
    try:
        if hash_it(submission) == 293366475:
            return True, "You killed the hash!"
        else:
            return False, "Keep hashing..."
    except:
        return False, "an error != success"
