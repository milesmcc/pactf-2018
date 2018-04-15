def grade(key, submission):
    if submission == 'flag_is_DjKVIXXQRZZrrAd' or submission == 'DjKVIXXQRZZrrAd':
        return True, "You found the hidden message."
    else:
        return False, "Keep searching."
