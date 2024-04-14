import heapq

a_arr_size, b_arr_size = map(int, input().split())

sorted_a_arr = sorted(list(map(int, input().split())))
sorted_b_arr = sorted(list(map(int, input().split())))

combined_arr = list(heapq.merge(sorted_a_arr, sorted_b_arr))
print(" ".join(map(str, combined_arr)))