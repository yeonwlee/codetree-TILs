num_of_points = int(input())

points = [
    tuple(map(int, input().split()))
    for _ in range(num_of_points)
]

min_distance_pow = float('inf')

for first_index in range(num_of_points - 1):
    for second_index in range(first_index + 1, num_of_points):
        x_distance = abs(points[first_index][0] - points[second_index][0])
        y_distance = abs(points[first_index][1] - points[second_index][1])
        cur_distance_pow = x_distance ** 2 + y_distance ** 2
        if cur_distance_pow < min_distance_pow:
            min_distance_pow = cur_distance_pow

print(min_distance_pow)