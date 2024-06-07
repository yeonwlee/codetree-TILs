num_of_stone, max_jump_distance = map(int, input().split())

stones = list(map(int, input().split()))

cur_stone_value = stones[0]
for num in range(cur_stone_value, 101): # 조건 범위, 최대 값 가정
    cur_pos: int = 0
    while (distance_of_can_jump_stone:=next((jump_distance for jump_distance, value in enumerate(stones) if value <= num and cur_pos < jump_distance), None)):
        if abs(cur_pos - distance_of_can_jump_stone) <= max_jump_distance: # 범위 내로 뛸 수 있는 곳이 있음
            cur_pos += abs(cur_pos - distance_of_can_jump_stone)
        else: # 범위 내에 뛸 수 있는 곳이 없음
            break
    if cur_pos == num_of_stone - 1:
        print(num)
        break