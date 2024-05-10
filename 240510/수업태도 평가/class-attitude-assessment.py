num_of_give_point_info = int(input())
student_point = {'Bessie':0, 'Elsie':0, 'Daisy':0, 'Gertie':0, 'Annabelle':0, 'Maggie':0, 'Henrietta':0}
for _ in range(num_of_give_point_info):
    student, point = input().split()
    point = int(point)
    student_point[student] += point

ordered_result = sorted([(student, point) for student, point in student_point.items()], key=lambda x: x[1])
min_point = min(ordered_result,key=lambda x:x[1])[1]
students_not_min_point = [(student, point) for student, point in ordered_result if point != min_point]
print(students_not_min_point[0][0])