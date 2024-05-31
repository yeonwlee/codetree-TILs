# 풀이1
# a, b, c = map(int, input().split())

# max_num_of_a = c // a 
# max_num_of_b = c // b

# max_value = 0
# for a_multiply in range(max_num_of_a + 1):
#     for b_multiply in range(max_num_of_b + 1):
#         if (cur_value:= a * a_multiply + b * b_multiply) <= c:
#             max_value = max(max_value, cur_value)

# print(max_value) 

# 풀이2: for 중첩 줄이기
a, b, c = map(int, input().split())

max_num_of_a = c // a 

max_value = 0
for a_multiply in range(max_num_of_a + 1):
    a_value = a * a_multiply
    b_multiply = (c - a_value) // b
    b_value = b * b_multiply
    max_value = max(max_value, a_value + b_value)

print(max_value)