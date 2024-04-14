a_arr_size, b_arr_size = map(int, input().split())

combined_arr = list(map(int, input().split())) + list(map(int, input().split()))
combined_arr.sort()
for num in combined_arr:
    print(num, end=" ")