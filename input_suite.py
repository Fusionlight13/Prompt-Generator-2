from sys import exit

user_data = []


def continuous_input(required_info, ex_type='str', ex_command='/s'):
    user_input = ''
    answers = []
    loop_iteration = 0
    while user_input != ex_command:
        loop_iteration += 1
        user_input = input(f'{required_info} ({loop_iteration}): ')
        if user_input == ex_command:
            break
        if ex_type == 'int':
            try:
                convert_data = int(user_input)
                answers.append(convert_data)
            except ValueError as ex:
                print(ex)
                loop_iteration -= 1
        else:
            answers.append(user_input)
    return answers


def menu_maker(nav_options, input_text='Enter an option: '):
    user_input = 0
    mapped_input = {}
    used_map = {}
    for i in range(len(nav_options)):
        mapped_input[i + 1] = nav_options[i]
    while user_input not in range(1, len(nav_options) + 1):
        for option_count in range(len(nav_options)):
            print(f'{option_count + 1}) {nav_options[option_count]}')
        try:
            user_input = int(input(input_text))
        except ValueError as ex:
            print(ex)
    used_map[user_input] = mapped_input[user_input]
    return used_map


def define_types(answers):
    #Checks for identical data types.
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

"""
    Questions: Must be a list but the length can be less than two. Questions and Answers must be of the same length. Ex: 2 questions and 2 pairs of answers.
    Answers: Must be a 2d matrix [[]]. Each answer pair inside of the main array can be any of length. Each pair must have the same data type. EXCEPTION RAISED. To have a custom input, use [None].
    none_type: Is REQUIRED for each none specified in Answers. Types must be in an array: ['str', 'int']. None's must match the none_type.
    question_index: Converts text input of specified question count in an integer response corresponding to the length of answers given. If only one question is listed, an array is not required.

"""
def main_func(questions, answers, none_type=None, question_index=None):
    #
    error_handling(questions, answers)
    current_row = -1
    noneType = -1
    current_question = 0
    for question in questions:
        current_question += 1
        numbered_answers = False
        user_input = ''
        current_row += 1
        choices_given = 0
        if answers[current_row][0] is not None:
            while user_input not in answers[current_row]:
                if question_index is not None:
                    if not isinstance(question_index, list):
                        if question_index == current_question:
                            numbered_answers = True
                    elif question_index[current_row] == current_question:
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
            noneType += 1
            if isinstance(none_type, list):
                if none_type[noneType] == 'str':
                    user_input = str(input(question))
                    user_data.append(user_input)
                elif none_type[noneType] == 'int':
                    not_error = True
                    while not_error:
                        try:
                            user_input = int(input(question))
                            user_data.append(user_input)
                            not_error = False
                        except ValueError as ex:
                            print(ex)
            elif none_type == 'str':
                ser_input = str(input(question))
                user_data.append(user_input)
            elif none_type == 'int':
                not_error = True
                while not_error:
                    try:
                        user_input = int(input(question))
                        user_data.append(user_input)
                        not_error = False
                    except ValueError as ex:
                        print(ex)
    return user_data


all_surveys = []
for person in range(1, 3 + 1):
    print('Survey', len(all_surveys) + 1)
    main_menu = main_func(['Are you older than 18? ', 'How would you rate this product? ', 'Would you have any ideas of how you could improve this product? '], answers=[['Yes', 'No'], ['One star', 'Two stars', 'Three stars', 'Four stars', 'Five stars'], [None]], none_type=['str'], question_index=2)
    all_surveys.append(main_menu)
print(all_surveys)
