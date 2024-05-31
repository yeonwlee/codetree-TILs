'''
우리는 그릇을 ( 또는 ) 로 표현하여 쌓은 높이를 알아보려고 합니다.
그릇의 높이는 10cm입니다. 단, 겹쳐진 경우는 5, 반대 방향으로 쌓은 경우는 그대로 10이 더해집니다.
(( 는 15, () 또는 )( 는 20입니다.
그릇의 모양이 주어졌을 때 그릇의 높이를 구하는 프로그램을 작성해보세요.
'''

plates = input()

cur_pos = plates[0]
height = 10
for index in range(1, len(plates)):
    if cur_pos == plates[index]:
        height += 5
    else:
        height += 10
        cur_pos = plates[index]

print(height)