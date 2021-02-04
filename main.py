from grade_calculation import grade_calculate, course_counter, quality_assurance, degree_class_check
from data_storage import stg2_grades, stg3_grades
from random import randint

# randomise grade scores for testing - remove when sure code is correct
for value in stg2_grades.values():
    value[1] = randint(1, 4)
for value in stg3_grades.values():
    value[1] = randint(1, 4)
print(stg2_grades)
print(stg3_grades)

num_courses = course_counter(stg2_grades) + course_counter(stg3_grades)

if num_courses > 240:
    print(f"Too many credits entered!")

elif num_courses < 240:
    print(f"Too few credits entered!")

else:
    stage_2 = grade_calculate(stg2_grades)
    stage_3 = grade_calculate(stg3_grades)

    final_grade = stage_2 + stage_3
    print(f"Final credit mark is {final_grade}")

    quality_check = quality_assurance(stg3_grades)
    print(f"Quality score is {quality_check}")

    degree_class = degree_class_check(final_grade, quality_check)
    print(f"Your degree class is {degree_class}")
