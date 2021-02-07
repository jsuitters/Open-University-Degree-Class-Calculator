# this file contains a dictionary with previously completed modules grades

import csv


def fill_dict(grades_2, grades_3):
    with open('Grades.csv', 'r') as csv_file:
        csv_read = csv.reader(csv_file)
        next(csv_read)
        for line in csv_read:
            course_col = line[0]
            course_code = course_col[::-1]
            if course_code[2] == str(2):
                grades_2[line[0]] = [int(line[1]), int(line[2])]
            elif course_code[2] >= str(3):
                grades_3[line[0]] = [int(line[1]), int(line[2])]


stg2_grades = {}
stg3_grades = {}
fill_dict(stg2_grades, stg3_grades)

"""
# stage 3 with 4 30 credit modules
stg2_grades = {"T229": [30, 1], "T271": [30, 1], "T272": [30, 1], "T276": [30, 1]}
stg3_grades = {"T329": [30, 1], "T356": [30, 1], "T367": [30, 1], "T452": [30, 1]}



# stage 3 with 1 60 credit module and 2 30 credit modules
stg2_grades = {"T229": [30, 1], "T271": [30, 1], "T272": [30, 1], "T276": [30, 1]}
stg3_grades = {"T329": [60, 1], "T367": [30, 1], "T452": [30, 1]}


# stage 3 with 2 60 credit modules
stg2_grades = {"T229": [30, 1], "T271": [30, 1], "T272": [30, 1], "T276": [30, 1]}
stg3_grades = {"T329": [60, 1], "T452": [60, 1]}

"""
