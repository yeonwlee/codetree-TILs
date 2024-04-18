def get_next_direction(cur_index: int) -> int:
    return (cur_direction_index + 1) % 4


def is_within_bound(cur_x: int, cur_y: int) -> bool:
    return (0 <= cur_x < col) and (0 <= cur_y < row) 

row, col = map(int, input().split())
visited_mark = [
    [0 for _ in range(col)]
    for _ in range(row)
]

#오른쪽, 아래, 왼쪽, 위쪽
#을 오른쪽으로 꺾는다는 개념으로 가져감
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
cur_x, cur_y = 0, 0
cur_direction_index = 0

for num in range(row * col):
    visited_mark[cur_y][cur_x] = num + 1
    next_x, next_y = cur_x + dxs[cur_direction_index], cur_y + dys[cur_direction_index]
    if (not is_within_bound(next_x, next_y)
        or visited_mark[next_y][next_x] != 0): # 범위를 넘었거나, 방문을 한 경우
        cur_direction_index = get_next_direction(cur_direction_index)
        next_x, next_y = cur_x + dxs[cur_direction_index], cur_y + dys[cur_direction_index]  
    cur_x, cur_y = next_x, next_y
    


for row in visited_mark:
    print(' '.join(map(str, row)))