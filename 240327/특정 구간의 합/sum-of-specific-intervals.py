#슬라이싱
# length_of_arr, num_of_number_pairs = map(int, input().split())
# number_arr = list(map(int, input().split()))
# pairs = [tuple(map(int, input().split())) for _ in range(num_of_number_pairs)]

# for number_pair in pairs:
#     start_index, end_index = number_pair[0] - 1, number_pair[1] - 1
#     print(sum(number for number in number_arr[start_index: end_index + 1]))


#누적합 활용하기
length_of_arr, num_of_number_pairs = map(int, input().split())
number_arr = list(map(int, input().split()))
pairs = [tuple(map(int, input().split())) for _ in range(num_of_number_pairs)]
prefix_sum_arr = [0]

for index, number in enumerate(number_arr):
    prefix_sum_arr.append(prefix_sum_arr[-1] + number)

for number_pair in pairs:
    start_index, end_index = number_pair[0] - 1, number_pair[1] - 1
    print(prefix_sum_arr[end_index + 1] - prefix_sum_arr[start_index]) #구간합