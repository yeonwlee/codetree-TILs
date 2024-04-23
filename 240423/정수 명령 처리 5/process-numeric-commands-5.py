num_of_commands = int(input())
arr = []

for _ in range(num_of_commands):
    command = input().split()
    if len(command) == 2:
        command, num = command
    else: 
        command = command[0]

    if command == "push_back":
        arr.append(int(num))
    elif command == "pop_back":
        arr.pop()
    elif command == "size":
        print(len(arr))
    elif command == "get":
        print(arr[int(num) - 1])