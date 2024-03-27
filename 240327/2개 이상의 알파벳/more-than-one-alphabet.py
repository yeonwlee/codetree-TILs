#문제 잘못 이해함. '서로 다른 알파벳의 수'임. '같은 알파벳의 수'가 아니라

def check_it_has_different_chars(string: list[str]) -> bool:
    return len(set(string)) >= 2

string_list = list(input())
print("Yes" if check_it_has_different_chars(string_list) else "No")