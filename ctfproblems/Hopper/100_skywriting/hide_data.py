"""This file runs steganography on the given .wav file to produce 20 files, one of which has good
data and the rest which have random garbage."""

import random

from sub_cipher import ciphertext
from WavSteg import hide_data

N_FILES = 20
secret_file_num = random.randrange(0, 20)
print(secret_file_num)

cipherdata = bytes(ciphertext, 'utf8')
data_len = len(cipherdata)

texts = []
for i in range(20):
    if i != secret_file_num:  # no fancy data, just random garbage
        garb = []
        for i in range(data_len):
            garb.append(random.randint(0, 255))
        texts.append(bytes(garb))
    else:  # use actual data
        texts.append(cipherdata)

for i in range(20):
    with open("bits/{}.dat".format(i), 'wb') as out:
        out.write(texts[i])

SOUND_PATH = "gusty-garden-galaxy.wav"
DATA_PATH = "bits/{}.dat"
OUT_PATH = "static/gusty-garden-galaxy-{}.wav"

for i in range(20):
    hide_data(SOUND_PATH, DATA_PATH.format(i), OUT_PATH.format(i), 1)
