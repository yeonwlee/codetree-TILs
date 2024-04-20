num_of_strs, specific_str = input().split()
num_of_strs = int(num_of_strs)

for _ in range(num_of_strs):
    cur_str = input()
    if cur_str.find(specific_str) >= 0:
        print(cur_str)