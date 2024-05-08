# 기수 정렬, 오름차순
def radix_sort(arr, position) -> None:
    while position >= 0:
        buckets = [[] for _ in range(10)]
        for num_str in arr:
            digit = num_str[position] if position < len(num_str) else '0'  # 자릿수가 부족할 경우 0으로 간주
            buckets[int(digit)].append(num_str)
        arr = [num for pos in buckets for num in pos] # 1차원화
        position -= 1
    return arr


num_of_numbers = int(input())
elements = list(input().split())

max_position = len(max(elements, key=len)) - 1

elements = radix_sort(elements, max_position)
print(' '.join(map(str, elements)))