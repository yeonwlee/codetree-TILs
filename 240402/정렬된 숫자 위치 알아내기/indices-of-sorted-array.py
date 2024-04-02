num_of_data = int(input())
data = [
    (value, index) for index, value in enumerate(map(int, input().split()))
]

sorted_data = sorted(data, key=lambda x: (x[0], x[1]))

for one in data:
    print(sorted_data.index(one) + 1, end= " ")