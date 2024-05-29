# str에서 특정 인덱스의 값을 변경한 str 리턴
def replace_char_at_index(source:str, target_index:int, replace_char:str) -> str:
    return source[:target_index] + replace_char + source[target_index + 1:]   

low, high = map(int, input().split())

low_num_of_pos = len(str(low)) # 최소 자리수
high_num_of_pos = len(str(high)) # 최대 자리수
suspect_numbers = set()

for digit in range(low_num_of_pos, high_num_of_pos + 1):
    for base_number in range(0, 10):
        all_same_number = str(base_number) * digit  # 유효한 자릿수만큼 똑같은 숫자로 str 생성
        for cur_pos in range(digit):
            for try_num in range(0, 10):
                if (cur_pos == 0 and try_num == 0) or base_number == try_num:
                    continue
                suspect_number = int(replace_char_at_index(all_same_number, cur_pos, str(try_num)))
                if low <= suspect_number <= high:
                    suspect_numbers.add(suspect_number)
                
print(len(suspect_numbers))