num_of_compitition, num_of_dev = map(int, input().split())

result_of_compitition = [
    tuple(map(int, input().split()))
    for _ in range(num_of_compitition)
]

# 자기 외 다른 개발자들을 모두 하위 순위 개발자로 초기화
result = {dev:set(range(1, num_of_dev + 1)) - {dev} for dev in range(1, num_of_dev + 1)}

for compitition in result_of_compitition:
    for target_index, dev in enumerate(compitition):
        # 하위 순위의 개발자들
        lower_devs = set(compitition[target_index + 1:])
        # 교집합
        result[dev] &= lower_devs

case_count = sum(len(lowers) for lowers in result.values())
print(case_count)