def grade(key, submission):
    if submission == 'last bits matter':
        return True, "Nice job! You found the needle in the haystack!"
    else:
        return False, "Sorry, that isn't right! Looks can be deceiving..."
