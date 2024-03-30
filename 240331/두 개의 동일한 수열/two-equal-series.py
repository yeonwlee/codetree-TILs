length_of_list = int(input())
arr1 = sorted(list(map(int, input().split())))
arr2 = sorted(list(map(int, input().split())))

print("Yes" if all(True if elem1 == elem2 else False for elem1, elem2 in zip(arr1, arr2)) else "No")