money = int(input())
result = ""
if money >= 3000:
    result = "book"
elif money >= 1000:
    result = "mask"
elif money >= 500:
    result = "pen"
else:
    result = "no"
print(result)