num_of_stone, max_jump_distance = map(int, input().split())

stones = list(map(int, input().split()))

cur_stone_value = stones[0]
for num in range(cur_stone_value, 101): # 조건 범위, 최대 값 가정
    cur_pos: int = 0
    # 해당 값을 최대값으로 했을 때, 밟을 수 있는 돌중 cur_pos 이후의 돌을 꺼냄.
    while (distance_of_can_jump_stone:=next((jump_distance for jump_distance, value in enumerate(stones) if value <= num and cur_pos < jump_distance), None)):
        if abs(cur_pos - distance_of_can_jump_stone) <= max_jump_distance: # 뛸 수 있음
            cur_pos += abs(cur_pos - distance_of_can_jump_stone)
        else: # 뛸 수 없음
            break
    if cur_pos == num_of_stone - 1: # 마지막 돌에 위치함
        print(num)
        break