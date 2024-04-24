class Node():
    def __init__(self, data: int):
        self.data: int = data
        self.prev: Node = None
        self.next: Node = None


class DoublyLinkedList():
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.node_count = 0


    def push_front(self, data: int) -> None:
        new_node = Node(data)
        # 연결리스트에 아무것도 없는 경우
        if self.empty():
            new_node.prev = None # 기본적으로 초기화가 None으로 되나 명시적으로 표현
            new_node.next = None
            self.head = new_node
            self.tail = new_node
        elif self.node_count == 1: # 기존에 노드가 하나만 있는 경우
            self.head.prev = new_node
            new_node.prev = None
            new_node.next = self.head
            self.tail = self.head
            self.head = new_node
        else: # 기존에 노드가 2개 이상 있는 경우
            self.head.prev = new_node
            new_node.prev = None
            new_node.next = self.head
            self.head = new_node
        
        self.node_count += 1


    def push_back(self, data: int) -> None:
        new_node = Node(data)
        # 연결리스트에 아무것도 없는 경우
        if self.empty():
            new_node.prev = None # 기본적으로 초기화가 None으로 되나 명시적으로 표현
            new_node.next = None
            self.head = new_node
            self.tail = new_node
        elif self.node_count == 1: # 기존에 노드가 하나만 있는 경우
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node.next = None
            self.head = self.tail
            self.tail = new_node
        else: # 기존에 노드가 2개 이상 있는 경우
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node.next = None
            self.tail = new_node
        
        self.node_count += 1


    def pop_front(self) -> Node:
        # 연결리스트에 아무것도 없는 경우
        if self.empty():
            return None
        elif self.node_count == 1: # 기존에 노드가 하나만 있는 경우
            result = self.head.data
            self.tail = None
            self.head = None
            self.node_count -= 1
            return result
        else: # 기존에 노드가 2개 이상 있는 경우
            result = self.head.data
            self.head.next.prev = None
            self.head = self.head.next
            self.node_count -= 1
            return result


    def pop_back(self) -> Node:
        # 연결리스트에 아무것도 없는 경우
        if self.empty() == 1:
            return None
        elif self.node_count == 1: # 기존에 노드가 하나만 있는 경우
            result = self.tail.data
            self.tail = None
            self.head = None
            self.node_count -= 1
            return result
        else: # 기존에 노드가 2개 이상 있는 경우
            result = self.tail.data
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.node_count -= 1
            return result


    def size(self) -> int:
        return self.node_count


    def empty(self) -> int:
        return 0 if self.node_count > 0 else 1


    def front(self) -> int:
        return self.head.data


    def back(self) -> int:
        return self.tail.data



num_of_commands = int(input())
doubly_linked_list = DoublyLinkedList()

for _ in range(num_of_commands):
    commands = input().split()
    if len(commands) == 1:
        command, num = commands[0], None
    else:
        command, num = commands[0], commands[1]

    cur_method = getattr(doubly_linked_list, command)
    if num is not None:
        cur_method(num)
    else:
        print(cur_method())