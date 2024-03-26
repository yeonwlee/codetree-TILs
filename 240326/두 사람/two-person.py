first_person = input().split()
second_person = input().split()
if (int(first_person[0]) >= 19 and first_person[1] == "M") or (int(second_person[0]) >= 19 and second_person[1] == "M"):
    print(1)
else:
    print(0)