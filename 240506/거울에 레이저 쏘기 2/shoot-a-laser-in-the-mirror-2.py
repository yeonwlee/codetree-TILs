width_of_grid = int(input())
mirror_grid = [
    list(map(str, input()))
    for _ in range(width_of_grid) 
]


cur_position = int(input())
positions =[]

#########
#시작 위치 및 방향 세팅    
# 윗면
for i in range(width_of_grid):
    positions.append((0, i, "D"))
# 오른쪽 면
for i in range(width_of_grid):
    positions.append((i, width_of_grid - 1, "L"))
# 아랫쪽 면
for i in range(width_of_grid):
    positions.append((width_of_grid - 1, width_of_grid - 1 - i, "U"))
# 왼쪽 면
for i in range(width_of_grid):
    positions.append((width_of_grid - 1 - i, 0, "R"))

########
# /
direction_1 = {"U": (-1, 1, "R"), "D": (1, -1, "L"), "L":(-1, 1, "U"),"R":(1, -1, "D")}

# \
direction_2 = {"U": (-1, -1, "L"), "D": (1, 1, "R"), "L":(1, 1, "D"),"R":(-1, -1, "U")}


cur_row, cur_col, direction = positions[cur_position - 1]
count = 0

while 0 <= cur_row < width_of_grid and 0 <= cur_col < width_of_grid:
    if mirror_grid[cur_row][cur_col] == "/":
        cur_row += direction_1[direction][0]
        cur_col += direction_1[direction][1]
        direction = direction_1[direction][2]
    else:
        cur_row += direction_2[direction][0]
        cur_col += direction_2[direction][1]
        direction = direction_2[direction][2]
    count += 1

print(count)