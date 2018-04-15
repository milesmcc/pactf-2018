import pickle
import zlib
from random import randint
import pdb
import base64

def generate(key):
	key = "Gotza_Makes_1T_V_small_%s" % str(key)
	pk = pickle.dumps({"flag": key})
	pk = pk[2:]
	for i in range(randint(10, 100)):
		pk = zlib.compress(pk)
	pk = base64.b64encode(pk)
	return ("""My friend gave me [this file](data:application/zip;base64,%s), but I have no idea what to do with it?"""%str(pk)[2:-1],
			"""I tried to make this file really, really small.""")


'''
ANSWER

for i in range(1, 100):
	try:
		pk = zlib.decompress(pk)
	except:
		print(pk)
'''