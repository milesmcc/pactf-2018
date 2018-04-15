def grade(key, submission):
    if submission == "big_brother_is_looking_at_your_photos":
        return True, "Remember to clear your EXIF!"
    else:
        return False, "Keep looking..."
