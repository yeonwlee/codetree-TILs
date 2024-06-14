def change_to_digit(number:str, formation:int) -> int:
    digit = 0
    for pow_value, num_pos in enumerate(number[::-1]):
        remain = reverse_number_range[num_pos]
        digit += (remain * pow(formation, pow_value))
    return digit
    

def change_digit_to_target_formation(number:int, formation:int) -> str:
    changed_number = number
    answer = []
    while changed_number > formation: 
        changed_number, remain = divmod(changed_number, formation)
        answer.append(str(number_range[remain]))
    answer.append(str(number_range[changed_number]))
    return ''.join(reversed(answer)) 


formation, number, target_formation = input().split()
formation, target_formation = int(formation), int(target_formation)

# 숫자 범위
number_range = {num:str(num) for num in range(10)}
number_range.update({index:chr(ascii) for index,ascii in enumerate(range(ord('a'), ord('z') + 1), start=10)})
reverse_number_range = {value:key for key, value in number_range.items()}

# 10진수로 전환(기준)
digit_number = change_to_digit(number, formation)

# 타겟 진수로 전환
print(change_digit_to_target_formation(digit_number, target_formation))