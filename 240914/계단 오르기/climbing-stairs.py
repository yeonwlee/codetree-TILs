num = int(input())

def count_case(cur_num:int) -> int:
    if cur_num == num:
        return 1

    count = 0    
    if cur_num >= 2:
        count += count_case(cur_num - 2)
    if cur_num >= 3:
        count += count_case(cur_num - 3)
    return count


print(count_case(num))