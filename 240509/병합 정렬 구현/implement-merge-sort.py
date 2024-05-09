def merge_sort(arr:list[int]) -> None:
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    # 좌분할
    left = merge_sort(arr[0:mid])
    # 우분할
    right = merge_sort(arr[mid:])
    #정복
    return merge(left, right)

#병합
def merge(left_arr:list[int], right_arr:list[int]) -> None:
    left_index = right_index = 0
    
    merged_arr = []
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merged_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merged_arr.append(right_arr[right_index])
            right_index += 1
    
    # 왼쪽 리스트가 남아 있으면
    while left_index < len(left_arr):
        merged_arr.append(left_arr[left_index])
        left_index += 1
    
    # 오른쪽 리스트가 남아 있으면
    while right_index < len(right_arr):
        merged_arr.append(right_arr[right_index])
        right_index += 1

    return merged_arr


num_of_numbers = int(input())
numbers = list(map(int, input().split()))

merged_arr = merge_sort(numbers)

print(' '.join(map(str, merged_arr)))