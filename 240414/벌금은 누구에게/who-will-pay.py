num_of_students, student_id_get_punishment, punishment_count_to_pay_fine = map(int, input().split())

student_punishment_info = [
    int(input())
    for _ in range(student_id_get_punishment)
]

student_punishment_count = [
    0 for _ in range(num_of_students)
]

max_punishment_count = 0

for student_id in student_punishment_info:
    student_punishment_count[student_id - 1] += 1
    if max_punishment_count < student_punishment_count[student_id - 1]:
        max_punishment_count = student_punishment_count[student_id - 1]
        if max_punishment_count >= punishment_count_to_pay_fine:
            print(student_id)
            break

if max_punishment_count < punishment_count_to_pay_fine:
    print(student_id) #아무도 벌금을 내는 학생이 없는 경우