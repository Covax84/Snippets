def insert_sort(a):
    """ Insert sort. """
    for top in range(1, len(a)):
        k = top
        while k > 0 and a[k - 1] > a[k]:
            a[k], a[k - 1] = a[k - 1], a[k]
            k -= 1


def choice_sort(a):
    """ Choice sort. """
    for pos in range(0, len(a) - 1):
        for k in range(pos + 1, len(a)):
            if a[k] < a[pos]:
                a[k], a[pos] = a[pos], a[k]


def bubble_sort(a):
    """ Bubble sort. """
    for bypass in range(1, len(a)):
        for k in range(0, len(a) - bypass):
            if a[k] > a[k + 1]:
                a[k], a[k + 1] = a[k + 1], a[k]


def qsort(arr: list):
    """ Hoare sort aka qsort(C) aka quicksort. """
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
    return qsort(less) + [pivot] + qsort(greater)


def my_count_sort(a: list):  # данная сортировка ограничена 10ю значениями F [0,1,2,3,4,5,6,7,8,9]
    """ Функция сортировки подсчётом. Шаг 1й - частотный анализ, шаг 2й - построение списка. """
    F = [0] * 10
    for i in range(len(a)):
        x = a[i]
        F[x] += 1
    a_sorted = ''
    for digit in range(10):
        a_sorted += (str(digit) + ' ') * F[digit]  # пробельчик добавим, чтобы работал .split
    return list(map(int, a_sorted.split()))


def test_sort(sort_algorithm):
    """ Sort algorithms testing """
    print('TESTING:' + sort_algorithm.__doc__ + '\n' + 'Test one:   ', end='')
    a = [5, 3, 2, 1, 0, 4]
    a_sorted = [0, 1, 2, 3, 4, 5]
    sort_algorithm(a)
    print('Successful' if a == a_sorted else 'Failed!!!')

    print('Test two:   ', end='')
    a = list(range(10, 15)) + list(range(5, 10))
    a_sorted = list(range(5, 15))
    sort_algorithm(a)
    print('Successful' if a == a_sorted else 'Failed!!!')

    print('Test three: ', end='')
    a = [4, 2, 1, 4, 1]
    a_sorted = [1, 1, 2, 4, 4]
    sort_algorithm(a)
    print('Successful' if a == a_sorted else 'Failed!!!')
    print('-------------------------')


test_sort(insert_sort)
test_sort(choice_sort)
test_sort(bubble_sort)
test_sort(bubble_sort)
