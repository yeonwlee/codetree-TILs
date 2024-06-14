import sys


def is_ascii_alpha(c):
    ascii_value = ord(c)
    return (65 <= ascii_value <= 90) or (97 <= ascii_value <= 122)


input = sys.stdin.readline

num_of_char = int(input().rstrip())
for _ in range(num_of_char):
    char = input().rstrip()
    if is_ascii_alpha(char):
        print(char)
    elif char.isdigit():
        print(ord(char))