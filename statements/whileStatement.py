# 반복해서 문장을 수행해야 할 경우 while 문을 사용한다.
# while <조건문>:
#    <수행할 문장1>
#    <수행할 문장2>
#    <수행할 문장3>
#    <수행할 문장4>
#    ...
# while문이 참일 경우 반복해서 수행한다.
treeHit = 0
while treeHit<10:
    treeHit = treeHit+1
    print("나무를 %d번 찍습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")
