def extract_digit(string: str) -> int:
    return int(''.join([char for char in string if char.isdecimal()]))


str_a, str_b = input().split()

print(extract_digit(str_a) + extract_digit(str_b))