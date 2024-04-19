# ‘편안한 상태’란 방금 막 칠해진 칸을 기점으로 위 아래 양옆으로 인접한 4개의 칸 중 
# 격자를 벗어나지 않는 칸에 색칠되어 있는 칸이 정확히 3개인 경우를 뜻합니다.


def is_within_bound(x:int, y:int) -> bool:
    return (0 <= x < width_of_grid) and (0 <= y < width_of_grid)


def is_comport_status(row: int, col: int) -> bool:
    coloring_count = 0
    for dx, dy in zip(dxs, dys):
        next_x, next_y = col + dx, row + dy  
        if is_within_bound(next_x, next_y) and color_status_of_grid[next_y][next_x] == 1:
            coloring_count += 1
    return coloring_count == 3


width_of_grid, num_of_coloring = map(int, input().split())

#색칠 정보
color_status_of_grid = [
    [0 for _ in range(width_of_grid)]
    for _ in range(width_of_grid)
]

#북동남서
dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]

for _ in range(num_of_coloring):
    row, col = map(int, input().split())
    row, col = row - 1, col - 1 #인덱스화
    color_status_of_grid[row][col] = 1
    print(1 if is_comport_status(row, col) else 0)