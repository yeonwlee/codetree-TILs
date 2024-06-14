from itertools import combinations

'''
홀수가 짝수보다 우선순위가 높다.
같은 홀수끼리는 수 자체가 더 큰 경우가 우선순위가 높다.
같은 짝수끼리도 수 자체가 더 큰 경우가 우선순위가 높다.
'''
numbers = map(int, input().split())

print(list(combinations(numbers, 2)))