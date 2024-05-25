# itertools.permutations를 사용하지 않음
try_num = int(input())
try_info = [
    tuple(map(int, input().split()))
    for _ in range(try_num)
]

possible_combinations = set()
for first in range(1, 10):
    for second in range(1, 10):
        for third in range(1, 10):
                if first != second and second != third and first != third:
                    possible_combinations.add((first, second, third))


for trying in try_info:
    suggest_answer, count_num_at_the_position, count_num_in_set = trying 
    suggest_answer = list(map(int, str(suggest_answer)))
    possible_combinations = {combi for combi in possible_combinations
                            if count_num_at_the_position == sum(1 for index in range(3) if combi[index] == suggest_answer[index]) 
                            and count_num_in_set == sum(1 for index in range(3) if combi[index] != suggest_answer[index] and suggest_answer[index] in combi)}

print(len(possible_combinations))