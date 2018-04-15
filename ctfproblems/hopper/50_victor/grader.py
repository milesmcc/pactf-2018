def grade(key, submission):
    if submission == 'сделайте_это_вручную':
        return True, "Отличная работа. Correct!"
    else:
        return False, "Будьте лучше. Try again."
