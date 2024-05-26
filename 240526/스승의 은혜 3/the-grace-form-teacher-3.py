num_of_student, budget = map(int, input().split())
student_present_info = [
    tuple(map(int, input().split()))
    for _ in range(num_of_student)
]

student_present_info.sort(key=lambda x: [x[0] + x[1], x[1]])
max_student_num = 0

for student_index in range(len(student_present_info) - 1, -1, -1):
    price, send_fee = student_present_info[student_index]
    apply_coupon_price = price // 2 + send_fee
    sum_price = apply_coupon_price
    students = 1
    for student_index2 in range(len(student_present_info)):
        if student_index == student_index2:
            continue
        sum_price += sum(student_present_info[student_index2])
        if sum_price >= budget:
            max_student_num = max(max_student_num, students)
            break
        students += 1
        
print(max_student_num)