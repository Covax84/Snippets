def permutations(n: int, m: int = -1, prefix=None):
    """ generate permutations """
    m = n if m == -1 else m
    prefix = prefix or []
    if m == 0:
        return print(*prefix)
    for digit in range(1, n + 1):
        if digit in prefix:
            continue            # условие генерации без повторов
        prefix.append(digit)
        permutations(n, m - 1, prefix)
        prefix.pop()
