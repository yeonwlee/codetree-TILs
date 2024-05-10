numbers = {num for num in range(1, 31)}

for _ in range(28):
    cur_input_num = int(input())
    numbers.remove(cur_input_num)

print(min(numbers))
print(max(numbers))