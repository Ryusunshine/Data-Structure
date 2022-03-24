# 힙
# 1. 데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리(Complete Binary Tree)
# 2. 부모 노드의 데이터는 자식 노드 데이터보다 크거나 같음

# 힙을 사용하는 이유
# 배열에 데이터를 넣고, 최대값과 최소값을 찾으려면 O(n) 이 걸림
# 이에 반해, 힙에 데이터를 넣고, 최대값과 최소값을 찾으면,  𝑂(𝑙𝑜𝑔𝑛)  이 걸림
# 우선순위 큐와 같이 최대값 또는 최소값을 빠르게 찾아야 하는 자료구조 및 알고리즘 구현 등에 활용됨

# 힙과 이진 탐색 트리의 공통점과 차이점
# 공통점: 힙과 이진 탐색 트리는 모두 이진 트리임
# 차이점:
    # 힙은 각 노드의 값이 자식 노드보다 크거나 같음(Max Heap의 경우)
    # 이진 탐색 트리는 왼쪽 자식 노드의 값이 가장 작고, 그 다음 부모 노드, 그 다음 오른쪽 자식 노드 값이 가장 큼
    # 힙은 이진 탐색 트리의 조건인 자식 노드에서 작은 값은 왼쪽, 큰 값은 오른쪽이라는 조건은 없음
    # 힙의 왼쪽 및 오른쪽 자식 노드의 값은 오른쪽이 클 수도 있고, 왼쪽이 클 수도 있음
    # 이진 탐색 트리는 탐색을 위한 구조, 힙은 최대/최소값 검색을 위한 구조 중 하나로 이해하면됨.

# 힙에 데이터 삽입하기
# 삽입할 노드는 기본적으로 왼쪽 최하단부 노드부터 채워지는 형태로 삽입

# 힙에 데이터 삽입하기 - 삽입할 데이터가 힙의 데이터보다 클 경우 (Max Heap 의 예)
# 먼저 삽입된 데이터는 완전 이진 트리 구조에 맞추어, 최하단부 왼쪽 노드부터 채워짐
# 채워진 노드 위치에서, 부모 노드보다 값이 클 경우, 부모 노드와 위치를 바꿔주는 작업을 반복함 (swap)

# 힙에서 데이터 삭제하기
# 보통 삭제는 최상단 노드 (root 노드)를 삭제하는 것이 일반적임
# 힙의 용도는 최대값 또는 최소값을 root 노드에 놓아서, 최대값과 최소값을 바로 꺼내 쓸 수 있도록 하는 것임
# 상단의 데이터 삭제시, 가장 최하단부 왼쪽에 위치한 노드 (일반적으로 가장 마지막에 추가한 노드) 를 root 노드로 이동
# root 노드의 값이 child node 보다 작을 경우, root 노드의 child node 중 가장 큰 값을 가진 노드와 root 노드 위치를 바꿔주는 작업을 반복함 (swap)

if __name__ == "__main__":
    tree = [None, 1,4,2,4,5,6]

    #힙으로 만들기
    for i in reversed(range(1, len(tree))):
        heapify(tree,i , len(tree))
        print(tree)



# 최소 힙
# 1. 완전 이진 트리(CBT)
# 2. 부모 노드의 데이터는 자식 노드 데이터보다 작거나 같음

# 활용
# 힙 정렬 / 우선순위 큐 구현

# heapify 연산이란?
# 특정 노드가 힙 조건을 만족하도록 원래 위치를 찾아주는 함수
import heapq
from queue import PriorityQueue


def heapify(tree, index, tree_size):
    pass


# 오른쪽 자식 노드 인덱스 구하기
def get_right_child_index(cbt, index):
    right_child_index = index * 2
    if right_child_index < 1 or right_child_index > len(cbt) - 1:
        return None
    else:
        return right_child_index


# 부모 노드 인덱스 구하기
def get_parent_child_index(cbt, index):
    parent_index = index // 2
    if parent_index == 0:  # 인덱스가 0이면 안됨됨
        return None
    else:
        return parent_index


def reverse_heapify(tree, index):  # reverse_heapify = 아래서부터 heapify

    if index == 1:  # 인덱스가 1이면 제일 위에 있는 원소 root
        return  # 부모가 없으니깐 바로 return

    parent_index = get_parent_child_index(tree, index)
    if parent_index is None:  # 부모가 없는경우
        return

    if tree[index] < tree[parent_index]:
        return

    # 위의 if문에 안걸리면 부모가 있다는 뜻. 즉, 부모 노드보다 큰 경우
    tree[index], tree[parent_index] = tree[parent_index], tree[index]  # 둘의 자리를 바꿔준다.
    reverse_heapify(tree, parent_index)  # 재귀 호출로 반복 실행.


# 우선 순위 큐
# 1. 힙으로 만든 추상 자료형이다.
# 2. 우선순위가 높은 순서대로 데이터가 나온다.

# 정렬된 동적 배열 또는 링크드리스트로 만든 우선순위 큐의 삽입 연산: O(n)
# 정렬된 동적 배열 또는 링크드리스트로 만든 우선순위 큐의 팝 연산: O(1)

# 힙으로 만든 우선순위 큐의 삽입 연산: O(log n)
# 힙으로 만든 우선순위 큐의 팝 연산: O(log n)

# 우선 순위 큐의 트리 모양은 왼쪽은 작은수, 오른쪽으로 갈수록 큰숫자가 정렬돼!

class PriorityQueue:
    def __init__(self):
        self.heap = [None]  # 우선 아무것도 없는 heap하나 만든다.

    # 힙에 데이터 삽입하기
    # 1. 힙의 마지막 인덱스에 데이터 삽입
    # 2. 삽입한 데이터와 부모를 비교해서 위치를 조정한다.
    # 3. 올바르게 될때까지 2번 재귀적으로 반복한다.

    def insert(self, data):
        self.heap.append(data)  # 마지막에 추가
        reverse_heapify(self.heap, len(self.heap) - 1)  # 마지막에 추가한 원소 reverse_heapify 수행해서 맞는 위치로.

    # 힙에서 데이터 삭제
    # 1. 삭제할때는 root노드와 마지막 노드 위치를 바꾼다.
    # 2. 마지막 위치로 간 원래 root 노드의 데이터를 별도 변수에 저장하고 노드는 힙에서 지운다.
    # 3. 새로운 root 노드를 대상으로 heapify해서 망가진 힙 속성을 복원한다.
    # 4. 2단계에서 따로 저장해둔 최우선 순위 데이터를 리턴한다.

    def extract_max(self):
        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]  # 1번 수행
        max_value = self.heap[-1]  # 2번 수행
        self.heap.remove(max_value)
        # heapify(tree, index, tree_size)
        heapify(self.heap, 1, len(self.heap))  # 3번 수행 하면 다시 heap조건 만족

        return max_value

    if __name__ == "__main__":
        priority_queue = PriorityQueue()

        priority_queue.insert(1)
        priority_queue.insert(8)
        priority_queue.insert(5)
        priority_queue.insert(3)
        priority_queue.insert(10)

        print(priority_queue)

        print(priority_queue.extract_max())
        print(priority_queue.extract_max())
        print(priority_queue.extract_max())
        print(priority_queue.extract_max())
        print(priority_queue.extract_max())


        # 원래는 이 함수임
        # import heapq
        q = []
        heapq.heappush(q, 10)
        heapq.heappush(q, 5)
        heapq.heappush(q, 8)
        heapq.heappush(q, 7)
        print(q)
