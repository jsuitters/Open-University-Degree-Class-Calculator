# file contains functions for generating random grade numbers to add to grades in data_storage.py
from random import randint


def random_test(grades):
    for val in grades.values():
        val[1] = randint(1, 4)
    return grades

'''
# randomise grade scores for testing | paste into main.py when required
# remember to import test.py into main.py
stg2_grades = random_test(stg2_grades)
print(stg2_grades)
stg3_grades = random_test(stg3_grades)
print(stg3_grades)
'''