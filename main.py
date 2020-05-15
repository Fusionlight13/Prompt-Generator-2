row_types = []
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


def main_func(questions, answers):
    current_question = 0
    possible_error = size_detection(questions, answers)


if __name__ == '__main__':
    main_func(questions=['q1', 'q2'], answers=[['Yes', 'no'], [None]])
# questions = main_func(questions=['What is your name? ', 'Is this your first time? ', 'How old are you? ',
                                     # 'Will you quit? '], answers=[[None], ['Yes', 'No'], [None], ['of course', 'no I will not.']], declaredNontype=['str', 'int'], questionIndex=(0, 2))
