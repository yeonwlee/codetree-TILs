import sys
import math

input = sys.stdin.readline

height, weight = map(int, input().rstrip().split())
bmi: int = math.trunc((weight * 10000) / (height ** 2))
print(bmi)
if bmi >= 25:
    print("Obesity")