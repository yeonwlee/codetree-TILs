phone_number = input().split("-")
phone_number[2], phone_number[1] = phone_number[1], phone_number[2]
print("-".join(phone_number))