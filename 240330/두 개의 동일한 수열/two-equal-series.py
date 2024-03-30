length_of_list = int(input())
arr1 = list(map(int, input().split())).sort()
arr2 = list(map(int, input().split())).sort()

print("Yes" if arr1 == arr2 else "No")