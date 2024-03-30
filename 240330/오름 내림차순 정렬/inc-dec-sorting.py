number = int(input())
numbers = list(map(int, input().split()))

sorted_numbers = sorted(numbers)

for num in sorted_numbers:
    print(num, end=" ")

print()

for num in sorted_numbers[::-1]:
    print(num, end=" ")