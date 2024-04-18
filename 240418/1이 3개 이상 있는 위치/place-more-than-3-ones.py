width_of_grid = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(width_of_grid)
]

#상하좌우
dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]

def is_in_grid(x: int, y: int) -> bool:
    return (0 <= x < width_of_grid) and (0 <= y < width_of_grid)


def count_num1_around(cur_x: int, cur_y: int) -> int:
    count: int = 0
    for dx, dy in zip(dxs, dys):
        if is_in_grid(cur_x + dx, cur_y + dy) and grid[cur_x + dx][cur_y + dy] == 1:
            count += 1
    return count


box_num_of_fitting_condition = 0

for row_point, row in enumerate(grid):
    for col_point, col in enumerate(row):
        count_num1 = count_num1_around(row_point, col_point)
        if count_num1 >= 3:
            box_num_of_fitting_condition += 1

print(box_num_of_fitting_condition)