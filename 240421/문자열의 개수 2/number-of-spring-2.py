num_of_strs = 0
even_position_strs = []

while (cur_str:= input()) != "0":
    num_of_strs += 1
    if num_of_strs % 2 == 0:
        even_position_strs.append(cur_str)

print(num_of_strs)
for cur_str in even_position_strs:
    print(cur_str)