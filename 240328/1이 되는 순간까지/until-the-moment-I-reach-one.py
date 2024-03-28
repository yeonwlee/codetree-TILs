# N이 짝수이면 2로 나누고, 
# 홀수이면 3으로 나눈 몫을 취하는 작업을 반복하다가 
#그 값이 1이 되면 그때까지 진행한 작업의 횟수를 구하는 프로그램
def solution(number: int, count: int) -> int:
    if number == 1:
        return count
    
    if number % 2 == 0:
        return solution(number // 2, count + 1)
    else:
        return solution(number // 3, count + 1)


number = int(input())
print(solution(number, 0))