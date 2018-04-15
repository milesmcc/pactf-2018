def grade(key, submission):
	submission = submission.replace('flag:', '').strip()
	if submission == "scrambled_a_byte_902_102__910_917_102_104_1042":
		return True, "Scrambled eggs. Yum!"
	else:
		return False, "Keep trying..."
