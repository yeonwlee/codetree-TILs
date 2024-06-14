def is_ascii_alpha(char:str) -> bool: # isalpha() 는 다른 언어의 문자도 true로 취급함
    ascii_value = ord(char)
    return (65 <= ascii_value <= 90) or (97 <= ascii_value <= 122)

source = input()

for char in source:
    if is_ascii_alpha(char):
        print(char.lower(), end='')