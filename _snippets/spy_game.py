def spy_game(arr: list):
    """ input: list of integers
        output: true if list contains sequence 0, 0, 7
    """
    return (''.join(str(x) for x in arr)).find('007') != -1


my_list = [0, 0, 1, 2, 3, 0, 0, 2, 0, 0, 7, 1, 2, 3]
print(spy_game(my_list))
