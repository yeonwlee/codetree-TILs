num_of_datas = int(input())
datas = [
    input().split()
    for _ in range(num_of_datas)
]

datas.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True) # 국, 영, 수 우선순위. 
#문자열은 - 연산자가 사용이 안되어 내림차순 정렬을 위해 reverse 옵션 추가

for data in datas:
    print(*data)