# 집합자료형
s1 = set([1,2,3])
print(s1)
s2 = set("HelloPython")
print(s2) # 중복을 허용하지 않고 순서가 없다는 특징이 있다, "순서가 없다" == "인덱싱을 지원하지 않는다"
# 따라서 자료중복을 제거하기 위한 필터로 사용된다.
# 만약 set에 저장된 값을 인덱싱으로 접근하려면 리스트나 튜플로 변환한 후 해야 한다.
li = list(s1)
print(li)
print(li[0])


# 집합 자료형 활용하는 방법
# 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1&s2) # 교집합 혹은 print(s1.intersection(s2))
print(s1|s2) # 합집합 혹은 print(s1.union(s2))
print(s1 - s2) # 차집합 print(s1.difference(s2))
               #      print(s2.difference(s1))


# 집합 자료형 관련 함수들
# 값 1개 추가하기(add): 이미 만들어진 set 자료형에 값을 추가할 수 있다. 1개의 값만 추가할 경우
s1 = set([1, 2, 3])
s1.add(4)
print(s1)
# 값 여러 개 추가하기(update): 여러 개의 값을 한번에 추가할 때는
s1.update([4,5,6])
print(s1)
# 특정 값 제거하기(remove): 특정 값ㅇ르 제거하고 싶을 때는
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)

# 연습문제
# 문제1. 집합 만들기1: ['a','b','c'] 라는 리스트를 집합 자료형으로 만드시오
li2 = ['a', 'b', 'c']
se1 = set(li2)
print(se1)
# 문제2. 집합의 중복: 중복을 허용하지 않는 집합 자료형의 특징을 이용하여 다음 a 리스트에서 중복된 숫자들을 제거해보자
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
s2 = set(a)
a2 = list(s2)
print(a2)
# 문제3. 차집합: s1 집합의 항목 중 s2 집합에 포함된 항목을 제거 해 보자
s1 = set(['a', 'b', 'c', 'd', 'e'])
s2 = set(['c', 'd', 'e', 'f', 'g'])
print(s1 - s2)
# 문제4. 집합 만들기2: 비어있는 집합 자료형을 만들어보자
a = {''}
print(type(a))
# 문제5. 집합 추가 a에 {'d','e','f'}를 추가하시오
a = {'a', 'b', 'c'}
a.update('d','e','f')
print(a)