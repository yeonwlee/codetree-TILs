def one_to_end_number(number: int) -> None:
    if 1 > number:
        return
    
    one_to_end_number(number - 1)
    print(number, end=" ")


def end_number_to_one(number: int) -> None:
    if 1 > number:
        return
    
    print(number, end=" ")
    end_number_to_one(number - 1)


end_number = int(input())
one_to_end_number(end_number)
print()
end_number_to_one(end_number)