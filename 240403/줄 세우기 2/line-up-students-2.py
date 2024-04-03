class Student:
    def __init__(self, height, weight, id_number):
        self.height = height
        self.weight = weight
        self.id_number = id_number


num_of_students = int(input())
students = []

for id_number in range(1, num_of_students + 1):
    height, weight = map(int, input().split())
    students.append(Student(height, weight, id_number))

students.sort(key=lambda student: (student.height, -student.weight))

for student in students:
    print(student.height,student.weight, student.id_number)