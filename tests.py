# file contains functions for generating random grade numbers to add to grades in data_storage.py
from random import randint


def random_test(grades):
    for val in grades.values():
        val[1] = randint(1, 4)
    return grades