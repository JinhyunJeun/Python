# if 조건문:
#   수행할 문장1
#   수행할 문장2
#   ...
# else:
#   수행할 문장1
#   수행할 문장2
#   ...

# 파이썬 들여쓰기(indentation): 파이썬에서 들여쓰기는 중요하다. 조건문에서 같은 블럭에 속하려면 depth를 유지해야한다.


# and, or, not
money = 2000
card = 1
if money >= 3000 or card:
    print("택시타라")
else:
    print("BusMetroWalk")

# x in s, x not in s
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])
print('a' in ('a', 'b', 'c'))
print('j' not in 'python')

# 조건문에서 아무 일도 하지 않게 설정하고 싶다면? pass
pocket = ['paper', 'cellphone', 'wallet']
if 'money' in pocket:
    pass
else:
    print("카드로 결제하라")
# if문을 한 줄로 작성하기
if 'money' in pocket: pass
else: print("카드를 꺼내라")

# 연습문제
# 문제1.
money = 5000
card = False
if money>=4000:
    print("홍길동씨는 택시타고 집에 갈 수 있음")
else:
    print("집에 못ㅋ감ㅋ")
# 문제2.
lucky_list = [1, 9, 23, 46]
if 23 in lucky_list:
    print("야호")
# 문제3.
"""
0)이름 담을 자료형 선택해 name이라 변수명 정하고 입력받기
1)국어 점수 담을 자료형 선택해 kor라 변수명 정하고 입력받기
2)영어 점수 담을 자료형 선택해 eng라 변수명 정하고 입력받기
3)수학 점수 담을 자료형 선택해 math라 변수명 정하고 입력받기
4)총점 점수 담을 자료형 선택해 tot라 변수명 정하고 입력받기
5)평균 점수 담을 자료형 선택해 avg라 변수명 정하고 입력받기
6)모두 출력      - 평균은 소수점 처리되게 만들기
7)평균 95점 이상이면 장학생
8)국어점수 90점 이상이면 수, 80이상 우, 70이상 미, 60이상 양, 나머지 가
9)평균 70이상이면 "합격"
단, 세 과목 중에서 한 과목이라도 40미만이면 합격이 아니라"재시" 평균이 70미만이면 "fail"
어느 과목때문에 재시험인지, 영수 모두 수우미양가
"""

name = input("Name: ")
kor = int(input("국어 성적: "))
eng = int(input("영어 성적: "))
mat = int(input("수학 성적: "))
tot = int(kor+eng+mat)
avg = float(tot/3)
score = ["점수", kor, eng, mat, tot, avg]
sub = ["과목", "국어", "영어", "수학", "총점", "평균"]
i = 0
while i < len(sub):
    i = i+1
    print(sub[i-1]+"\t"+str(score[i-1])) # 왜 이렇게 만들었는지 모르겠는데 print 안에 int는 출력이 안된다. 무조건 str이어야 할 것.
if avg >= 95:
    print("장학생입니다")
if avg>=70 and kor>40 and eng>40 and mat>40:
    print("합격입니다.")
if avg>=70 and (kor<=40 or eng<=40 or mat<=40):
    print("과락입니다.")
if avg<70:
    print("불합격입니다.")