from collections import Counter

#흰,검,회색 타일 수 각각 구하기
def is_tile_already_dupl_colored(tile) -> bool:
    if tile["cur_color"] == "G":
        return True
    for count in tile.values():
        print(count)
    return all(True for count in tile.values() if count >= 2)


num_of_command = int(input())
color_of_tile = [{"W": 0, "B": 0, "cur_color": 2} for _ in range(100000)]
commands = [
    input().split()
    for _ in range(num_of_command)
]

cur_position = 100
for x, direction in commands:
    x = int(x)
    if direction == "L":
        for index in range(cur_position, cur_position - x, -1):
            if is_tile_already_dupl_colored(color_of_tile[index]):
                color_of_tile[index]["cur_color"] = "G"
            else:
                color_of_tile[index]["W"] += 1
                color_of_tile[index]["cur_color"] = "W"
            cur_position -= x
    else:
        for index in range(cur_position, cur_position + x):
            if is_tile_already_dupl_colored(color_of_tile[index]):
                color_of_tile[index]["cur_color"] = "G"
            else:
                color_of_tile[index]["B"] += 1
                color_of_tile[index]["cur_color"] = "B"
            cur_position += x


white_tile = 0
black_tile = 0
gray_tile = 0

for tile in color_of_tile:
    if tile["cur_color"] == "W":
        white_tile += 1
    elif tile["cur_color"] == "B":
        black_tile += 1
    elif tile["cur_color"] == "G":
        gray_tile += 1

print(white_tile, black_tile, gray_tile)