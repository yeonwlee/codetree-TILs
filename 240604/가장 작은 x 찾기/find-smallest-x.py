import sys

input = sys.stdin.readline

repeat_num = int(input().rstrip())
suspect = set()

for count in range(1, repeat_num + 1):
    clue_range = tuple(map(int, input().rstrip().split()))    
    # 양의 정수 x로 시작해 값에 2를 곱하는 것을 반복 한다 == 짝수
    start = clue_range[0] if clue_range[0] % 2 == 0 else clue_range[0] + 1
    for x in range(start, clue_range[1] + 1, 2):
        cur_suspect = set()
        check_num = x
        for _ in range(count):
            check_num //= 2
        cur_suspect.add(check_num)
        if not suspect:
            suspect = cur_suspect.copy() # 전체 의심 수가 비어있으면 현재의 수 값들을
        else:  # 아니면 기존 의심되었던 수와 현재 의심되는 수의 교집합을 저장
            suspect &= cur_suspect

print(min(suspect))