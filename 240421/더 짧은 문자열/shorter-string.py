str1, str2 = input().split()

if len(str1) == len(str2):
    print("equal")
else:
    min_str = min(str1, str2, key=len)
    print(min_str, len(min_str))