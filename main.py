from sys import exit

user_data = []


def define_types(answers):
    for row in answers:
        cutoff = False
        row_size = len(row)
        total_int = 0
        total_str = 0
        for element in row:
            if element is None:
                cutoff = True
                break
            elif isinstance(element, str):
                total_str += 1
            elif isinstance(element, int):
                total_int += 1
        if row_size == total_str:
            continue
        elif row_size == total_int:
            continue
        elif cutoff:
            continue
        else:
            return 'object types do not match'

    return 'ok'


def size_detection(questions, answers):
    total_questions = len(questions)
    total_answers = len(answers)
    if total_answers == total_questions:
        mismatch = define_types(answers)
        return mismatch
    else:
        return 'Unmatched questions to answers or vice-versa'


def error_handling(questions,answers):
    possible_error = size_detection(questions, answers)
    if possible_error == 'ok':
        return
    elif possible_error == 'Unmatched questions to answers or vice-versa':
        print(possible_error)
        exit(1)
    elif possible_error == 'object types do not match':
        print(possible_error)
        exit(1)


def main_func(questions, answers, nonetype=None, questionIndex=None):
    error_handling(questions, answers)
    current_row = -1
    nonType = -1
    current_question = 0
    for question in questions:
        current_question += 1
        numbered_answers = False
        user_input = ''
        current_row += 1
        choices_given = 0
        if answers[current_row][0] is not None:
            while user_input not in answers[current_row]:
                if questionIndex is not None:
                    if not isinstance(questionIndex, list):
                        if questionIndex == current_question:
                            numbered_answers = True
                    elif questionIndex[current_row] == current_question:
                        numbered_answers = True
                for choice in answers[current_row]:
                    if not numbered_answers:
                        print(choice)
                if numbered_answers:
                    user_input = int(0)
                    while user_input not in range(1, choices_given + 1):
                        choices_given = 0
                        for choice in answers[current_row]:
                            choices_given += 1
                            print(f'{choices_given}) {choice}')
                        try:
                            user_input = int(input(question))
                            user_data.append(user_input)
                        except ValueError as ex:
                            print(ex)
                    break
                else:
                    user_input = input(question)
                    user_data.append(user_input)
        else:
            nonType += 1
            if nonetype[nonType] == 'str':
                user_input = str(input(question))
                user_data.append(user_input)
            elif nonetype[nonType] == 'int':
                not_error = True
                while not_error:
                    try:
                        user_input = int(input(question))
                        user_data.append(user_input)
                        not_error = False
                    except ValueError as ex:
                        print(ex)
    return user_data


