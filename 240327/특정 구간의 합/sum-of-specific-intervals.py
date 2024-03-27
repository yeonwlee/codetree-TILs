length_of_arr, num_of_number_pairs = map(int, input().split())
number_arr = list(map(int, input().split()))
pairs = [tuple(map(int, input().split())) for _ in range(num_of_number_pairs)]

for number_pair in pairs:
    start_index, end_index = number_pair[0] - 1, number_pair[1] - 1
    print(sum(number for number in number_arr[start_index: end_index + 1]))