num_of_data = int(input())
data = [
    (value, index) for index, value in enumerate(map(int, input().split()))
]

sorted_data = sorted(data, key=lambda x: (x[0], x[1]))

sorted_data_index_info = {number:index + 1 for index, number in enumerate(sorted_data)}

for one_of_data in data:
    print(sorted_data_index_info[one_of_data], end= " ")