from itertools import permutations

max_num: int = int(input())
sum_arr = list(map(int, input().split()))

# 모든 조합 만들기
for cur_combi in sorted(permutations(range(1, max_num + 1))):
    if all(cur_sum == cur_combi[index] + cur_combi[index + 1] for index, cur_sum in enumerate(sum_arr)):
        print(' '.join(map(str, cur_combi)))