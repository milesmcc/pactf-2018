def grade(key, submission):
    if submission == "the_real_answer_is_always_in_the_comments":
        return True, "Just ask HackerNews or Reddit!"
    else:
        return False, "Keep trying..."
