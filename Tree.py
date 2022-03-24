# 트리 Tree

# 1. 트리 (Tree) 구조
# 트리: Node와 Branch를 이용해서, 사이클을 이루지 않도록 구성한 데이터 구조
# 탐색(검색) 알고리즘 구현을 위해 많이 사용됨

# 2. 알아둘 용어
# Root Node: 트리 맨 위에 있는 노드
# Level: 최상위 노드를 Level 0으로 하였을 때, 하위 Branch로 연결된 노드의 깊이를 나타냄
# Leaf Node (Terminal Node): Child Node가 하나도 없는 노드
# Depth: 트리에서 Node가 가질 수 있는 최대 Level

# 3. 종류
# 이진 트리: 노드의 최대 Branch가 2인 트리
# 이진 탐색 트리 (Binary Search Tree, BST): 왼쪽 노드는 해당 노드보다 작은 값, 오른쪽 노드는 해당 노드보다 큰 값을 가지고 있음!

# 4. 활용
# 계층 관계를 가진 데이터를 저장할 때
# 정렬(힙 정렬), 압축(후프만 코드)을 매우 똑똑하게 처리하고싶을때
# 우선순위 큐(힙으로), 딕셔너리(BST), 셋(BST)와 같은 추상 자료형을 구현할때

# 이진 탐색 트리
# 1.정의
# 임의의 어떤 노드에 대해 그 왼쪽 부분 트리의 모든 데이터 < 임의 노드 데이터 < 오른쪽 부분 트리의 모든 데이터

# 2.활용
# 이진 탐색 트리는 딕셔너리와 셋을 구현하는데 쓰임
# 데이터를 빠르게 찾을수있다

# 3.성질
# 이진 탐색 트리를 in-order 방법으로 순회하면 저장된 데이터들을 정렬된 순서대로 출력할수있다.
# 이진 탐색 트리는 완전 이진 트리가 아닌 경우가 더 많다
# 그렇기 때문에 노드가 n개 있을 때, 높이 h가 항상 O(log(n))이라고 할 수 없다
# 최악의 경우 예로 들자면, 이진 탐색 트리의 높이는 O(n)
#예를 들면 이진 탐색 트리에 데이터로 1,2,3,4,5,6 을 순서대로 삽입하면 트리가 한쪽으로 편향

#이진탐색 트리 구현
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self, root_node):
        self.root_node = None

    def insert(self, data):
        new_node = Node(data)
        if self.root_node is None:
            self.root_node = new_node
            return
        else: #root 노드가 있으면
            temp_node = self.root_node  # 비교하기 위해 현재 root node를 temp노드로 저장
            while True:
                if new_node.data < temp_node.data: #root보다 작으면 왼쪽으로 가야하고
                    if temp_node.left is None: #왼쪽 자식노드가 없다면
                        temp_node.left = new_node #새로운 노드가 왼쪽 자식 노드로 저장
                        break

                    else:  # temp_node 왼쪽 자식 노드가 있다면, 또 밑의 자식과 비교하기위해 temp_node로 바꿔 비교한다.
                        temp_node = temp_node.left  # while문 순회하면서 비교


                else:  # new_node > temp_node : root보다 크므로 오른쪽으로 가야함
                    if temp_node.right is None: #오른쪽 자식 노드가 비여있으면
                        temp_node.right = new_node #새로운 노드를 오른쪽 자식 노드에 저장
                        break

                    else:  # root 오른쪽에 노드가 이미 있다면
                        temp_node = temp_node.right  # 그 오른쪽 노드를 temp_node로 변경하고 그 밑에 오른쪽 노드와 비교하기

    def search(self, data):#root노드부터 내가 원하는 값이 어디있는지 순회하면서 탐색
        temp = self.root_node
        while True:
            if temp is None: #root_node가 없으면 데이터 없는거
                return None

            if temp.data == data:
                return temp
            elif temp.data > data:
                temp = temp.left #temp의 왼쪽 자식노드가 temp로 업데이터해서 또 비교
            else:
                temp = temp.right #temp의 오른쪽 자식노드가 temp로 업데이트해

if __name__ == "__main__":
    root_node = Node(1)
    bst = BinarySearchTree(root_node)


#데이터 삽입
bst.insert(7)
bst.insert(8)
bst.insert(4)
bst.insert(5)
bst.insert(11)

#탐색
print(bst.search(7).data)
print(bst.search(4).data)
print(bst.search(11).data)





