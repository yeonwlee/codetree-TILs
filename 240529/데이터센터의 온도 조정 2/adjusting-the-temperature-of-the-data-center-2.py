# 온도를 적절히 설정하여 데이터센터안의 최고 작업량을 출력하는 프로그램을 작성해보세요.
num_of_machine, workload1, workload2, workload3 = map(int, input().split())
temperature_range = [
    tuple(map(int, input().split()))
    for _ in range(num_of_machine)
]

lower, higher = float('inf'), float('-inf')
# 기계 선호 최저온도, 최고온도 -- 범위 정하기
for low, high in temperature_range:
    lower = min(lower, low)
    higher = max(higher, high)

max_workload = float('-inf')
for temperature in range(lower - 1, higher + 2):
    sum_of_workload = 0
    for low, high in temperature_range:
        if temperature < low:
            sum_of_workload += workload1
        elif temperature <= high:
            sum_of_workload += workload2
        else: 
            sum_of_workload += workload3
    max_workload = max(sum_of_workload, max_workload)

print(max_workload)