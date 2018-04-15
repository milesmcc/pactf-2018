def grade(key, submission):
	if submission == ("V1gnette_%s" % str(key)):
		return True, "I love me a good Vigenere. Scrumptious!"
	else:
		return False, "Keep trying..."