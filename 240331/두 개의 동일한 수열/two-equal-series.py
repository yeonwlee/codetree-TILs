length_of_list = int(input())
arr1 = sorted(list(map(int, input().split())))
arr2 = sorted(list(map(int, input().split())))

print("Yes" if arr1 == arr2 else "No")