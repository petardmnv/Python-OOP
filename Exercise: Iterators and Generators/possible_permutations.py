from itertools import permutations


def possible_permutations(l: list):
    res = permutations(l)
    for r in res:
        yield list(r)
