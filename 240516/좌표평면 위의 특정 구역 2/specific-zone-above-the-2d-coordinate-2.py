num_of_points = int(input())

points = [
    tuple(map(int, input().split()))
    for _ in range(num_of_points)
]

min_area = float('inf')

for index, _ in enumerate(points):
    cur_min_x, cur_max_x = 40000, 0
    cur_min_y, cur_max_y = 40000, 0
    for target_index, target_point in enumerate(points):
        if index == target_index:
            continue
        cur_x, cur_y = target_point
        cur_min_x, cur_min_y = min(cur_x, cur_min_x), min(cur_y, cur_min_y)
        cur_max_x, cur_max_y = max(cur_x, cur_max_x), max(cur_y, cur_max_y)
    cur_area = abs(cur_max_x - cur_min_x) * abs(cur_max_y - cur_min_y)
    min_area = min(min_area, cur_area)


print(min_area)