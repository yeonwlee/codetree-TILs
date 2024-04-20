multiply_value, mod_value = map(int, input().split())


# cur_value = multiply_value
# results = []

# while (cur_value:=cur_value * multiply_value % mod_value) not in results:
#     results.append(cur_value)
   
# print(len(results[results.index(cur_value):]))

cur_value = multiply_value
set_for_checking_cycle = set()
results = []

while (cur_value:=cur_value * multiply_value % mod_value) not in set_for_checking_cycle:
    results.append(cur_value)
    set_for_checking_cycle.add(cur_value)
   
print(len(results[results.index(cur_value):]))