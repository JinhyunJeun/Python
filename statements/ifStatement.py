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