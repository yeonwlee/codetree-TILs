start_num = 185
target_num = int(input()) * 10

count_of_numbers = target_num - start_num + 1
sum_values = (start_num + target_num) * count_of_numbers / 2 #가우스 덧셈

print(f"{int(sum_values)} {round(sum_values / count_of_numbers, 1):.1f}")