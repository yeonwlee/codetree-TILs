from itertools import combinations
from functools import reduce

'''
홀수가 짝수보다 우선순위가 높다.
같은 홀수끼리는 수 자체가 더 큰 경우가 우선순위가 높다.
같은 짝수끼리도 수 자체가 더 큰 경우가 우선순위가 높다.
'''
numbers = list(map(int, input().split()))

odd_semi_answers = []
even_semi_answers = []
for num_of_multi in range(1, len(numbers) + 1):
    for combi in combinations(numbers, num_of_multi):
        if (semi_answer:=reduce(lambda x, y: x * y, combi)) % 2 == 1:
            odd_semi_answers.append(semi_answer)
        else:
            even_semi_answers.append(semi_answer)
    
odd_semi_answers.sort(reverse=True)
even_semi_answers.sort(reverse=True)

if odd_semi_answers:
    print(odd_semi_answers[0])
else:
    print(even_semi_answers[0])