nth, num_of_command = map(int, input().split())
piled_block_info = [0 for _ in range(nth)]
commands = [
    tuple(map(int, input().split()))
    for _ in range(num_of_command)
]

for command in commands:
    for index in range(command[0], command[1] + 1):
        piled_block_info[index] += 1

print(max(piled_block_info))