import sys
from itertools import combinations
# A ≤ B ≤ C ≤ D 찾아내기

# 조건상, a,b,c,d 중 음수는 없음(1 ≤ 모든 입력값 ≤ 40)
# 그렇다면 정렬한 후에 왼쪽에서부터 4개의 숫자가 a, b, c, d에 할당될 가능성이 높음
infos = sorted(tuple(map(int, input().split())))

for a_index in range(15):
    a = infos[a_index]
    for b_index in range(a_index + 1, 15):
        b = infos[b_index]
        for c_index in range(b_index + 1, 15):
            c = infos[c_index]
            for d_index in range(c_index + 1, 15):
                d = infos[d_index]
                # a + b, b + c, c + d, d + a, a + c, b + d, a + b + c, a + b + d, a + c + d, b + c + d, a + b + c + d
                sum_values = [sum(num_combi) for pair_num in range(2, 5) for num_combi in combinations([a, b, c, d], pair_num)]
                sum_values.extend([a, b, c, d])
                sum_values.sort()
                if sum_values == infos:
                    print(a, b, c, d)
                    sys.exit()