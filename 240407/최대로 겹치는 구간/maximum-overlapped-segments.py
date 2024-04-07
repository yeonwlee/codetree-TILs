def change_point_to_plus_num(str_num_value: str, condition_num: int = 100) -> int:
    return int(str_num_value) + condition_num


num_of_lines = int(input())
point_info = [0 for _ in range(200)] #조건은 -100 ~ 100
lines = [
    tuple(map(change_point_to_plus_num, input().split()))
    for _ in range(num_of_lines)
]

for line in lines:
    start, end = line
    for index in range(start - 1, end - 1): # 마지막 점은 구간으로 취급X 
        point_info[index] += 1

print(max(point_info))