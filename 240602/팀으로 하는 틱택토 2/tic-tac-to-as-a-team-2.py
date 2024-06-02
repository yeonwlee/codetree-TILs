import sys

input = sys.stdin.readline

tictactoe = [
    list(input().strip())
    for _ in range(3)
]

# 가로, 세로, 대각선 등 승리하는 케이스를 모두 모으기
# 각 케이스 중 두 개의 수로 만들어진 경우 세기
victory_cases = set()

# 가로
for row in tictactoe:
    victory_cases.add(tuple(row))

# 세로    
for col in range(3):
    victory_cases.add(tuple([row[col] for row in tictactoe]))

# 대각선
victory_cases.add((tictactoe[0][0], tictactoe[1][1], tictactoe[2][2]))
victory_cases.add((tictactoe[0][2], tictactoe[1][1], tictactoe[2][0]))

print(sum(1 for cur_case in victory_cases if len(set(cur_case)) == 2))