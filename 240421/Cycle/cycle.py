multiply_value, mod_value = map(int, input().split())

results = {multiply_value}
cur_value = multiply_value
cycle = 0

while (cur_value:=cur_value * multiply_value % mod_value) not in results:
    cycle += 1
    results.add(cur_value)

print(cycle)