num_of_rect = int(input())

rect_area = [
    [0 for _ in range(200)] for _ in range(200)
]
rect_info = [
    tuple(map(int, input().split()))
    for _ in range(num_of_rect)
]


for x1, y1, x2, y2 in rect_info:
    x1, y1, x2, y2 = x1 + 100, y1 + 100, x2 + 100, y2 + 100
    for row_index in range(x1, x2):
        for col_index in range(y1, y2):
            rect_area[row_index][col_index] += 1

print(sum(1 for rect in rect_area for cur_area in rect if cur_area >= 1))