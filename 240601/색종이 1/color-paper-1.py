num_of_papers = int(input())

# 가로, 세로의 크기가 각각 10인 정사각형 모양의 파란색 색종이
# 왼쪽 아래의 x 좌표와 y 좌표
papers_pos_info = [
    tuple(map(int, input().split()))
    for _ in range(num_of_papers)
]

grid = [
    [0] * 100
    for _ in range(100)
]

for under_left_x, under_left_y in papers_pos_info:
    for x in range(under_left_x, under_left_x + 10):
        for y in range(under_left_y, under_left_y + 10):
            grid[x][y] = 1

print(sum(1 for row in grid for col in row if col == 1))