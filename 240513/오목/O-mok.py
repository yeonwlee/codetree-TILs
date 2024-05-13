def is_win(stone_color:int, row_index:int, col_index:int) -> tuple[int]:
    # 오른쪽으로 확인
    for col in range(col_index, col_index + 5):
        if omok[row_index][col] != stone_color:
            break
    else: 
        return (row_index, (col_index + 5) // 2 + 1)
    
    # 왼쪽 대각선 아래로 확인
    for col in range(col_index + 5, col_index - 1, -1):
        row = row_index
        if omok[row][col] != stone_color:
            break
        row += 1
    else:
        return ((row_index + 5) // 2 + 1, col_index // 2 + 1)

    # 아래로 확인
    for row in range(row_index, row_index + 5):
        if omok[row] != stone_color:
            break
    else:
        return ((row_index + 5) // 2 + 1, col_index)

    # 오른쪽 대각선 아래로 확인
    for col in range(col_index, col_index + 5):
        row = row_index
        if omok[row][col] != stone_color:
            break
        row += 1
    else:
        return ((row_index + 5) // 2 + 1, (col_index + 5) // 2 + 1)

    return None


omok = [
    list(map(int, input().split()))
    for _ in range(19)
]

# 오른쪽, 왼쪽대각선 아래, 아래, 오른쪽대각선 아래
done = False
for row_index in range(len(omok) - 5):
    for col_index in range(len(omok) - 5):
        if omok[row_index][col_index] != 0:
            if (result:=is_win(omok[row_index][col_index], row_index, col_index)) is not None:
                print(omok[row_index][col_index])
                print(result[0]+1, result[1]+1, sep=' ')
                done = True
                break
    if done:
        break
else:
    print(0)