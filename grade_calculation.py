# calculates grade based on info in data_storage.py
# module contains functions used in the calculation of the degree class

def grade_calculate(grades):
    total = 0
    for key, value in grades.items():
        course_code = key[::-1]  # reverse course code key in case course code starts with 2 letters
        if int(course_code[2]) == 1:
            pass
        if int(course_code[2]) == 2:
            total = total + (value[0] * value[1])
        if int(course_code[2]) >= 3:
            total = total + (2 * value[0] * value[1])
    return total


# calculates number of credits done based on info in data_storage.py

def course_counter(grades):
    counter = 0
    for key, value in grades.items():
        counter = counter + value[0]
    return counter


# calculates QA grade based on info in data_storage.py


def quality_assurance(grades):
    sixty_credits = 240  # highest possible score, so item will be appended at least once
    thirty_credit_lst = []
    for key, value in grades.items():
        if value[0] == 60 and sixty_credits >= value[0] * value[1]:
            sixty_credits = value[0] * value[1]
        elif value[0] == 30:
            thirty_credit_lst.append(value[0] * value[1])
    thirty_credit_lst.sort()
    if thirty_credit_lst:
        thirty_credits = thirty_credit_lst[0] + thirty_credit_lst[1]
    else:
        thirty_credits = 0
    if thirty_credits == 0:
        quality_score = sixty_credits
    elif thirty_credits >= sixty_credits != 0:
        quality_score = sixty_credits
    else:
        quality_score = thirty_credits
    return quality_score


def degree_class_check(grade, quality):
    if quality <= 60 and grade <= 630:
        degree_class = "First"
    elif quality <= 120 and grade <= 900:
        degree_class = "2:1"
    elif quality <= 180 and grade <= 1170:
        degree_class = "2:2"
    elif quality <= 240 and grade <= 1440:
        degree_class = "Third"
    else:
        degree_class = "Unexpected error - you should not be here!"
    return degree_class
