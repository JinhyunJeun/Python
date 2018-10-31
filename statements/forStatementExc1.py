
"""
별 찍기 1.
*
**
***
****
*****
"""
print("별 찍기1")
for a in range(6):
    for b in range(a):
        print("*", end='')
    print()
"""
별 찍기 2.
*****
****
***
**
*
"""
print("별 찍기2")
for a in range(6,0,-1):
    for b in range(a):
        print("*",end='')
    print()
"""
별 찍기 3.
*****
*****
*****
*****
*****
"""
print("별 찍기3")
for a in range(6):
    for b in range(6):
        print("*",end='')
    print()
"""
별 찍기 4.
*
 *
  *
   *
    *
"""
print("별 찍기4")
"""
print(chr(32)*0+"*")
print(chr(32)*1+"*")
print(chr(32)*2+"*")
print(chr(32)*3+"*")
print(chr(32)*4+"*")
"""
for a in range(6):
    print(chr(32)*a+"*")
print("별 찍기5")
"""
별 찍기 5.
     *
    ***
   *****
  *******
 *********
***********
print(chr(32)*5+"*"*1)
print(chr(32)*4+"*"*3)
print(chr(32)*3+"*"*5)
print(chr(32)*2+"*"*7)
print(chr(32)*1+"*"*9)
print(chr(32)*0+"*"*11)
"""
for x in range(1,6*2,2):
    print((" "*((6*2-1-x)//2))+("*"*x))