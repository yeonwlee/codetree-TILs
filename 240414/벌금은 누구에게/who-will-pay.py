num_of_students, student_id_get_punishment, punishment_count_to_pay_fine = map(int, input().split())

student_punishment_info = [
    int(input())
    for _ in range(student_id_get_punishment)
]

student_punishment_count = [
    0 for _ in range(num_of_students)
]

first_have_to_pay_fine_student = None
for student_id in student_punishment_info:
    student_punishment_count[student_id - 1] += 1
    if student_punishment_count[student_id - 1] >= punishment_count_to_pay_fine:
        first_have_to_pay_fine_student = student_id
        break

print(student_id if first_have_to_pay_fine_student is not None else -1)