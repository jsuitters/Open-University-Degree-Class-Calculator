from grade_calculation import grade_calculate, course_counter, quality_assurance, degree_class_check
from data_storage import stg2_grades, stg3_grades, fill_grades_dict
# from tests import random_test

fill_grades_dict(stg2_grades, 2)  # stage 2
fill_grades_dict(stg3_grades, 3)  # stage 3
# random_test(stg2_grades)
# random_test(stg3_grades)

num_courses = course_counter(stg2_grades) + course_counter(stg3_grades)

if num_courses < 240:
    credits_short = 240 - num_courses
    print(f"Too few credits entered! You need to add {credits_short} additional credits.")

elif num_courses > 240:
    credits_over = num_courses - 240
    print(f"Too many credits entered! You need to remove {credits_over} credits.")


else:
    stage_2 = grade_calculate(stg2_grades)
    stage_3 = grade_calculate(stg3_grades)

    final_grade = stage_2 + stage_3
    print(f"Final credit mark is {final_grade}")

    quality_check = quality_assurance(stg3_grades)
    print(f"Quality score is {quality_check}")

    degree_class = degree_class_check(final_grade, quality_check)
    print(f"Your degree class is: {degree_class}")
