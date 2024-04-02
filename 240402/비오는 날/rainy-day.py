num_of_source = int(input())
source = [
    input().split()
    for _ in range(num_of_source)
]

source.sort(key=lambda x: x[0])
for data in source:
    date, day, weather = data
    if weather == "Rain":
        print(date, day, weather)
        break