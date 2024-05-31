num_of_strs = int(input())
strs = [
    input()
    for _ in range(num_of_strs)
]
# 아스키코드 순으로 가장 먼저 나오는 문자열을 출력하는 프로그램을 작성해보세요.
strs.sort()
print(strs[0])