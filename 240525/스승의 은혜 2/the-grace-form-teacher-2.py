num_of_students, budget = map(int, input().split())

student_present_info = [
    int(input())
    for _ in range(num_of_students)
]

num_of_whole_students = len(student_present_info)
student_present_info.sort(reverse=True) # 가장 선물비용이 적은 학생부터 거꾸로 빼나가기 위한 내림차순 정렬

while budget > 0 and student_present_info:
    if budget - student_present_info[-1] < 0 and budget - student_present_info[-1] / 2 >= 0: # 예산 내에서 선물이 불가하지만 반값 쿠폰을 적용한 경우 선물 가능한 경우
        student_present_info.pop()
        break
    elif budget - student_present_info[-1] >= 0: # 평범하게 예산 내에서 선물할 수 있는 경우
        budget -= student_present_info.pop()
    else: # 반값 쿠폰을 써도 예산 내 선물 불가한 경우
        break

print(num_of_whole_students - len(student_present_info))