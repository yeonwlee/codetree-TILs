num_of_command = int(input())
point_info = [0 for _ in range(101)]

commands = [
    tuple(input().split())
    for _ in range(num_of_command)
]

cur_position = 0

for x, direction in commands:
    x = int(x)
    if direction == "L":
        for index in range(cur_position - x, cur_position):
            point_info[index] += 1
        cur_position -= x
    else: 
        for index in range(cur_position, cur_position + x):
            point_info[index] += 1
        cur_position += x

print(sum(1 for index in range(len(point_info) - 1) if point_info[index] >= 2))