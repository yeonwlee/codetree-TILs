num_of_field, target_height, min_num_of_connective_field_same_height = map(int, input().split())

fields = list(map(int, input().split()))

min_cost = float('inf')
for index in range(len(fields) - min_num_of_connective_field_same_height + 1):
    cur_cost = 0
    for in_range_index in range(index, index + min_num_of_connective_field_same_height):
        cur_cost += abs(target_height - fields[in_range_index])
    min_cost = min(min_cost, cur_cost)

print(min_cost)