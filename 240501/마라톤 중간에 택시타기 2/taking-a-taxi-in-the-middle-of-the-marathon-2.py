# Manhattan Distance로 거리 구함
def get_distance(check1:tuple[int], check2:tuple[int]) -> int:
    return abs(check1[0]-check2[0]) + abs(check1[1]-check2[1]) 

num_of_checkpoints = int(input())
checkpoints = [
    tuple(map(int, input().split()))
    for _ in range(num_of_checkpoints)
]

#각 체크포인트를 건너뛸 때 발생하는 절약된 거리를 계산하되, 이 절약된 거리가 최대인 체크포인트를 찾음
max_saving_distance = float('-inf')
skip_target_checkpoint = None
for index in range(1, len(checkpoints) - 1): #첫번째와 마지막 체크포인트는 건너뛰지 않음
    cur_distance = (get_distance(checkpoints[index - 1], checkpoints[index]) +
                        get_distance(checkpoints[index], checkpoints[index + 1]))
    skipped_cur_checkpoint_distance = get_distance(checkpoints[index - 1], checkpoints[index + 1])
    cur_saving_distance = cur_distance - skipped_cur_checkpoint_distance
    if max_saving_distance < cur_saving_distance:
        max_saving_distance = cur_saving_distance
        skip_target_checkpoint = index

del checkpoints[skip_target_checkpoint]
    

total_distance = sum(map(lambda pair: get_distance(pair[0], pair[1]), zip(checkpoints, checkpoints[1:])))
print(total_distance)