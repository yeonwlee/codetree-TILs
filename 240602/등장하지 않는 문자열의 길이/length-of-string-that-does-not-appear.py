import sys

input = sys.stdin.readline

source_len = int(input().rstrip())
source = input().rstrip()

# 연속 부분 문자열로 두 번 이상 나타나지 않는 문자열의 최소 길이를 출력하는 프로그램을 작성하세요.
for length in range(1, source_len // 2 + 2): # 두 번 이상 나타날 수 있는 문자열 길이까지 확인하면 됨
    is_in_source = False
    for check_index in range(source_len):
        if check_index + length > source_len: # 모두 찾을 때 까지 해당 문자열을 2개 이상 못 찾았으면
            break
        elif source.count(str(source[check_index:check_index + length])) >= 2: # 소스 문자열에서 해당 길이만큼 자른(부분문자열)의 갯수가 2개 이상이면
            is_in_source = True
            break
    if not is_in_source:
        print(length) # 문자열의 길이 출력
        break