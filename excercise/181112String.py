# Exc001 난수 0과 1만 랜덤하게 나오기
from random import *
i = randint(1,101)
print(i)
# Exc002 난수 1~45만 랜덤하게 나오기(로또 6개)
for j in range(6):
    j = randint(1,46)
    print(j)
# Exc003 Happy Birthday
#   1. 글자 갯수
#   2. 0번째 글자
#   3. B 찾기
#   4. C 찾기
#   5. 전부 소문자로 출력
#   6. 전부 대문자로 출력
#   7. 4번째 글자에서 마지막까지 출력
#   8. 4번째에서 7번째 글자까지 출력
str = "Happy Birthday"
print("글자 갯수: %d" % (len(str)-1))
print("0번째 글자: "+str[0])
print("B찾기: %d" % str.index("B"))
print("C찾기: %d" % str.find("C"))
print("전부소문자출력: %s" % str.lower())
print("전부대문자출력: %s" % str.upper())
print("4번째부터 마지막까지 출력: ")
for i in range(4,14):
    print(str[i], end='')
print()
print("4번째에서 7번째 글자까지 출력: ")
for i in range(4,8):
    print(str[i],end='')
print()
# Exc004 주민번호를 이용해 나이와 성별 출력하기 jumin = "0012303234567"
jumin = "00123032234567"

if jumin[6]=="3":
    print("성별: 남자")
elif jumin[6]=="4":
    print("성별: 여자")
else:
    print("뭔가 잘못됨")
print("나이: %d"% (18-int(jumin[0:1])+1))
# Exc005 이메일에 @이 있으면 분리해서 출력 "admin@email.com"
email = "admin@email.com"
if "@" in email:
    print(email.split("@"))
# Exc006 h를 찾아 H로 변경 mess = "hello Hi HaHa"
mess = "hello Hi HaHa"
"""if 'h' in mess:
    i = mess.index('h')
    mess[i].upper()
    print(mess)
    모루겠다
"""
# Exc007 문자열의 맨 앞, 맨 뒤 공백 제거 mess = "    S K Y    "
mess = "    S K Y    "
print(mess.strip())
# Exc008 num_rank = [10, -20, 3, -40, 5]
#   1. 음수의 갯수 구하기
#   2. 양수 중에서 홀수의 합
#   3. num_rank[4] 요소의 등수
#   4. 최대값, 최소값 구하기
num_rank = [10, -20, 3, -40, 5]
cnt = 0
for i in range(len(num_rank)):
    if num_rank[i] < 0:
        cnt=cnt+1
print("1.음수의 갯수 구하기: %d" % cnt)
hol = 0
for i in range(len(num_rank)):
    if num_rank[i] >=0 and num_rank[i]%2!=0:
        hol += num_rank[i]
print("2.양수 중에서 홀수의 합: %d" % hol)
a = num_rank[4]
num_rank.sort()
print("3.num_rank[4] 요소의 등수: %d" % (num_rank.index(a)-1))
print("4.최대값: %d, 최소값: %d 구하기" % (max(num_rank),min(num_rank)))
# Exc009 name = ["아이언맨","헐크","캡틴","토르","호크아이"]
#        kor = [100, 20, 90, 70, 35]
#        eng = [100, 50, 95, 80, 100]
#        mat = [100, 30, 90, 60, 100]
#   1. 평균 구하기
#   2. 등수 구하기
#   3. 합격, 재시험, 불합격
#      평균이 60점 이상이면 합격
#      합격에서도 국영수 중 한 과목이라도 40점 미만이면 재시험. 아니면 불합격
#      평균 95점 이상이면 장학생
#      평균 10점당 * 한 개씩
name = ["아이언맨","헐크","캡틴","토르","호크아이"]
kor = [100,20,90,70,35]
eng = [100,50,95,80,100]
mat = [100,30,90,60,100]
print("\t\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % ("국어","영어","수학","평균","결과","재시험여부","장학생 여부"))
for i in range(len(kor)):
    avg = (kor[i]+eng[i]+mat[i])/3
    if avg >= 60:
        hap = "합격"
        if kor[i]>=40 and eng[i]>=40 and mat[i]>=40:
            tong = "통과"
        else:
            tong = "재시험"
    else:
        hap = "불합격"
    print("%s\t\t%d\t%d\t%d\t%0.1f\t%s\t%s" % (name[i],kor[i],eng[i],mat[i],avg,hap,tong))
# Exc010 계산기
#   1. 숫자 입력받기:
#      -10000 ~ 10000 사이에서만 입력 가능하게
#      - 잘못 입력 받으면 다시 입력받기
#   2. 숫자 입력받기
#      -10000 ~ 10000 사이에서만 입력 가능하게
#      - 잘못 입력 받으면 다시 입력받기
#   3. 연산자 입력받기
#      - +,-,*,/ 만 입력가능하게
#      - 잘못 입력 받으면 다시 입력받기
#   4. 각각의 계산기능 출력
#   5. 계산이 끝났으면 다시하겠습니까?(y/n) 출력
a = 0
b = 0
c = 0
def inputData(a,b,c):
    while True:
        a = int(input("첫 번째 숫자를 입력하세요: "))
        b = int(input("두 번째 숫자를 입력하세요: "))
        c = input("연산자를 입력하세요: ")
        if c != '+':
            print("잘못 입력하셨습니다.")
        else:
            break
    result = 0
    if c == '+':
        result = a+b
    if c == '-':
        result = a-b
    if c == '*':
        result = a*b
    if c == '/':
        result = a/b
    print(result)
inputData(a,b,c)