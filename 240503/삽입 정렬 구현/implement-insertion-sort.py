class InsertionSort():
    def sort_asc(self, arr: list[int]) -> None:
        for index in range(1, len(arr)):
            compare_index = index - 1 # 현재 요소와 비교할 요소의 인덱스
            key = arr[index] # 현재 요소의 값
            while compare_index >= 0 and arr[compare_index] > key:
                arr[compare_index + 1] = arr[compare_index]
                compare_index -= 1
            arr[compare_index + 1] = key
    


num_of_elements = int(input())
numbers = list(map(int, input().split()))
insertion_sort = InsertionSort()
insertion_sort.sort_asc(numbers) # 매개변수로 넘긴 배열을 바로 변경

print(' '.join(map(str, numbers)))