def are_they_can_be_with_same_line(one_cur_col: int, two_cur_col: int) -> bool:
    return one_cur_col + 3 + two_cur_col + 3 <= width_of_grid


width_of_grid = height_of_grid = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(width_of_grid)
]

window1 = sum(grid[0][:3])
can_be_same_line = are_they_can_be_with_same_line(0, 3)
if can_be_same_line:
    window2 = sum(grid[0][3:6])
    window2_row = 0
    window2_col = 4
else:
    window2 = sum(grid[1][:3])
    window2_row = 1
    window2_col = 1

max_num_of_coins = window1 + window2

window1_row = 0
window1_col = 1
while window1_row < height_of_grid:
    for col_1 in range(window1_col, width_of_grid - 2):
        window1 = window1 - grid[window1_row][col_1 - 1] + grid[window1_row][col_1]
        while window2_row < height_of_grid:
            for col_2 in range(window2_col, width_of_grid - 2):
                window2 = window2 - grid[window2_row][col_2 - 1] + grid[window2_row][col_2]
                max_num_of_coins = max(max_num_of_coins, window1 + window2)
            window2_row += 1
            window2_col = 0
        if can_be_same_line:
            window2_row = window1_row
        else:
            window2_row = window1_row + 1
    window1_row += 1

print(max_num_of_coins)