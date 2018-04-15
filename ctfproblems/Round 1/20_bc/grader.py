def grade(key, submission):
    if submission.lower() == 'cassius':
        return True, "Nice job! You are the noblest of them all!"
    else:
        return False, "Sorry, that isn't correct! Maybe a classic piece of literature would soothe your psyche..."
