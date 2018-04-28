def grade(key, submission):
    if submission == 'сделайте_это_вручную' or submission == 'СДЕЛАЙТЕ_ЭТО_ВРУЧНУЮ':
        return True, "Отличная работа. Correct!"
    else:
        return False, "Будьте лучше. Try again."
