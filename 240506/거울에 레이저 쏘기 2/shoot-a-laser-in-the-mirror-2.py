width_of_grid = int(input())
mirror_grid = [
    list(map(str, input()))
    for _ in range(width_of_grid) 
]


cur_position = int(input())
positions =[]

#########
#시작 위치 및 방향 세팅    
for setting_index in range(width_of_grid * 4 // 2):
    if setting_index < width_of_grid: # 윗면
        positions.append((0, setting_index, "D"))
    elif setting_index < width_of_grid * 2: # 오른쪽 면
        positions.append((setting_index - width_of_grid, width_of_grid -1, "L"))

right_side = positions[width_of_grid * 2 - 1:width_of_grid - 1:-1]
up_side = positions[width_of_grid- 1::-1]

# 아랫쪽 면
for cur_pos_at_side in right_side:
    positions.append((cur_pos_at_side[1], cur_pos_at_side[0], "U"))

# 왼쪽 면
for cur_pos_at_side in up_side:
    positions.append((cur_pos_at_side[1], cur_pos_at_side[0], "R"))

########
# /
direction_1 = {"U": (0, 1, "R"), "D": (0, -1, "L"), "L":(-1, 0, "U"),"R":(1, 0, "D")}

# \
direction_2 = {"U": (-1, -1, "L"), "D": (0, 1, "R"), "L":(1, 0, "D"),"R":(-1, 0, "U")}

########

cur_position = positions[cur_position - 1]
count = 0
while cur_position[0] < width_of_grid and cur_position[1] < width_of_grid:
    cur_row, cur_col, direction = cur_position
    if mirror_grid[cur_row][cur_col] == "/":
        cur_position = (cur_row + direction_1[direction][0], cur_col + direction_1[direction][1], direction_1[direction][2]) 
        count += 1
    else:
        cur_position = (cur_row + direction_2[direction][0], cur_col + direction_2[direction][1], direction_2[direction][2]) 
        count += 1

print(count)