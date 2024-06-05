import sys

input = sys.stdin.readline

score = int(input().rstrip())
pass_score = 80

if score >= pass_score:
    print('pass')
else:
    print(f'{pass_score - score} more score')