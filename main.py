row_types = []
user_data = []


def size_detection(questions, answers):
    error_bool = True
    question_len = len(questions)
    answer_len = len(answers)
    answer_ints = 0
    answer_types(answers)
    # print(f'question length: {question_len}, answer length: {answer_len}')
    if question_len == answer_len:
        error_bool = False
    for row_status in row_types:
        if row_status == 'UTRT':
            error_bool = True
    return error_bool


def answer_types(answers):
    global row_types
    int_increments = 0
    str_increments = 0
    for answer in range(len(answers)):
        skip_type = False
        current_len = len(answers[answer])
        for item in answers[answer]:
            if isinstance(item, int):
                int_increments += 1
            elif isinstance(item, str):
                str_increments += 1
            elif item is None:
                skip_type = True
        if current_len == int_increments:
            row_types.append('io')
            str_increments = 0
            int_increments = 0
        elif current_len == str_increments:
            row_types.append('so')
            str_increments = 0
            int_increments = 0
        elif skip_type:
            row_types.append('sk')
            int_increments = 0
            str_increments = 0
        else:
            row_types.append('UTRT')


def main_func(questions, answers, declaredNontype, questionIndex):
    possible_error = size_detection(questions, answers)
    current_column = -1
    number_incrementals = False
    current_non_type = -1
    current_question = 0
    user_input = ''
    if possible_error:
        print('Argument or types do not match!')
    else:
        for question in questions:
            current_column += 1
            choice_adding = 0
            current_question += 1
            number_incrementals = False
            try:
                if answers[current_column][0] is not None:
                    while user_input not in answers[current_column]:

                        if questionIndex[current_column] == current_question:
                            number_incrementals = True
                        for choice in answers[current_column]:
                            if not number_incrementals:
                                print(choice)
                        if number_incrementals:
                            while user_input not in range(1, choice_adding + 1):
                                choice_adding = 0
                                for choice in answers[current_column]:
                                    choice_adding += 1
                                    print(f'{choice_adding}) {choice}')
                                try:
                                    user_input = int(input(question))
                                    user_data.append(user_input)
                                except ValueError as ex:
                                    print(ex)
                            break
                        else:
                            user_input = input(question)
                else:
                    current_non_type += 1
                    if declaredNontype[current_non_type] == 'str':
                        user_input = str(input(question + '(*Expected type: str): '))
                        user_data.append(user_input)
                    elif declaredNontype[current_non_type] == 'int':
                        user_input = int(input(question + '(*Expected type: int): '))
                        user_data.append(user_input)
            except IndexError as ex:
                print(ex)
    return user_data


if __name__ == '__main__':
    questions = main_func(questions=['What is your name? ', 'Is this your first time? ', 'How old are you? ',
                                     'Will you quit? '], answers=[[None], ['Yes', 'No'], [None], ['of course', 'no I will not.']], declaredNontype=['str', 'int'], questionIndex=(0, 2))