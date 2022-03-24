# 1. 제너레이터 함수

# 제너레이터 함수는 제너레이터 객체를 반환하는 함수이다.
# 제너레이터 객체는 일종의 이터레이터 객체이다.

# caller 함수는 제너레이터 함수를 호출하여 제너레이터 객체를 얻고
# next(gen)으로 제너레이터 함수 내부를 실행한다
# 실행 도중에 yield 키워드를 마주치게 되면
# 제너레이터 함수는 자신의 실행과 관련된 상태(스택, 실행위치 등)을
# caller 함수에게 제어권을 양보하면서 yield 키워드의 뒤에오는 값을 호출한다.

def gen():
    yield 1
    yield 2

g = gen()
print(g.__next__())
print(g.__next__())

# 2. 코루틴
# 코루틴을 호출하면 코루틴 객체가 반환된다.
# 코루틴 객체는 제너레이터 객체에 한가지 기능이 추가된 함수이다.
# 값을 메인 루틴에서 코루틴으롷 전달한다.
# 만약 caller 함수가 코루틴 객체의 send(값) 메소드를 호출하면
# 실행이 중단되었던 부분에 위치한 yield 키워드 구문의 자리를 send(값)으로 보낸다.

def co():
    x = yield 1
    yield x

c = co()
print(c.__next__())
print(c.send(100))

# 정리하자면
# 코루틴 내부에서 yield 값 = 코루틴이 caller에게 값을 넘겨주는것
# 메인 루틴에서 co.send(값)= 코루틴 내부로 값을 전달하는것

# 코루틴을 간단하게 만드는 방법으로 함수의 앞에 async 키워드를 붙인다.

# 3. 중첩 제너레이터

# 아래의 예시처럼 제너레이터가 내부에서 또 다른 제너레이터를 실행하는 경우

def generator1():
    yield 1
    yield 2
    yield 3

def generator2():
    go1 = generator1()
    for element in go1:
        yield element

g = generator2()
print(g.__next__())
print(g.__next__())
print(g.__next__())