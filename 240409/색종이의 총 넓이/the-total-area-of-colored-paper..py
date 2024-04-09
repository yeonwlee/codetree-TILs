#겹치는 영역은 한번만 넓이 계산

paper_width = 8
num_of_paper = int(input())
paper_left_end_position_info = [
    tuple(map(int, input().split()))
    for _ in range(num_of_paper)
]

offset= 100
#좌표평면 (-100,-100)~(100, 100)
area = [
    [0 for _ in range(200)] for _ in range(200)
]

for x, y in paper_left_end_position_info:
    x, y = x + offset, y + offset #위치를 양수화하기 위함
    for row in range(x, x + paper_width):
        for col in range(y, y + paper_width):
            area[row][col] += 1

print(sum(1 for row in area for col in row if col >= 1))