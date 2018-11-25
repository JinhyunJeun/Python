"""
파일을 통한 입출력 방법에 대해 알아보자
"""
f = open("/home/jhjeun86/Documents/test.txt",'w',1,'utf-8') # 경로없이 파일명만 지정하면 해당 폴더(/home/jhjeun86/anaconda3/envs/virtualEnv)에 생성된다.
# f.close() # 파일객체 = open(파일이름,파일 열기 모드)
"""
파일열기모드
f: 읽기모드 - 파일을 읽기만 할 때 사용
w: 쓰기모드 - 파일에 내용을 쓸 때 사용
a: 추가모드 - 파일의 마지막에 새로운 내용을 쓸 때 사용

파일을 쓰기 모드로 열게 되면 해당 파일이 이미 존재하는 경우 원래 있던 내용이 모두 사라지고, 해당 파일이 존재하지 않으면 새로운 파일이 생성된다.
close() 함수의 경우 파일 객체를 닫아주는 역할을 한다. 프로그램을 종료할 때 파이썬 프로그램이 열려 있는 파일 객체를 자동으로 닫아주지만 
쓰기모드로 열었던 파일을 닫지 않고 다시 사용하려하면 오류를 발생시킨다.
"""

# 파일 쓰기 모드로 열어 출력값 적기
for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    print(data)
    f.write(data)
f.close()

# 프로그램의 외부에 저장된 파일을 읽는 여러가지 방법
"""
파이썬에는 외부 파일을 읽어 들여 프로그램에서 사용할 수 있는 여러 가지 방법이 있다.
"""
# readline()함수 이용하기
f2 = open("/home/jhjeun86/Documents/test.txt",'r')
line = f2.readline()
print(line) # 한 줄만 읽기
f2.close()

# 모든 라인을 읽어서 화면에 출력하고 싶다면
f2 = open("/home/jhjeun86/Documents/test.txt",'r')
while True:
    line = f2.readline()
    if not line: break # 더 이상 읽을 line이 없으면 멈춘다.
    print(line)
f2.close()

# readlines()함수 이용하기
f3 = open("/home/jhjeun86/Documents/test.txt",'r')
lines = f3.readlines() # readlines()함수는 파일의 모든 라인을 읽어서 각각의 줄을요소로 갖는 리스트로 리턴한다.
for line in lines:
    print(line)
f3.close()

# read()함수 이용하기
f4 = open("/home/jhjeun86/Documents/test.txt",'r')
data = f4.read() # read()는 파일의 내용 전체를 문자열로 리턴한다.
print(data)
f4.close()

# 파일에 새로운 내용 추가하기
"""
파일을 열 때 원래 있던 값을 유지하면서 새로운 값을 추가해야하는 경우 파일을 추가모드('a')로 열면 된다.
"""
f5 = open("/home/jhjeun86/Documents/test.txt",'a')
for i in range(11,20):
    data = "%d번째 줄입니다.\n" % i
    f5.write(data)
f5.close()

# with문과 함께 사용하기
"""
파일을 열면 항상 close()해주어야 한다. 이것을 자동으로 해주는 것이 with()이다.
"""
with open("/home/jhjeun86/Documents/test2.txt",'w') as f:
    f.write("Life is too short, you need python") # with문을 이용하면 with 블록을 벗어나는 순간 열린 파일 객체 f가 자동으로 close되어 편리하다.