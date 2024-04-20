multiply_value, mod_value = map(int, input().split())


cur_value = multiply_value
results = set()
cycle = 0

while (cur_value:=cur_value * multiply_value % mod_value) not in results:
    cycle += 1
    results.add(cur_value)

print(cycle)