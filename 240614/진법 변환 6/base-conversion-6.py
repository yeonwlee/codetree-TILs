def change_to_digit(number:str, formation:int) -> int:
    digit = 0
    for pow_value, num_pos in enumerate(number):
        remain = reverse_number_range[num_pos]
        digit += remain * pow(formation, pow_value)
    
    return digit
    

def change_digit_to_target_formation(number:int, formation:int) -> str:
    front, remain = divmod(number, formation)
    return str(front) + str(number_range[remain])


formation, number, target_formation = input().split()
formation, target_formation = int(formation), int(target_formation)

# 숫자 범위
number_range = {num:num for num in range(10)}
number_range.update({index:chr(ascii) for index,ascii in enumerate(range(ord('a'), ord('z') + 1), start=10)})
reverse_number_range = {value:key for key, value in number_range.items()}

# 10진수로 전환(기준)
digit_number = change_to_digit(number, formation)

# 타겟 진수로 전환
print(change_digit_to_target_formation(digit_number, target_formation))