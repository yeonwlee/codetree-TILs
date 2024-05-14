num_of_field, target_height, min_num_of_connective_field_same_height = map(int, input().split())

fields = list(map(int, input().split()))

# 미리 연속 타겟 묶음으로 높이를 더해둠
fields_height_sum = [
    sum(fields[index:index + min_num_of_connective_field_same_height]) 
    for index in range(num_of_field - min_num_of_connective_field_same_height + 1)
]

min_cost = float('inf')
target_sum = target_height * min_num_of_connective_field_same_height

for index, cur_range_sum in enumerate(fields_height_sum):
    cur_cost = abs(cur_range_sum - target_sum)
    if cur_cost == 0:
        cur_cost = sum(abs(target_height - element) 
            for element in fields[index:index+min_num_of_connective_field_same_height] 
            if element != target_height)
    min_cost = min(min_cost, cur_cost)

print(min_cost)