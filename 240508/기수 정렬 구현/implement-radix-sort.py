# 기수 정렬, 오름차순
def radix_sort(arr, position) -> None:
    buckets = [[] for _ in range(10)]
    while position >= 0:
        for num_str in arr:
            if len(num_str) <= position:
                buckets[int(num_str[position])].append(num_str[position])
        arr = [num for pos in buckets for num in pos] # 1차원화
        position -= 1
    return arr


num_of_numbers = int(input())
elements = list(input().split())

max_position = len(max(elements, key=len)) - 1

elements = radix_sort(elements, max_position)
print(' '.join(map(str, elements)))