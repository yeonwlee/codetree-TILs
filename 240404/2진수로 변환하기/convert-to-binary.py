digit_num = int(input())

#bin
#print(bin(digit_num)[2:])

def make_binary_num(num: int) -> None:
    if num < 2:
        print(num, end="")
        return
    
    div_result, remain = divmod(num, 2)
    make_binary_num(div_result)
    print(remain, end="")
    

make_binary_num(digit_num)