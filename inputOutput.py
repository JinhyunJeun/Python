# 사용자의 입력을 받는 방법과 출력하는 방법을 알아보자
# 사용자 입력
"""
사용자가 입력한 값을 어떤 변수에 대입하고 싶을 때
input 사용
a = input()
input은 입력되는 모든 것을 문자열로 취급한다.
"""
# print 자세히 알기
"""
큰 따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다
"""
print("life" "is" "too short")
print("life"+"is"+"too short") # 두 개의 결과는 같다.
"""
문자열 띄어쓰기는 콤마로 한다
"""
print("life","is","too short")
"""
한 줄에 결과값 출력하기
"""
for i in range(5):
    print(i,end='')