from functools import reduce

# Manhattan Distance로 거리 구함
def get_distance(check1:tuple[int], check2:tuple[int]) -> int:
    return abs(check1[0]-check2[0]) + abs(check1[1]-check2[1]) 

num_of_checkpoints = int(input())
checkpoints = [
    tuple(map(int, input().split()))
    for _ in range(num_of_checkpoints)
]

max_distance = float('-inf') # 건너뛰는 거리가 가장 길어지면 최소 거리를 가게 됨
skip_target_checkpoint = None
for index in range(1, len(checkpoints) - 1):
    cur_skip_distance = (get_distance(checkpoints[index - 1], checkpoints[index]) +
                        get_distance(checkpoints[index], checkpoints[index + 1]))
    if max_distance < cur_skip_distance:
        max_distance = cur_skip_distance
        skip_target_checkpoint = index

del checkpoints[skip_target_checkpoint]
    

total_distance = sum(map(lambda pair: get_distance(pair[0], pair[1]), zip(checkpoints, checkpoints[1:])))
print(total_distance)