OFFSET = 100

def color_rect_in_area(area: list, rect: tuple, color: str):
    x1, y1, x2, y2 = [one_of_coord + OFFSET for one_of_coord in rect]
    for row in range(x1, x2):
        for col in range(y1, y2):
            area[row][col] = color


num_of_rect = int(input())
rect_info = [
    tuple(map(int, input().split()))
    for _ in range(num_of_rect)
]
area = [
    ["-" for _ in range(200)] for _ in range(200)
]

for index, rect in enumerate(rect_info):
    color: str = "r"
    if index % 2 != 0:
        color = "b"
    color_rect_in_area(area, rect, color)

print(sum(1 for row in area for box in row if box == "b"))