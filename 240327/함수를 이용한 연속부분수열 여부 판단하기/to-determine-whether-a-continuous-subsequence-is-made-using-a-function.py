def is_part_of_source(source: list[int], check_data: list[int]) -> bool:
    if len(source) < len(check_data):
        return False
    for index, _ in enumerate(source):
        if len(source) > len(check_data) + index:
            if source[index:len(check_data) + index] == check_data:
                return True
    return False


n1, n2 = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print("Yes" if is_part_of_source(arr1, arr2) else "No")