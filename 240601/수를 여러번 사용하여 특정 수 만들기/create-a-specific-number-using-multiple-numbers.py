a, b, c = map(int, input().split())

max_num_of_a = c // a 
max_num_of_b = c // b

max_value = 0
for a_multiply in range(max_num_of_a + 1):
    for b_multiply in range(max_num_of_b + 1):
        if (cur_value:= a * a_multiply + b * b_multiply) <= c:
            max_value = max(max_value, cur_value)

print(max_value)