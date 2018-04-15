from hashlib import md5
from itertools import product
from string import ascii_lowercase as alphabet

# used for a progress bar so you can see if you should stop this or not
from tqdm import tqdm

HASH = "eca065fba51916821eb7274c786c67d9"

ans = ""
for word in tqdm(product(alphabet, repeat=6), total=26 ** 6):
    if md5(str.encode(''.join(word))).hexdigest() == HASH:
        ans = ''.join(word)
        break

print()
print(ans)
print()
