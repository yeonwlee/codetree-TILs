import math

def print_lcm(num1: int, num2: int) -> None:
    print(math.lcm(num1, num2))    
    
    
num1, num2 = map(int, input().split())
print_lcm(num1, num2)