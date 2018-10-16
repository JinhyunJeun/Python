# list자료형
# list indexing
a = [1, 2, 3]
print(a)
print(a[0]+a[2])
print(a[-1])
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[-1][0])
a = [1, 2, ['a', 'b', ['life', 'is']]]
print(a[2][2][0])


# list slicing
a = [1, 2, 3, 4, 5]
print(a[0:2]) # 마지막번째는 포함되지 않는다
a = "12345"
print(a[0:2]) # 자바의 substring과 같음
a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
print(b, c)

# 중첩된 리스트에서 슬라이싱하기
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])
print(a[3][:2])

# list연산자: +기호로 더할 수 있고 *기호로 반복할 수 있다.
# 1) list더하기(+)
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

# 2) list반복하기(*)
a = [1, 2, 3]
print(a*3)


# list의 수정, 변경과 삭제
# 1. 리스트에서 하나의 값 수정하기
a = [1, 2, 3]
a[2] = 4
print(a)
# 2. 리스트에서 연속된 범위의 값 수정하기
print(a[1:2])
a[1:2] = ['a', 'b', 'c']
print(a)
# 3. []사용해서 리스트 요소 삭제하기
a[1:3] = []
print(a)
# 4. del함수 사용해 리스트 요소 삭제하기
del a[1]
print(a)

# list관련 함수들
# list에 요소 추가
a = [1, 2, 3]
a.append(4)
print(a)
a.append([5, 6])
print(a)

# list 정렬(sort): sort함수는 list의 요소들을 순서대로 정렬해준다.
a = [1, 4, 3, 2]
a.sort()
print(a)

# list 뒤집기(reverse): reverse함수는 list를 역순으로 뒤집어준다. 이때 list요소들을 정렬 후 역순으로 정렬하는 것이 아니라 그냥 현재의
#                      요소들을 거꾸로 뒤집는다.
a = ['a', 'c', 'b']
a.reverse()
print(a)
#
# 위치반환(index): index(x) 함수는 리스트에 x라는 값이 있으면 x의 위치값을 반환한다. JAVA의 indexOf와 같음
a = [1, 2, 3]
print(a.index(3)) # 해당하는 요소가 없다면 리턴없이 에러를 뿜는다.

# list에 요소 삽입(insert): insert(a, b)는 list의 a번째 위치에 b를 삽입하는 함수이다.
a.insert(0, 'a')
print(a)

# list요소 제거(remove): remove(x)는 list에서 첫 번째로 나오는 x를 제거하는 함수이다.
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)

# list 요소 끄집어내기(pop): pop()은 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제하는 함수이다.
a = [1, 2, 3]
print(a.pop())
print(a)

# list에 포함된 요소 x의 갯수 세기(count)
a = [1, 2, 3, 1]
print(a.count(1))

# list 확장(extend): extend(x)에는 list만 올 수 있으며 원래의 a list에 x list를 더하게 된다.
a = [1, 2, 3]
a.extend([4, 5])
print(a)
b = [6,7]
a.extend(b)
print(a)



# 문제1. list indexing, a list를 이용하여 you too 를 출력하시오.
a = ['life', 'is', 'too', 'short', 'you', 'need', 'python']
a.reverse()
print(a[2], a[4])

# 문제2. list join, list b를 life is too short로 출력해보자
b = ['life','is','too','short']
print(" ".join(b))

# 문제3. list의 갯수
a = [1, 2, 3]
print(len(a))

# 문제4. list의 append, extend / list에 [4,5]를 apend 했을 때와 extend 했을 때의 차이
a = [1, 2, 3]
a.append([4,5])
print(a)
a = [1, 2, 3]
a.extend([4,5])
print(a)

# 문제5. list 정렬
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# 문제6. list 삭제: a = [1, 2, 3, 4, 5]를 a = [1, 3, 5]로 만들어보자
a = [1, 2, 3, 4, 5]
a.remove(2)
a.remove(4)
print(a)
