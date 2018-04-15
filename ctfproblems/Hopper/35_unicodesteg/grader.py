def grade(key, submission):
    if submission == "in plain sight":
        return True, "Correct! Sometimes the most useful information is invisible!"
    else:
        return False, "Not quite! Sometimes looks can be deceiving..."
