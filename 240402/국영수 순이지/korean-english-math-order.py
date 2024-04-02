num_of_datas = int(input())
datas = [
    input().split()
    for _ in range(num_of_datas)
]

datas.sort(key=lambda x: (-int(x[1]), -int(x[2]), -int(x[3]))) # 국, 영, 수 우선순위. 

for data in datas:
    print(*data)