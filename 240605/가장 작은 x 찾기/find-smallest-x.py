import sys
import math

input = sys.stdin.readline

repeat_num = int(input().rstrip())
suspect = set()
clues =[
    tuple(map(int, input().rstrip().split()))
    for _ in range(repeat_num)  
]

clue_range = clues[-1] # 가장 마지막 범위

# 2를 곱할 때 마다 ==> 확인 벙뮈를 짝수로 한정
start = clue_range[0] if clue_range[0] % 2 == 0 else clue_range[0] + 1 

for x in range(start, clue_range[1] + 1, 2): # 짝수만 확인
    check_num = x
    is_valid = True
    for count_num in range(repeat_num - 2, -1, -1): # 이전 범위들에 해당 값이 속하는 지확인
        check_num //= 2
        if not (clues[count_num][0] <= check_num <= clues[count_num][1]): # 속하지 않으면 
            is_valid = False
            break
    if is_valid:
        suspect.add(math.ceil(check_num / 2)) # 마지막 예상 값
        # 주의할 점. python의 round의 반올림은 bankers' rounding이라는 방식으로, 
        #  0.5인 경우 가장 가까운 짝수로 반올림함. 삽질 이유

print(min(suspect))