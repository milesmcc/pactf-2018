def grade(key, submission):
    if submission == 'write your own music' or submission == "WRITE YOUR OWN MUSIC":
        return True, "Exactly!"
    else:
        return False, "No :( Why should Martin not buy melody packs?"
