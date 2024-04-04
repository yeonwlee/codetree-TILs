binary_num = input()
result: int = 0

for index, cur_position_num in enumerate(binary_num[::-1]):
    if cur_position_num == "1":
        result += 2 ** index

print(result)