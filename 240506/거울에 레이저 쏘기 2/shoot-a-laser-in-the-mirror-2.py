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
    positions.append((0, i, "U"))
# 오른쪽 면
for i in range(width_of_grid):
    positions.append((i, width_of_grid - 1, "R"))
# 아랫쪽 면
for i in range(width_of_grid):
    positions.append((width_of_grid - 1, width_of_grid - 1 - i, "D"))
# 왼쪽 면
for i in range(width_of_grid):
    positions.append((width_of_grid - 1 - i, 0, "L"))

########
# /
direction_1 = {
    "U": (0, -1, "R"), 
    "D": (0, 1, "L"), 
    "L": (-1, 0, "D"), 
    "R": (1, 0, "U")
}

# \
direction_2 = {
    "U": (0, 1, "L"), 
    "D": (0, -1, "R"), 
    "L": (1, 0, "U"), 
    "R": (-1, 0, "D")
}


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