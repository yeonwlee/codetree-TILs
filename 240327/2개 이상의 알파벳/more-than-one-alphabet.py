def check_duplication(string: list[str]) -> bool:
    return len(string) > len(set(string))

string_list = list(input())
print("Yes" if check_duplication(string_list) else "No")