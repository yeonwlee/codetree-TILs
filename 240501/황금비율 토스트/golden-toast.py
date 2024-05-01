## TODO: 처음부터 다시
class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()  # 시작 더미 노드
        self.tail = Node()  # 끝 더미 노드
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_after(self, node, data):
        new_node = Node(data)
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node
        return new_node

    def delete_node(self, node):
        if node == self.tail:
            return None  # 타일 노드는 삭제할 수 없습니다.
        node.prev.next = node.next
        node.next.prev = node.prev
        return node.next  # 삭제된 노드의 다음 노드를 반환

    def to_string(self):
        result = []
        current = self.head.next
        while current != self.tail:
            result.append(current.data)
            current = current.next
        return ''.join(result)

def process_commands(initial_breads, commands):
    dll = DoublyLinkedList()
    current = dll.head

    for char in initial_breads:
        current = dll.insert_after(current, char)

    for command in commands:
        if command == 'L':
            if current != dll.head:
                current = current.prev
        elif command == 'R':
            if current.next != dll.tail:
                current = current.next
        elif command.startswith('P '):
            char = command.split()[-1]
            current = dll.insert_after(current, char)
        elif command == 'D':
            if current.next != dll.tail:
                current = dll.delete_node(current.next)  # 삭제 후 다음 노드로 이동

    return dll.to_string()

# 입력 부분 처리
num_of_bread, num_of_commands = map(int, input().split())
bread_info = input()
commands = [input().strip() for _ in range(num_of_commands)]

# 결과 출력
result = process_commands(bread_info, commands)
print(result)