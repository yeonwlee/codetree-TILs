def replace_char_at_index(source:str, target_index:int, replace_char:str) -> str:
    return source[:target_index] + replace_char + source[target_index + 1:]   


low, high = map(int, input().split())

low_num_of_pos = len(list(map(int, str(low))))
high_num_of_pos = len(list(map(int, str(high))))
suspect_numbers = set()

for digit in range(low_num_of_pos, high_num_of_pos + 1):
    all_pos_same_number = [str(try_number) * digit for try_number in range(0, 10)]
    for cur_number in all_pos_same_number:
        base_value = int(cur_number[0])
        for cur_pos in range(digit):
            for try_num in range(0, 10):
                if (cur_pos == 0 and try_num == 0) or base_value == try_num:
                    continue
                suspect_number = int(replace_char_at_index(cur_number, cur_pos, str(try_num)))
                if low <= suspect_number <= high:
                    suspect_numbers.add(suspect_number)
                
print(len(suspect_numbers))