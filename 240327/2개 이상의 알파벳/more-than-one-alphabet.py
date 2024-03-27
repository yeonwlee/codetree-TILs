#문제 잘못 이해함. '서로 다른 알파벳의 수'임. '같은 알파벳의 수'가 아니라

# def check_it_has_different_chars(string: str) -> bool: #str도 이터러블 객체이기 때문에 바로 set으로 변환 가능
#     return len(set(string)) >= 2

def check_it_has_different_chars(string: str) -> bool: 
    unique_chars = set()
    for char in string:
        unique_chars.add(char)
        if len(unique_chars) >= 2:
            return True
    return False


string = input()
print("Yes" if check_it_has_different_chars(string) else "No")