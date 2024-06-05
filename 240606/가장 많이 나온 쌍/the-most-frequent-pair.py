import sys

input = sys.stdin.readline

# 입력 외에 추가적인 이차원 배열을 사용하지 않고 문제를 해결해보세요.
max_range, num_of_pair = map(int, input().rstrip().split())
pairs = [
    tuple(map(int, input().rstrip().split()))
    for _ in range(num_of_pair)
]

max_pair_count = 0
base_index = 0
while base_index < len(pairs):
    a, b = pairs[base_index]
    count = 1 # 현재 쌍을 세고 시작
    compare_index = base_index + 1 # 그 뒤의 인덱스부터 확인
    while compare_index < len(pairs):
        c, d = pairs[compare_index]
        if (a == c and b == d) or (a == d and b == c): # 쌍이 순서 관계 없이 같으면
            count += 1 # 수를 세고
            del pairs[compare_index] # 해당 쌍 삭제
            continue
        compare_index += 1
    max_pair_count = max(max_pair_count, count)
    base_index += 1

print(max_pair_count)