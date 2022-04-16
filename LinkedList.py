# 링크드 리스트 (Linked List)

# 순차적으로 연결된 공간에 데이터를 나열하는 데이터 구조
# 링크드 리스트는 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조

# 간단한 링크드 리스트 예
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Node와 Node 연결하기 (포인터 활용)
node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1

# 링크드 리스트로 데이터 추가하기
def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

# 링크드 리스트 데이터 출력하기(검색하기)
node = head
while node.next:
    print(node.data)
    node = node.next
print (node.data)

# 파이썬 객체지향 프로그래밍으로 링크드 리스트 구현하기

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


linkedlist1 = NodeMgmt(0)
for data in range(1, 10):
    linkedlist1.add(data)
print(linkedlist1.desc())

# 링크드 리스트의 복잡한 기능2 (특정 노드를 삭제)
def delete(self, data):
    if self.head == '':
        print("해당 값을 가진 노드가 없습니다.")
        return

    if self.head.data == data:
        temp = self.head
        self.head = self.head.next
        del temp
    else:
        node = self.head
        while node.next:
            if node.next.data == data:
                temp = node.next
                node.next = node.next.next
                del temp
                return
            else:
                node = node.next

linkedlist1.delete(9)
print(linkedlist1.desc())

# 연습2: 위 코드에서 노드 데이터가 특정 숫자인 노드를 찾는 함수를 만들고, 테스트해보기
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head == '':
            print('해당 값을 가진 노드가 없습니다.')
            return
        if self.head.data == data:  # 경우의 수1: self.head를 삭제해야할 경우 - self.head를 바꿔줘야 함
            temp = self.head  # self.head 객체를 삭제하기 위해, 임시로 temp에 담아서 객체를 삭제했음
            self.head = self.head.next  # 만약 self.head 객체를 삭제하면, 이 코드가 실행이 안되기 때문!
            del temp
        else:
            node = self.head
            while node.next:  # 경우의 수2: self.head가 아닌 노드를 삭제해야할 경우
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    pass
                else:
                    node = node.next

    def search_node(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next

# 테스트
node_mgmt = NodeMgmt(0)
for data in range(1, 10):
    node_mgmt.add(data)

node = node_mgmt.search_node(4)
print (node.data)

# 더블 링크드 리스트(Doubly linked list)

class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print (node.data)
            node = node.next

double_linked_list = NodeMgmt(0)
for data in range(1, 10):
    double_linked_list.insert(data)
print(double_linked_list.desc())

# 연습3: 위 코드에서 노드 데이터가 특정 숫자인 노드 앞에 데이터를 추가하는 함수를 만들고, 테스트해보기

class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def search_from_head(self, data):
        if self.head == None:
            return False

        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False

    def search_from_tail(self, data):
        if self.head == None:
            return False

        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False

    def insert_before(self, data, before_data):
        if self.head == None:
            self.head = Node(data)
            return True
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node == None:
                    return False
            new = Node(data)
            before_new = node.prev
            before_new.next = new
            new.prev = before_new
            new.next = node
            node.prev = new
            return True

double_linked_list = NodeMgmt(0)
for data in range(1, 10):
    double_linked_list.insert(data)
print(double_linked_list.desc())

double_linked_list.insert_before(1.5, 2)
print(double_linked_list.desc())





