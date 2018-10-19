# 자료형의 값을 저장하는 공간, 변수
# c나 java처럼 변수의 자료형을 함께 쓸 필요가 없다. >> 추상자료형
# 변수명 = 변수에 저장할 값
# 변수란: 파이썬에서 사용하는 변수는 객체를 가리키는 것이라고 말할 수 있다.
a = [1, 2, 3]
print(id(a)) # 주소값을 확인 할 수 있다. 콜 바이 레퍼런스인듯하다. 자바는 콜 바이 밸류였는데

# 리스트를 변수에 넣고 복사하고자 할 때
a = [1, 2, 3]
b = a
print(b)
print(id(a))
print(id(b))
print(a is b) # 자바에서 ==과 같다. 같은 참조값(주소를 가리키는지, 객체를 가리키는지)을 물어봄
a[1] = 4
print(a)
print(b)

#[:] 이용: '[:]'은 리스트 전체를 가리킨다
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)

# copy 모듈 이용
from copy import copy
b = copy(a)
print(b)
print(b is a) # b에 a값을 넣었기 때문에 주소값은 다름.

# 변수를 만드는 여러 가지 방법
a, b = {'python', 'life'}
print(a)
print(b)
a = b = 'python'
a = 3
b = 5
a, b = b, a # 값 바꾸기
print(a)

# 연습문제
# 문제1. 변수와 객체1
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
# 문제2. 변수와 객체2
a = [1, 2, 3]
b = a
print(a is b)
# 문제3. 객체의 변경
a = b = [1, 2, 3]
a[1] = 4
print(b)
# 문제4. 리스트 복사1
a = [1, 2, 3]
b = a[:]
print(a is b)
# 문제5. 리스트 복사2
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)
# 문제6. 리스트의 더하기와 extend
a = [1, 2, 3]
a = a + [4, 5]
print(a)
print(id(a)) # 같은 주소값을 바라보고있지 않다.
a = [1, 2, 3]
a.extend([4, 5])
print(a)
print(id(a)) # 같은 주소 값을 바라본다.
# 문제7. 리스트복사3: a 리스트를 copy하여 b리스트르 다음과 같이 만들었다.
a = [1, [2, 3], 4]
b = a[:]
a[1][0] = 5
print(a)
print(b)
from copy import deepcopy
a = [1, [2, 3], 4]
b = deepcopy(a) # 얕은 카피 / 깊은 카피. [2,3]은 하나의 객체로 인식되기 때문에 다르게 인식하기 위해서는 딥카피가 필요하다.
a[1][0] = 5
print(a)
print(b)
