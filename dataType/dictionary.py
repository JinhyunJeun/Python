# 딕셔너리란: "이름"="홍길동","생일"="몇 월 몇 일"처럼 나타내는 대응관계
# key:value, key:value 로 나타내는 것. 이것은 json인가..?
# 순차적 검색이 아닌 해당 key에 들어있는 value를 검색하는 것
dic = {'name':'pey', 'phone':'01012341234', 'birth':'0718'}
print(dic['name']) # 이렇게 사용한다.

# 딕셔너리 쌍 추가, 삭제하기
# 1.딕셔너리 쌍 추가하기
a = {1:'a'}
a[2] = 'b'
print(a) # a 다 불러오기
a['name'] = 'pey'
print(a)
a[3] = [1, 2, 3]
print(a)
del a[3][0] 
print(a)

# 딕셔너리 관련 함수들
# key 리스트 만들기(keys)
a = {'name':'pey', 'phone':'01012341234', 'birth':'0718'}
print(a.keys())
for i in a.keys():
    print(i)
print(list(a.keys())) # dict_keys 객체를 리스트로 만들기
# value 리스트 만들기(values)
print(a.values())
# key, value 쌍 얻기(items)
print(a.items())
# key:value 쌍 모두 지우기(clear)
print(a.clear())
# key로 value 얻기
a = {'name':'pey', 'phone':'01012341234', 'birth':'0718'}
print(a.get('name'))
if 'name' in a:
    print(a.get('name'))
print('name' in a)

# 연습문제
# 문제1. 다음 중 안되는 것과 그 이유를 말하시오.
a['name'] = 'python'
a[('a',)] = 'python'
# a[[1]] = 'python' 딕셔너리 안에 리스트가 들어가서 안된다. 왜냐하면 리스트는 변하는 갑ㅅ이기 때문
# 문제2. a에서 B값을 추출하고 삭제하시오
a = {'A':90, 'B':80, 'c':70}
del a['B']
print(a)
# 문제3. 딕셔너리 최소값값 구하기.
a = {'A':90, 'B':80, 'c':70}
print(min(a.values()))
# 문제4. 딕셔너리를 리스트로 변환
print(a.items())
print(list(a.items())) # items함수를 이용해 key와 value 쌍을 튜플로 묶은 dict_items 객체로 리턴하고 list함수를 이용해서 리스트로 만든다.