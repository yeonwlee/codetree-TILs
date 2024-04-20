str_a, str_b = input().split()
result = 0
a_int_values = []
b_int_values = []

for char_a in str_a:
    if char_a.isdecimal():
        a_int_values.append(char_a)

for char_b in str_b:
    if char_b.isdecimal():
        b_int_values.append(char_b)


print(int(''.join(a_int_values)) + int(''.join(b_int_values)))