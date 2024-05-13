def is_within_bound(row_index:int, col_index:int) -> bool:
    return 0 <= row_index < row_num and 0 <= col_index < col_num


def check_all_direction(row_index:int, col_index:int) -> int:
    count = 0
    cur_row, cur_col = row_index, col_index
    for row_moving, col_moving in directions:
        next_row, next_col = cur_row + row_moving, cur_col + col_moving
        next_row2, next_col2 = next_row + row_moving, next_col + col_moving
        if is_within_bound(next_row2, next_col2):
            if (grid[next_row][next_col] == 'E' and 
                grid[next_row2][next_col2] == 'E'):
                count += 1
    return count


row_num, col_num = map(int, input().split())

grid = [
    list(input())
    for _ in range(row_num)
]

# 왼쪽 위, 위, 오른쪽 위,
# 왼쪽, 오른쪽
# 왼쪽 아래, 아래, 오른쪽 아래
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
count = 0

for row_index in range(row_num):
    for col_index in range(col_num):
        if grid[row_index][col_index] == 'L':
            # 전방향으로 2칸씩 확인: E가 두개 나오는지. 타겟 문자열 LEE
            count += check_all_direction(row_index, col_index)

print(count)