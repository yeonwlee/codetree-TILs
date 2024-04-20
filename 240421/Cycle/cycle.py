multiply_value, mod_value = map(int, input().split())


cur_value = multiply_value
results = set()

while (cur_value:=cur_value * multiply_value % mod_value) not in results:
    results.add(cur_value)
   
print(len(results))