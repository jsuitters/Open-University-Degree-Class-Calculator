import grade_calculation
import data_storage
# from tests import random_test

data_storage.fill_grades_dict(data_storage.stg2_grades, 2)  # stage 2
data_storage.fill_grades_dict(data_storage.stg3_grades, 3)  # stage 3
# random_test(stg2_grades)
# random_test(stg3_grades)

num_courses = grade_calculation.course_counter(data_storage.stg2_grades) +\
              grade_calculation.course_counter(data_storage.stg3_grades)

if num_courses < 240:
    credits_short = 240 - num_courses
    print(f"Too few credits entered! You need to add {credits_short} additional credits.")

elif num_courses > 240:
    credits_over = num_courses - 240
    print(f"Too many credits entered! You need to remove {credits_over} credits.")


else:
    stage_2 = grade_calculation.grade_calculate(data_storage.stg2_grades)
    stage_3 = grade_calculation.grade_calculate(data_storage.stg3_grades)

    final_grade = stage_2 + stage_3
    print(f"Final credit mark is {final_grade}")

    quality_check = grade_calculation.quality_assurance(data_storage.stg3_grades)
    print(f"Quality score is {quality_check}")

    degree_class = grade_calculation.degree_class_check(final_grade, quality_check)
    print(f"Your degree class is: {degree_class}")
