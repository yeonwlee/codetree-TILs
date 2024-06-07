num_of_stone, max_jump_distance = map(int, input().split())

stones = list(map(int, input().split()))

cur_stone_value = stones[0]
for num in range(cur_stone_value, 101): # 조건 범위, 최대 값 가정
    cur_pos: int = 0
    # 해당 값을 최대값으로 했을 때, 밟을 수 있는 돌 밟고 건너가기
    for index in range(cur_pos + 1, num_of_stone):
        if abs(cur_pos - index) <= max_jump_distance:
            if stones[index] <= num:
                cur_pos = index
        else:
            break
    if cur_pos == num_of_stone - 1: # 마지막 돌에 위치함
        print(num)
        break