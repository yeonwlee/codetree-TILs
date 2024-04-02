class Student:
    def __init__(self, name, subject1, subject2, subject3):
        self.name = name
        self.subject1 = int(subject1)
        self.subject2 = int(subject2)
        self.subject3 = int(subject3)

    def sum_points(self):
        return sum(getattr(self, attr) for attr in ['subject1', 'subject2', 'subject3'])


num_of_students = int(input())
students = []
for _ in range(num_of_students):
    student_info = input().split()
    students.append(Student(student_info[0], student_info[1], student_info[2], student_info[3]))

students.sort(key=lambda x: x.sum_points())

for student in students:
    print(*student.__dict__.values())