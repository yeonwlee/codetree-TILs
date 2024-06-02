import sys

input = sys.stdin.readline

source_len = int(input().rstrip())
source = input().rstrip()

# 연속 부분 문자열로 두 번 이상 나타나지 않는 문자열의 최소 길이를 출력하는 프로그램을 작성하세요.
for length in range(1, source_len + 1):
    seen = set()
    repeated = False
    for check_index in range(source_len - length + 1):
        substring = source[check_index: check_index + length]
        if substring in seen:
            repeated = True
            break
        seen.add(substring)
    if not repeated:
        print(length)
        break