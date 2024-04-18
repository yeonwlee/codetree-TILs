#상하좌우 중 특정 방향으로 1초에 한 칸씩 움직임
#격자 끝에 다다르면 방향을 반대로 바꾸는데, 1만큼의 시간이 소요됨(그 순간에는 제자리)

width_of_grid, time = map(int, input().split())
cur_row, cur_col, direction = input().split()
cur_row, cur_col = int(cur_row) - 1, int(cur_col) - 1 #인덱스를 맞춰주기 위함

#상/좌우/하
dxs, dys = [0, -1, 1, 0], [-1, 0, 0, 1]
direction_mapping_index = {"U": 0, "L": 1, "R": 2, "D": 3}
cur_direction_index = direction_mapping_index[direction]


def is_within_bound(x: int, y: int) -> bool:
    return (0 <= x < width_of_grid) and (0 <= y < width_of_grid)


for _ in range(time):
    next_row = cur_row + dys[cur_direction_index]
    next_col = cur_col + dxs[cur_direction_index]
    if is_within_bound(next_col, next_row):
        cur_row = next_row
        cur_col = next_col
    else:
        cur_direction_index = 3 - cur_direction_index


## 인덱스화 했기 때문에 다시 x행 y열로 변경해줘야함
cur_row, cur_col = cur_row + 1, cur_col + 1

print(cur_row, cur_col)