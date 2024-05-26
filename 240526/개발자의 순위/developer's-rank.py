num_of_compitition, num_of_dev = map(int, input().split())

result_of_compitition = [
    tuple(map(int, input().split()))
    for _ in range(num_of_compitition)
]

# 자기 외 다른 개발자들을 모두 하위 순위 개발자로 초기화
result = {dev:{dev_num for dev_num in range(1, num_of_dev + 1) if dev != dev_num} for dev in range(1, num_of_dev + 1)}

for compitition in result_of_compitition:
    for target_index in range(len(compitition)):
        # 하위 순위의 개발자들
        lower_devs = {compitition[compare_index] for compare_index in range(target_index + 1, len(compitition))}
        # 교집합
        result[compitition[target_index]] = result[compitition[target_index]] & lower_devs

case_count = sum(len(lowers) for lowers in result.values())
print(case_count)