# 함수란 무엇인가: 입력값을 가지고 어떤 일을 수행한 다음 그 결과물을 내어놓는 것
# 함수를 사용하는 이유: 반복되는 부분이 있을 경우 반복적으로 사용되는 가치 있는 부분을 묶어 만드는 것
# 자바의 메소드 같은 것
# 함수의 구조
"""
def 함수명(매개변수):
    <수행할 문장1>
    <수행할 문장2>
    ...
"""
def sum(a,b):
    return a+b
print(sum(3,4))

# 매개변수와 인수
"""
매개변수(parameter)와 인수(arguments)는 혼용해서 사용되는 헷갈리는 용어
매개변수는 함수에 입력으로 전달된 값ㅇ르 받는 변수를 의미하고 인수는 함수를 호출할 때 전달하는 입력값을 의미한다.
"""
def sum(a,b): # a, b는 매개변수
    return a+b
print(sum(3,4)) # 3,4는 인수

# 입력값과 결과값에 따른 함수의 형태
# 입력값 --> 함수 --> 리턴값


# 일반적인 함수: 입력값이 있고 결과값이 있는 함수가 일반적인 함수이다.
"""
def 함수이름(매개변수):
    <수행할 문장>
    ...
    return 결과값
"""
# 입력값이 없는 함수
def say():
    return 'hi'
a = say()
print(a)
# 결과값을 받을 변수 = 함수명()

# 결과값이 없는 함수
def sum(a,b):
    print("%d, %d의 합은 %d입니다." %(a,b,a+b))
"""
결과값이 없는 함수는 호출해도 돌려주는 값이 없기 때문에 다음과 같이 사용한다.
print(sum(3,4))
함수명(입력인수1, 입력인수2,...)
"""

# 입력값도 결과값도 없는 함수
def say():
    print('Hi')
"""
입력 인수를 받는 매개변수도 없고 return문도 없으니 입력값도 결과값도 없는 함수이다. 이 함수를 사용하는 방법은
"""
say() # 요렇게. 함수명만 달랑 적으면 된다.
print(say()) # 이렇게 하면 아무것도 안나온다.

# 매개변수 지정하여 호출하기: 함수를 호출할 때 매개변수를 지정하여 호출할 수도 있다.
def sum(a,b):
    return a+b
print(sum(a=3,b=7))

# 입력값이 몇 개가 될지 모를 때는 어떻게 해야 하는가
"""
입력값이 여러 개일 때 그 입력값들을 모두 더해주는 함수가 있다면
def 함수이름(*매개변수):
    <수행할 문장>
    ...
"""
# 여러 개의 입력값을 받는 함수 만들기
"""
sum_many(1,2)라면 3을, sum_many(1,2,3)이라면 6을 출력하는 함수를 만들어보자
"""
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum+i
    return sum
result = sum_many(1,2,3)
print(result)

def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result = result + i
    elif choice=="mul":
        result = 1
        for i in args:
            result = result*i
    return result
result = sum_mul("mul",1,2,3,4,5)
print(result)

# 키워드 파라미터 kwargs
"""
키워드 파라미터인 **kwargs는 keyword arguments의 약어이다.
**kwargs는 *args와 달리 *이 두 개 사용된다.
"""
def func(**kwargs):
    print(kwargs)
func(a=1)
func(name='foo',age=3)
"""
key=value 형태를 주었을 때 입력 값 전체가 kwargs라는 딕셔너리에 저장된다.
즉, **kwargs는 모든 key=value 형태의 입력인수가 저장되는 딕셔너리 변수이다.
또한 키워드 인수 뒤에 키워드 형태가 아닌 인수는 올 수 없게 된다.
"""

# 함수의 결과 값은 언제나 하나이다.
def sum_and_mul(a,b):
    return a+b, a*b
result = sum_and_mul(3,4)
print(result) # 결과값으로 (7,12)라는 튜플 값을 가지게 된다.

# return의 또 다른 쓰임새
"""
어떤 특별한 상황이 되면 함수를 빠져나가고자 할 때는 return을 단독으로 써서 함수를 즉시 빠져나갈 수 있다.
"""
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s가 아니다" % nick)
say_nick("바보")
say_nick("헤헷")

# 매개변수에 초기값 미리 설정하기
def say_myself(name,age,man=True):
    print("나의 이름은 %s입니다." % name)
    print("나의 나이는 %d입니다." % age)
    if man:
        print("남자")
    else:
        print("여자")
say_myself("홍길동",24,False)
say_myself("길길동",23)

# 함수 안에서 선언된 변수의 효력 범위
a=1
def vartest(a):
    a = a+1
print(a) # 결과로 2가 아닌 1이 나온다.

def varttest(b):
    b = b + 1
    return b
print(varttest(3))

# lambda
"""
람다는 함수를 생성할 때 사용하는 예약어로, def와 동일한 역할을 하낟. 보통 함수를 한 줄로 간결하게 만들 때 사용한다. 
def를 해야할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰인다.
사용법:
lambda 매개변수1, 매개변수2,....: 매개변수를 이용한 표현식
"""
sum = lambda a, b: a+b
print(sum(3,4))
def sum(a, b):
    return a+b
print(sum(4,5))

# def가 있는데도 lambda를 사용하는 이유는 def를 쓸 수 없는 곳에 사용하기 위해
myList = [lambda a,b:a+b, lambda a,b:a*b]
print(myList[0](8,7))

# 연습문제
# 문제1: 주어진 자연수가 홀수인지 짝수인지 판별해주는 함수를 작성하시오
n = int(input("숫자를 입력하세요"))
def isOdd(n):
    if n%2==0:
        print("짝수")
    else:
        print("홀수")
isOdd(n)

# 문제2: 평균값 계산: 입력으로 들어오는 모든 수의 평균값을 계산해주는 함수를 작성해보자.(단, 입력으로 들어오는 수의 갯수는 정해져있지 않다)
def avgValue(*args):
    avg = 0
    for i in args:
        avg += i
    return avg/len(args)
print(avgValue(3,6,9))

# 문제3: 구구단 출력: 입력을 자연수 n(2부터 9까지의 자연수)으로 받았을 때, n에 해당되는 구구단을 출력하는 함수를 작성해보자
n = int(input("2부터 9까지의 자연수 중 하나를 입력하세요: "))
def gugu(n):
    for i in range(1,10):
        print("%dx%d=%d" % (n, i, (n*i)))
gugu(n)