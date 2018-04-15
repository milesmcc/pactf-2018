def grade(key, submission):
    if submission == ("Gotza_Makes_1T_V_small_%s" % str(key)):
        return True, "Gotta make it very small."
    else:
        return False, "Keep trying..."