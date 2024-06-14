import sys

input = sys.stdin.readline

number = int(input().rstrip())
for _ in range(number):
    print(chr(int(input().rstrip())))