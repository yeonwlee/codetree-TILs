num_of_student, budget = map(int, input().split())
student_present_info = [
    tuple(map(int, input().split()))
    for _ in range(num_of_student)
]

whole_num_of_students = len(student_present_info)
# 선물값과 배송비를 합친 값, 선물 반값 쿠폰을 썼을 때의 값으로 정렬(역순. 거꾸로 꺼내기 위함)
student_present_info.sort(key=lambda x: [x[0] // 2 + x[1], x[0] + x[1]], reverse=True)
while budget > 0 and student_present_info:
    price, send_fee = student_present_info[-1]
    if budget - price - send_fee > 0:
        student_present_info.pop()
        budget -= (price + send_fee)
    elif budget - (price // 2) - send_fee > 0: # 선물 반 값 쿠폰 사용
        student_present_info.pop()
        budget -= (price // 2 + send_fee)
        break
    else: # 어떻든 선물을 못 사는 경우
        break

print(whole_num_of_students - len(student_present_info))