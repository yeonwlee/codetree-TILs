num_of_students, budget = map(int, input().split())

student_present_info = [
    int(input())
    for _ in range(num_of_students)
]

num_of_whole_students = len(student_present_info)
student_present_info.sort(reverse=True)

while budget > 0:
    if budget - student_present_info[-1] < 0 and budget - student_present_info[-1] / 2 >= 0:
        student_present_info.pop()
        break
    elif budget - student_present_info[-1] >= 0:
        budget -= student_present_info.pop()

print(num_of_whole_students - len(student_present_info))