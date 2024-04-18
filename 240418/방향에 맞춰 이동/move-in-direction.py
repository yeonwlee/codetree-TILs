num_of_moving = int(input())

#서, 남, 북, 동
dx, dy = {"W": -1, "S": 0, "N": 0, "E": 1}, {"W": 0, "S": -1, "N": 1, "E": 0}
cur_x, cur_y = 0, 0

for _ in range(num_of_moving):
    direction, distance = input().split()
    distance = int(distance)
    cur_x = cur_x + (dx[direction] * distance)
    cur_y = cur_y + (dy[direction] * distance)

print(cur_x, cur_y)