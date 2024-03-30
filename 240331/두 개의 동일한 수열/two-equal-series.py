length_of_list = int(input())
arr1 = sorted(list(map(int, input().split())))
arr2 = sorted(list(map(int, input().split())))

# print("Yes" if arr1 == arr2 else "No") #리스트가 달라도 전체를 비교하기 때문에 데이터가 커질 경우 연산이 길어질 수 있음
print("Yes" if all(elem1 == elem2 for elem1, elem2 in zip(arr1, arr2)) else "No") #조금 더 장황하긴 함