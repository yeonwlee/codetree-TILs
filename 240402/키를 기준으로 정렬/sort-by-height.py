num_of_datas = int(input())
datas = [
    input().split()
    for _ in range(num_of_datas)
]

datas.sort(key=lambda x: x[1]) # 키를 기준으로 정렬

for data in datas:
    print(*data)