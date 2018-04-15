def grade(key, submission):
    if submission.lower() == 'chesternez':
        return True, "Congratuations! Well done!"
    else:
        return False, "No dice! Nada! Nil! Falsa! Erroné!"
