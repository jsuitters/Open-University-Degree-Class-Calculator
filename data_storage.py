# this file contains a dictionary with previously completed modules grades pulled in from csv file

import csv


def fill_dict(grades, level):
    with open('Grades.csv', 'r') as csv_file:
        csv_read = csv.reader(csv_file)
        next(csv_read)
        for line in csv_read:
            course_col = line[0]
            course_code = course_col[::-1]
            if int(course_code[2]) == level:
                grades[line[0]] = [int(line[1]), int(line[2])]
            elif level == 3 and int(course_code[2]) == 4:  # level 3 course can have a 3 or 4 in code
                grades[line[0]] = [int(line[1]), int(line[2])]
    return grades


stg2_grades = {}
stg3_grades = {}
