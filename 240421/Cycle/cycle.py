multiply_value, mod_value = map(int, input().split())


cur_value = multiply_value
results = []

while (cur_value:=cur_value * multiply_value % mod_value) not in results:
    results.append(cur_value)
   
print(len(results[results.index(cur_value):]))