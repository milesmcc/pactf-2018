def grade(key, submission):
    if submission.lower() == 'sea' or submission.lower() == 'the sea':
        return True, "Yes! Miles learns Russian so he came up with the words that visually look same in both English and Russian."
    else:
        return False, "Nyet!"
