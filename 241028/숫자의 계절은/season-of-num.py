spring = {3, 4, 5}
summer = {6, 7, 8}
fall = {9, 10, 11}
winter = {12, 1, 2}

month = int(input())
if month in spring:
    print('Spring')
elif month in summer:
    print('Summer')
elif month in fall:
    print('Fall')
elif month in winter:
    print('Winter')