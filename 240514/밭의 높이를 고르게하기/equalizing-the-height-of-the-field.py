num_of_feild, target_height, minimum_num_of_connective_field_same_height = map(int, input().split())

fields = list(map(int, input().split()))
# 미리 연속 타겟 묶음으로 높이를 더해둠
fields_height_sum = [sum(fields[index:index+minimum_num_of_connective_field_same_height]) for index in range(num_of_feild - minimum_num_of_connective_field_same_height + 1)]

minimum_cost = float('inf')
for index, cur_range_sum in enumerate(fields_height_sum):
    cur_cost = abs(cur_range_sum - (target_height * minimum_num_of_connective_field_same_height))
    if cur_cost == 0:
        cur_cost = sum(abs(target_height - element) for element in fields[index:index+minimum_num_of_connective_field_same_height] if element != target_height)
    minimum_cost = min(minimum_cost, cur_cost)

print(minimum_cost)