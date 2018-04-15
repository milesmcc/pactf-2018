universe = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")+['_']

uni_len = len(universe)

def vign(txt='', key='', typ='d'):
	if not txt:
		print('Needs text.')
		return
	if not key:
		print('Needs key.')
		return
	if typ not in ('d', 'e'):
		print('Type must be "d" or "e".')
		return
	if any(t not in universe for t in key):
		print('Invalid characters in the key. Must only use ASCII symbols.')
		return
	ret_txt = ''
	k_len = len(key)
	for i, l in enumerate(txt):
		if l not in universe:
			ret_txt += l
		else:
			txt_idx = universe.index(l)
			k = key[i % k_len]
			key_idx = universe.index(k)
			if typ == 'd':
				key_idx *= -1
			code = universe[(txt_idx + key_idx) % uni_len]
			ret_txt += code
	return ret_txt

def generate(key):
	key = ("V1gnette_%s" % str(key))
	key = vign(key, 'itsAvIg', 'e')
	return ("""You are a military commander. Some poor intern has tried encrypting their messages to you. They gave you this string: "%s". Well now youl're gonna have to spend all afternoon on this. Sigh."""%str(key),
			"""He also scribbled the string 'it??v??' at the bottom. Not sure what that could mean. And remember to include the underscore!""")
