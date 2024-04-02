personal_info = [
    input().split()
    for _ in range(5)
]

ordered_by_name = sorted(personal_info, key=lambda x: x[0])
ordered_by_height = sorted(personal_info, key=lambda x: -int(x[1]))

print("name")
for person in ordered_by_name:
    name, height, weight = person
    print(name, height, format(float(weight), ".1f"))

print()

print("height")
for person in ordered_by_height:
    name, height, weight = person
    print(name, height, format(float(weight), ".1f"))