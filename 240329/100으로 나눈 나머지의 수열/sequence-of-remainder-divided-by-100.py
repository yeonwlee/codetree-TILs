'''
첫 번째는 2, 두 번째는 4, 세 번째부터는 앞의 두 수의 곱을 100으로 나눈 나머지로 이루어진 수열이 있습니다. 
100 이하의 정수 N을 입력받아 재귀함수를 이용하여 N번째 값을 구하여 출력하는 프로그램을 작성해보세요.
'''
def solution(index: int, memory_dict:dict[int, int]=None) -> int:
    if memory_dict is None:
        memory_dict = {0:2, 1:4}

    if index not in memory_dict:
        memory_dict[index] = solution(index - 1, memory_dict) * solution(index - 2, memory_dict) % 100

    return memory_dict[index]


target_index = int(input()) - 1
print(solution(target_index))