length_of_list = int(input())
arr1 = list(map(int, input().split())).sorted()
arr2 = list(map(int, input().split())).sorted()

print("Yes" if arr1 == arr2 else "No")