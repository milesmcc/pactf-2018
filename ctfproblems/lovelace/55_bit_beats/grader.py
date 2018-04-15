def grade(key, submission):
    if submission == 'flagispactfmusic' or submission == 'pactfmusic':
        return True, "Correct!"
    else:
        return False, "Not quite! Well, at least this piece has some nice bits..."
