multiply_value, mod_value = map(int, input().split())


cur_value = multiply_value
results = set()
cycle = 0

# while (cur_value:=cur_value * multiply_value % mod_value) not in results:
#     results.add(cur_value)
#     cycle += 1

# print(cycle)


while True:
    cur_value = cur_value * multiply_value % mod_value
    if cur_value not in results:
        results.add(cur_value)
        cycle += 1
    else:
        break

print(cycle)