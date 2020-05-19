nmb_List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # последовательность чисел
flg_List = [0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0]  # значение да/нет для каждого числа


def insolation_hours(hours: list, flags: list) -> list:
    """ result[0] contains values with negative flag
        result[1] contains values with positive flag
        Proper docstring is up to you :>
    """
    result = [[], []]
    positive = []
    negative = []

    for value, flag in zip(hours, flags):
        if flag:
            positive.append(value)
            if negative:
                result[0].append(negative)
                negative = []
        elif not flag:
            negative.append(value)
            if positive:
                result[1].append(positive)
                positive = []

    if positive:
        result[1].append(positive)
    elif negative:
        result[0].append(negative)

    return result


print(insolation_hours(nmb_List, flg_List))
