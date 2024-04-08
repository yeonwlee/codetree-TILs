from collections import Counter

num_of_command = int(input())
commands = [
    tuple(input().split())
    for _ in range(num_of_command)
]

tile_info = [
    "G"
    for _ in range(2 * 1000 * 100) #양수로 맞추기 위함
]

cur_position = 1000 * 100

for x, direction in commands:
    x = int(x)
    if direction == "L":
        for index in range(cur_position, cur_position - x, -1):
            tile_info[index] = "W"
        cur_position = cur_position - x + 1
    else:
        for index in range(cur_position, cur_position + x):
            tile_info[index] = "B"
        cur_position = cur_position + x - 1


tile_color_counter = Counter(tile_info)
print(tile_color_counter["W"], tile_color_counter["B"])