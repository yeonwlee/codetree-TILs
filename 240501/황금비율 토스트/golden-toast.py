## TODO: 처음부터 다시
class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        # 시작과 끝에 더미 노드를 생성
        self.head = Node()  # 시작 더미 노드
        self.tail = Node()  # 끝 더미 노드
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_after(self, node, data):
        if node == self.tail:
            return  # 더미 노드 뒤에는 삽입 불가
        new_node = Node(data)
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node
        return new_node

    def delete_node(self, node):
        if node == self.tail:
            return  # 더미 노드는 삭제 불가
        node.prev.next = node.next
        node.next.prev = node.prev

    def to_string(self):
        result = []
        current = self.head.next
        while current != self.tail:
            result.append(current.data)
            current = current.next
        return ''.join(result)

def process_commands(n, m, initial_breads, commands):
    dll = DoublyLinkedList()
    current = dll.head

    for char in initial_breads:
        current = dll.insert_after(current, char)

    current = dll.tail.prev  # 초기 위치는 모든 빵의 맨 마지막

    for command in commands:
        if command == 'L':
            if current != dll.head:  # 더미 노드가 아니면
                current = current.prev
        elif command == 'R':
            if current.next != dll.tail:  # 더미 노드가 아니면
                current = current.next
        elif command.startswith('P '):
            char = command.split()[-1]
            current = dll.insert_after(current, char)  # 삽입 후 새 노드가 현재 위치
        elif command == 'D':
            if current.next != dll.tail:  # 마지막 더미 노드가 아니면
                dll.delete_node(current.next)  # 다음 노드 삭제

    return dll.to_string()

# 입력 예제
n, m = map(int, input().split())
initial_breads = input()
commands = [input() for _ in range(m)]

# 결과 출력
result = process_commands(n, m, initial_breads, commands)
print(result)