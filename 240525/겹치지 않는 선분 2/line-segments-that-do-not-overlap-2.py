# 겹치지 않는 경우:
# (선분2의 시작점 < 선분1의 시작점 and 선분2의 끝점 < 선분1의 끝점) or
# (선분1의 시작점 < 선분2의 시작점 and 선분1의 끝점 < 선분2의 끝점)

num_of_lines = int(input())

lines = [
    tuple(map(int, input().split()))
    for _ in range(num_of_lines)
]

checked_lines = [0] * num_of_lines
num_of_lines_not_crossing = 0

for line_for_checking_index in range(num_of_lines):
    if not checked_lines[line_for_checking_index]: # 이미 다른 선분과 겹쳤던 경우 생략
        for other_line_index in range(num_of_lines):
            if line_for_checking_index == other_line_index: # 자기 자신은 생략
                continue
            start1, end1 = lines[line_for_checking_index]
            start2, end2 = lines[other_line_index]
            if not ((start2 < start1 and end2 < end1) or (start1 < start2 and end1 < end2)): # 평행하지 않으면(=겹치면)
                checked_lines[line_for_checking_index], checked_lines[other_line_index] = 1, 1
                break
        else:
            num_of_lines_not_crossing += 1

print(num_of_lines_not_crossing)