class Student:
    def __init__(self, height, weight, id_number):
        self.height = int(height)
        self.weight = int(weight)
        self.id_number = int(id_number)


num_of_students = int(input())
students: Student = []
for index in range(num_of_students):
    height, weight = input().split()
    students.append(Student(height, weight, index + 1))

students.sort(key=lambda x: (-x.height, -x.weight, x.id_number))

for student in students:
    print(*student.__dict__.values())