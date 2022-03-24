# 큐(Queue)

# 줄서는 행위와 유사
# 가장 먼저 넣은 데이터를 가장 먼저 꺼낼수 있는 구조

# Enqueue = 큐에 데이터를 넣는 기능
# Dequeue = 큐에 데이터를 꺼내는 기능

# 파이썬 queue 자료구조

# 1. Queue(): 가장 일반적인 큐 자료 구조
# 2. LifoQueue(): 나중에 입력된 데이터가 먼저 출력되는 구조(스택 구조와 비슷)
# 3. PriorityQueue() : 데이터마다 우선수위를 넣어서 우선순위가 높은 순으로 데이터를 출력


# Queue()로 큐 만들기
import queue
data_queue = queue.Queue()

data_queue.put(1)
data_queue.put(5)
data_queue.qsize()

print('Queue')
print(data_queue.get())
data_queue.qsize()

# LifoQueue()로 큐 만들기(Last-in, First-out)

# 마지막에 넣은 데이터가 처음에 출력

import queue
data_queue1 = queue.LifoQueue()

data_queue1.put(3)
data_queue1.put(4)
data_queue1.qsize()

print('LifoQueue')
print(data_queue1.get())

#PriorityQueue()로 큐 만들기

#데이터를 넣을때 우선순위 번호를 넣는것
#우선순위가 낮은것부터 출력
#((순위, 데이터)) 순으로 입력

import queue
data_queue2 = queue.PriorityQueue()

data_queue2.put((0,'Have'))
data_queue2.put((2, 'good'))
data_queue2.put((3, 'day'))
data_queue2.put((1, 'a'))

data_queue2.qsize()

print('PriorityQueue')
print(data_queue2.get())
print(data_queue2.get())
print(data_queue2.get())
print(data_queue2.get())

# 리스트 변수로 큐를 다루는 enqueue, dequeue  기능 구현해보기
queue_list = list()
def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data

for element in range(1,10):
    enqueue(element)


print(len(queue_list))

print(dequeue())