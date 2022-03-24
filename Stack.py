# 스택
# 데이터를 제한적으로 접근할수있는 구조
# 한쪽 끝에서만 자료를 넣거나 뺄수 있는 구조
# 가장 나중에 쌓은 데이터를 가장 먼저 빼낼수 있는 데이터 구조
# 책 쌓기 연상

#1.스택구조
# 스택은 LIFO(Last In First Out) 또는 FILO(First In Last Out) 데이터 관리 방식을 따른다.
# 대표적인 스택의 활용
# 컴퓨터 내부의 프로세스 구조의 함수 동작 방식

#2.주요 기능
# push(): 데이터를 스택에 넣기
# pop(): 데이터를 스택에서 꺼내기

#3.자료구조 스택의 장단점
# 장점
# 구조가 단순해서 구현이 쉽다
# 데이터 저장/읽기 속도가 빠르다

#단점
# 데이터 최대 개수를 미리 정해야한다.
# 이로 인해 저장 공간의 낭비가 발생할수있다.

stack_list = list()
stack_list.append(2)
stack_list.append(10)

print(stack_list)
print(stack_list.pop()) #늦게 넣은 10이 먼저 출력
print(stack_list.pop()) #처음 입력한 데이터 2가 출력

# 리스트 변수로 스택을 다루는 pop, push 기능 구현해보기 (pop, push 함수 사용하지 않고 직접 구현해보기)

stack_test = list()

def push(data):
    stack_test.append(data)

def pop():
    data = stack_test[-1] #마지막에 들어온게 제일 먼저 빠져나감
    del stack_test[-1]
    return data

for element in range(1,10):
    push(element) #마지막 원소 9가 나와야 정상

print(stack_test.pop())