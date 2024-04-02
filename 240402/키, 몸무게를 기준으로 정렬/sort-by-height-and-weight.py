num_of_person = int(input())
person = [
    input().split()
    for _ in range(num_of_person)
]

person.sort(key=lambda x: (int(x[1]), -int(x[2])))

for one in person:
    print(*one)