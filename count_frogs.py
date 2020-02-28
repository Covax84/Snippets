from functools import reduce


def reduce_count_frogs(year: int) -> int:
    """ There is a 120 frogs in a swamp at year 1.
        Every year 50 frogs are caught, 
        the remaining frogs double the population.
        
        Input: year(years passed since year 1)
        Output: frogs population for specified year 
    """
    return reduce(lambda x, y: (x-50)*2, range(year-1), 120)


def recurrent_count_frogs(year: int) -> int:
    """ There is a 120 frogs in a swamp at year 1.
        Every year 50 frogs are caught, 
        the remaining frogs double the population.
        
        Input: year(years passed since year 1)
        Output: frogs population for specified year 
    """
    if year == 1:
        return 120
    return (recurrent_count_frogs(year - 1) - 50) * 2


# print(recurrent_count_frogs(99))

# print(reduce_count_frogs(99))
