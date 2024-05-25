from itertools import permutations


try_num = int(input())
try_info = [
    tuple(map(int, input().split()))
    for _ in range(try_num)
]

all_combination = set()
for first in range(1, 10):
    for second in range(1, 10):
        for third in range(1, 10):
            all_combination.add((first, second, third))

possible_combinations = set()

for trying in try_info:
    suggest_answer, count_num_at_the_position, count_num_in_set = trying 
    suggest_answer = list(map(int, str(suggest_answer)))
    if possible_combinations: # 가능한 조합이 이미 있으면
        answer = set()
        for combi in possible_combinations: 
            if count_num_at_the_position == sum(1 for index in range(3) if combi[index] == suggest_answer[index]):
                if count_num_in_set == sum(1 for index in range(3) if combi[index] != suggest_answer[index] and suggest_answer[index] in combi):
                    answer.add(combi)
        possible_combinations = answer
    else:
        for combi in all_combination: 
            if count_num_at_the_position == sum(1 for index in range(3) if combi[index] == suggest_answer[index]):
                if count_num_in_set == sum(1 for index in range(3) if combi[index] != suggest_answer[index] and suggest_answer[index] in combi):
                    possible_combinations.add(combi)

print(len(possible_combinations))