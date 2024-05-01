class Node:
    def __init__(self, data: str) -> None:
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0
        self.cur_position = None


    def push_front(self, data: str) -> Node:
        new_node = Node(data)
        new_node.prev = None
        if self.get_count():
            new_node.next = self.head
            self.head.prev = new_node
        else:
            new_node.next = None
        self.head = new_node
        self.count += 1

        return self.head
    

    def push_back(self, data: str) -> Node:
        new_node = Node(data)
        new_node.next = None
        if self.get_count():
            new_node.prev = self.tail
            self.tail.next = new_node
        else:
            self.head = new_node
            new_node.prev = None
        self.tail = new_node
        self.count += 1

        return self.tail
    

    def del_node(self, node: Node) -> Node:
        next_position: Node = node.next
        if node == self.begin(): # 지우는게 head일 경우
            self.head = node.next
            self.head.prev = None

            node.next = None
            next_position = self.begin()
        elif node == self.end(): # 지우는게 tail일 경우
            self.tail = node.prev
            self.tail.next = None

            node.prev = None
            next_position = self.end()
        else: 
            node.next.prev = node.prev
            node.prev.next = node.next
            node.prev = None
            node.next = None
        
        self.count -=1

        return next_position
            
            
    def add_node(self, node: Node, data) -> Node: #주어진 노드의 위치에 넣음
        next_position: Node = None
        if node == self.begin():
            next_position = self.push_front(data)
        elif node == self.end():
            next_position = self.push_back(data)
        else:
            new_node = Node(data)
            new_node.prev = node
            new_node.next = node.next
            node.next.prev = new_node
            node.next = new_node
            next_position = new_node.next
            self.count += 1

        return next_position


    def get_next_node(self, node: Node) -> Node:
        return node.next


    def get_count(self):
        return self.count
    

    def begin(self):
        return self.head


    def end(self):
        return self.tail

        

num_of_bread, num_of_command = map(int, input().split())

status_of_bread = list(input())

#연결리스트 세팅
doubly_linked_list = DoublyLinkedList()
for bread_info in status_of_bread:
    doubly_linked_list.push_back(bread_info)

#이터레이터 세팅
iterator = doubly_linked_list.end()
for _ in range(num_of_command):
    secret_command = input().split()
    if secret_command[0] == 'L': # 바로 앞에 있는 빵을 건너뛴 위치로 변경
        if iterator.prev is not None:
            iterator = iterator.prev
    elif secret_command[0] == 'R': # 바로 뒤에 있는 빵을 건너뛴 위치로 변경
        if iterator.next is not None:
            iterator = iterator.next
    elif secret_command[0] == 'D': #바로 뒤에 있는 빵 제거
        if iterator == doubly_linked_list.end():
            doubly_linked_list.del_node(iterator)
        elif iterator.next is not None:
            iterator = doubly_linked_list.del_node(iterator.next)
    elif secret_command[0] == 'P': #가리키는 위치에 식빵 추가
        iterator = doubly_linked_list.add_node(iterator, secret_command[1])


iterator = doubly_linked_list.begin()
while iterator != None:
    print(iterator.data, end="")
    iterator = iterator.next