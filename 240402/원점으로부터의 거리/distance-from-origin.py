num_of_points = int(input())

points = []

for index in range(num_of_points):
    points.append(list(map(int, input().split())))
    points[index].append(index + 1) # 번호도 넣어주기

points.sort(key=lambda x: (abs(x[0]) + abs(x[1]), x[2]))

for point in points:
    _, _, id_number = point
    print(id_number)