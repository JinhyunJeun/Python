# 문자열 인덱싱:  
# a = "Life is too short, You need Python"이라는 문자가 있을 때
#      0123456789... 이렇게 나가는 것을 말한다.
# 따라서 a[0]='L'이 된다.
a = "Life is too short, You need Python"
print(a[0:4])   # Life 출력


# 문자열 formating
# 숫자 바로 대입
string = "I eat %d apples" % 3
print(string)
# 문자 바로 대입
string = "I eat %s apples" % "five"
print(string)
# 숫자 값을 나타내는 변수로 대입
num = 3
string = "I eat %d apples" % num값
print(string)
# 2개 이상의 값 넣기
num = 10
day = "three"
string = "I ate %d apples. So I was sick for %s days" % (num, day)
print(string)
# 문자열 format code
# %s = String
# %c = Character
# %d = Integer
# %f = floating-point
# %o = 8진수
# %x = 16진수
# %% = Literal % (%자체)
string = "error is %d %%" % 98
print(string)


# 포멧코드와 숫자 함께 사용하기
# 1) 정렬과 공백
string = "%10s" % "hi" # 10칸 안에서 문자열 hi를 오른쪽 정렬하라는 의미
print(string)
string = "%-10s" % "hi" # 10칸 안에서 문자열 hi를 왼쪽 정렬하라는 의미
print(string)
string = "%-10sjane" % "hi" # 10 칸 안에서 hi는 왼쪽 정렬되고 11번째에 jane이 들어가게됨
print(string)
# 2) 소수점 표현하기
floooat = "%0.4f" % 3.42134234 # 소수점 넷째 자리까지 표현
print(floooat)
floooat = "%10.4f" % 3.42134234 # 10개짜리 공간에서 오른쪽 정렬하고 소수점 넷째 자리까지 표현
print(floooat)


# format 함수를 이용한 포매팅: 문자열의 format() 함수를 이용하면 좀 더 발전된 스타일로 문자열의 포맷을 지정할 수 있다.
# 1) 숫자 바로 대입하기
string = "I eat {0} apples.".format(3)
print(string)
# 2) 문자열 바로 대입하기
string = "I eat {0} apples.".format("three")
print(string)
# 3) 숫자 값을 가진 변수로 대입하기
num = 5
string = "I eat {0} apples".format(num)
print(string)
# 4) 두 개 이상의 값 넣기
num = 10
day = "two"
string = "I ate {0} apples. So I sick for {1} days.".format(num, day)
print(string)
# 5) 이름으로 넣기
string = "I ate {number} apples. So I was sick for {day} days".format(number=12, day="seven") # format 좀 신기한듯
print(string)
# 6) 인덱스와 이름을 혼용해서 넣기
string = "I ate {0} apples. So I was sick for {day} days".format(14, day = 7)
print(string)
# 7) 왼쪽 정렬
string = "{0:<10}".format("hi") # 총 자릿수 10개에서 왼쪽 정렬, 화살표가 가리키는 방향이 정렬 방향이 된다.
print(string)
# 8) 오른쪽 정렬
string = "{0:>10}".format("hi")
print(string)
# 9) 가운데 정렬
string = "{0:^10}".format("hi") # 가운데 정렬은 ^
print(string)
# 10) 공백 채우기
string = "{0:=^10}".format("hi")
print(string)
string ="{0:^^10}".format("ss")
print(string)
string = "{0:!^10}".format("hi")
print(string)
string = "{0:!<10}".format("hi")
print(string)
# 소수점 표현하기
y = 3.42134234
floooat = "{0:0.4f}".format(y)
print(floooat)
floooat = "{0:10.4f}".format(y) # 10칸에서 소수점 네 자리 + 오른쪽 정렬
print(floooat)
# { 또는 } 표현하기
string = "{{and}}".format()
print(string)

# f문자열 포매팅(python 3.6 이상부터 가능)
name = "홍길동"
age = 30
print(f"나의 이름은 {name} 입니다. 나이는 {age} 입니다.")
# f문자열 포메팅은 표현식을 지원하기 때문에 아래와 같은 것도 가능하다
age = 30
print(f"나는 내년이면 {age+1}살이 된다.")
# dictionary는 f문자열에서 다음과 같이 사용 가능
d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.') # 따옴표 잘 쓸 것. ""와''을 잘 사용할 것
# 정렬은 다음과 같이 할 수 있다. / 이건 연습이 좀 필요할듯
print(f'{"hi":<10}') 
print(f'{"hi":>10}')
print(f'{"hi":^10}')
print(f'{"hi":=^10}')
print(f'{"hi":!<10}')
# f 문자열에서 { 나 }를 사용하려면
print(f"{'{'}")
print(f"{'}'}")


# 문자열과 관련 함수들: 내장함수를 사용하려면 문자열 변수 이름 뒤에 .을 붙인 다음 함수 이름을 써주면 된다.
# 문자 갯수 세기(count)
a = "hobby"
print(a.count("b"))
# 위치 알려주기1: find
a = "Python is the best choice"
print(a.find("b")) # 찾는 문자가 없으면 -1을 리턴한다. JAVA의 indexOf와 같음.
# 위치 알려주기2: index
a = "Life is too Short"
print(a.index("i"))
# 문자열 삽입: join
a = ","
print(a.join('abcd'))
print(",".join("efgh")) # ,에 변수 지정 안하고 이렇게 많이 씀
print(",".join(['i','j','k','l'])) # join을 쓰면 출력이 list처럼 안나온다.
# 소문자를 대문자로 바꾸기: upper()
a = "hi!"
print(a.upper())
# 대문자를 소문자로 바꾸기: lower()
a = "HELLO PYTHON"
print(a.lower())
# 왼쪽 공백 지우기: lstrip()
a = " hi "
print(a.lstrip())
# 오른쪽 공백 지우기: rstrip()
print(a.rstrip())
# 양쪽 공백 지우기: strip()
print(a.strip())
# 문자열 바꾸기: replace()
a = "life is too short"
print(a.replace("life","your hair"))
# 문자열 나누기: split()
a = "Hello; world"
print(a.split(";"))
b = "Hello Python"
print(b.split())
# 연습문제
# 문제3. "PYTHON" 앞에 공백 24개 추가 하여 30자리 문자열 만들기
print(' '*24 + "PYTHON")
# 문제4. 문자열 나누기: 881120-1068234를 YYYYMMDD로 출력하기
string = "881120-106823"
sangYun = string.split("-")
sangYunWolIl = sangYun[0].replace("88","1988")
print(sangYunWolIl)
# 문제5. 문자열 인덱싱: 881120-1068234에서 성별을 나타내는 1을 출력
print(sangYun[1][0])
# 문제6. 1980M1120 이라는 문자열이 있을 때 M19801120으로 바꾸시오.
string = "1980M1120"
splited = string.split("M")
print("M"+splited[0]+splited[1])
# 문제7. 문자열 포맷: "PYTHON" 앞에 24개의 공백을 추가하여 30자리 문자열 만들기
print(" "*24+f'{"PYTHON":30}')
# 문제8. 문자열 찾기: "Life is too short, you need python"
#       에서 "short"라는 문자열이 시작되는 인덱스를 구하시오.
string = "Life is too short, you need python"
print(string.find("short"))
# 문제9. 문자열 바꾸기1 a:b:c:d 문자열에서 replace를 이용 a#b#c#d로 바꾸기
string = "a:b:c:d"
print(string.replace(":","#"))