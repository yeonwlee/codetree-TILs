#1초에 한 칸 씩 이동
def find_return_to_zero_time(num_of_moving: int) -> int:
    cur_x, cur_y = 0, 0
    time = 0
    for _ in range(num_of_moving):
        direction, distance = input().split()
        distance = int(distance)
        for _ in range(distance):
            cur_x, cur_y = cur_x + dxs[direction], cur_y + dys[direction]
            time += 1
            if cur_x == 0 and cur_y == 0:
                return time
    return -1
    

num_of_moving = int(input())

#서남북동
dxs, dys = {"W":-1, "S":0, "N":0, "E":1}, {"W":0, "S":1, "N":-1, "E":0}

print(find_return_to_zero_time(num_of_moving))