def grade(key, submission):
    if submission == "it_is_only_uphill_from_here_%s" % str(key):
        return True, "Good luck!"
    else:
        return False, "Ask Julius again..."
