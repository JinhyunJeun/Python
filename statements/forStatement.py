# 파이썬의 직관적인 특징을 가장 잘 나타내 주는 것이 반복문이다.
# for문의 구조: for 변수 in 리스트(또는 튜플, 문자열):
#                수행할 문장1
#                수행할 문장2
#                수행할 문장3
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)
# one, two, three 라는 리스트는 one이 먼저 i에 대입된 후 print(i)라는 문장을 수행한다.
# 다음 two라는 두 번째 요소가 i 변수에 대입된 후 print(i) 문장을 수행하고 리스트의 마지막 요소까지 이것ㅇ르 반복한다.
a = [(1,2), (3,4), (5,6)]
for (first,last) in a:
    print(first+last)
marks = [90, 25, 67, 45, 80]
num = 0
for mark in marks:
    num = num+1
    if mark>=60:
        print("%d번 학생은 합격입니다." % num)
    else:
        print("%d번 학생은 불합격입니다." % num)
# range 함수: 숫자 리스트를 자동으로 만들어준다.
a = range(10)
print(a)
sum = 0
for i in range(1,11): # 마지막 숫자는 포함되지 않는다(10까지 포함됨)
    sum = sum + i
print(sum)

for num in range(len(marks)):
    if marks[num]<60: continue
    print("%d번 학생은 합격입니다."% (num+1))
"""
구구단프로그램입니다.
원하는 단을 입력해주세요
2x1=2
2x2=4 출력
"""
print("구구단 프로그램입니다. 원하는 단을 입력해주세요")
dan = int(input())
i = 0
if dan in range(1,10):
    for i in range(1,10):
        result = dan*i
        # print(str(dan)+"x"+str(i)+"="+str(result))
        print(str(dan)+"x%d="%i+str(result)) # % 순서 눈여겨 볼 것. %i가 뒤에 오면 안된다.
        # 이걸 str로 바꾸는 이유는 int에 str을 더할 수 없기 때문인듯
        
else:
    print("2~9단까지만 입력해주세요.")
"""
1~20 사이에 3의 배수의 갯수를 구하시오
"""
cnt = 0
for i in range(1,21):
    if i%3==0:
        cnt = cnt+1
print(cnt)
# 리스트 안에 for문 포함하기
# 리스트 안에 for문을 포함하는 리스트 내포(list comprehension)을 이용하면 좀 더 편리하고 직관적인 프로그램을 만들 수 있다.
b = [1,2,3,4]
result = []
for no in b:
    result.append(no*3)
print(result)
# 2의 배수에만 3곱해서 출력
c = [1,2,3,4]
resultt = [noo*3 for noo in c if noo%2==0]
print(resultt)
# 리스트 내포의 일반적인 문법은 다음과 같다. "if조건"부분은 생략할 수 있다.
# [표현식 for 항목 in 반복가능객체 if 조건]
"""
for문을 두 개 이상 사용하는 것도 가능하다. for문을 여러 개 사용할 때의 문법은 다음과 같다.
[표현식 for 항목1 in 반복가능객체1 if 조건1
       for 항목2 in 반복가능객체2 if 조건2
       ...
       for 항목 n 반복가능객체n if 조건n]
"""
# 다시 구구단으로 돌아와서
result = [x*y for x in range(2,10)
              for y in range(1,10)]
print(result)


# 서기 1년부터 2018년까지 윤년의 갯수
cnt = 0
for year in range(1,2019):
     if year%4==0 and year%100!=0 or year%400==0:
        cnt = cnt + 1
print(cnt)
# 두 수 사이의 합을 구하시오
print("더하기 프로그램입니다. 숫자 두 개를 넣으세요.")
x = int(input("첫 번째 숫자를 입력하세요: "))
y = int(input("두 번째 숫자를 입력하세요: "))
print(x+y)