from enum import Enum

class Color(Enum):
    NONE = 2
    WHITE = 3
    BLACK = 4
    GRAY = 5


def be_gray_tile(tile: dict) -> bool:
    if tile["cur_color"] == Color.GRAY.value:
        return True
    return all(True if count >= 2 else False for count in tile.values())


num_of_command = int(input())
tile_info = [{"W":0, "B":0, "cur_color": Color.NONE.value} for _ in range(200000)]

commands = [
    tuple(input().split())
    for _ in range(num_of_command)
]

cur_position = 100000

for x, direction in commands:
    x = int(x)
    if direction == "L": #왼쪽, 흰색
        for index in range(cur_position, cur_position - x, -1):
            tile_info[index]["W"] += 1
            if be_gray_tile(tile_info[index]):
                tile_info[index]["cur_color"] = Color.GRAY.value
            else:
                tile_info[index]["cur_color"] = Color.WHITE.value
        cur_position = cur_position - x + 1
    elif direction == "R": #오른쪽, 검은색
        for index in range(cur_position, cur_position + x):
            tile_info[index]["B"] += 1
            if be_gray_tile(tile_info[index]):
                tile_info[index]["cur_color"] = Color.GRAY.value
            else:
                tile_info[index]["cur_color"] = Color.BLACK.value
        cur_position = cur_position + x - 1


white_tile = 0
black_tile = 0
gray_tile = 0

for tile in tile_info:
    if tile["cur_color"] == Color.WHITE.value:
        white_tile += 1
    elif tile["cur_color"] == Color.BLACK.value:
        black_tile += 1
    elif tile["cur_color"] == Color.GRAY.value:
        gray_tile += 1

print(white_tile, black_tile, gray_tile)