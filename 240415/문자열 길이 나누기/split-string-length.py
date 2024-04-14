num_of_str = int(input())
joined_str = ""

for _ in range(num_of_str):
    joined_str += input()

strs = list(joined_str)
print(''.join(strs[:len(strs)//2]))
print(''.join(strs[len(strs)//2:]))