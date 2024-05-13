width_of_grid = height_of_grid = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(width_of_grid)
]

max_num_of_coins = 0

for row_1 in range(height_of_grid):
    for col_1 in range(width_of_grid - 2):
        target1= sum(grid[row_1][col_1:col_1+3])
        for row_2 in range(row_1, height_of_grid):
            start_col = col_1 + 3 if row_1 == row_2 else 0
            if start_col + 3 <= width_of_grid:   
                for col_2 in range(start_col, width_of_grid - 2):
                    target2 = sum(grid[row_2][col_2:col_2+3])
                    max_num_of_coins = max(max_num_of_coins, target1 + target2)
            else:
                continue
   

print(max_num_of_coins)