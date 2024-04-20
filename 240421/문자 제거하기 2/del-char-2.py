source_str, num_of_commands = input().split()
source_str = list(source_str)
num_of_commands = int(num_of_commands)

for _ in range(num_of_commands):
    del_position = int(input()) - 1
    if len(source_str) <= del_position:
        continue
    source_str.pop(del_position)
    print(''.join(source_str))