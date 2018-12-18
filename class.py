# 클래스가 필요한 이유
"""
붕어빵틀 -> 클래스(class)
붕어빵틀에 의해 만들어진 붕어빵 -> 객체(object)
- 클래스란 똑같은 무엇인가를 계속해서 만들어낼 수 있는 설계 도면 같은 것.
- 객체는 클래스에 의해 만들어진 피조물을 뜻한다.
클래스에 의해 만들어진 객체는 독립적인 성격을 갖는다. 그래서 동일한 클래스에 의해 생성된 객체들은 서로에게 영향을 주지 않는다.
"""
# 객체와 인스턴스의 차이
"""
클래스에 의해 만들어진 객체를 인스턴스라고도 한다.
a = Cookie()에서 a는 객체이다. 또한 a라는 객체는 Cookie의 인스턴스이다.
즉, 인스턴스라는 말은 객체가 어떤 클래스의 객체인지를 설명할 때 사용한다.
"""
# 간단한 사칙연산 클래스
class FourCal:
    def setData(self, a, b):
        self.a = a
        self.b = b
    def sum(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
c = FourCal()
d = FourCal()
print(type(c))

'''print(c.sum(2,3))
print(c.mul(3,2))'''

"""
인스턴스를 호출하지 않고 클래스명.메서드로 사용하는 경우
a = FourCal()
FourCal.sum(a, 3, 4) 이런 식으로 사용한다.
"""

'''c.sum(2,3)
print(c.a)
print(c.b)'''
c.setData(2,3)
d.setData(3,4)
print(d.sum())
print(d.sub())
print(d.div())

# 생성자(Constructor)
'''
위의 예제에서 setData 메소드가 없다면 나머지 메소드들은 사용할 수 없다. 이렇게 초기값을 지정해줘야 하는 경우 생성자를 이용한다.
파이썬 메소드명으로 '__init__'을 사용하면 이 메소드는 생성자가 된다.
'''

class calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def plus(self):
        result = self.first+self.second
        return result
    def minus(self):
        result =  self.first-self.second
        return result
    def divide(self):
        result =  self.first/self.second
        return result
    def multiply(self):
        result = self.first*self.second
        return result
a = calculator(4, 2)
print("a.first=%d" % a.first)
print("a.second=%d" % a.second)
print("a.plus(4+2)=%d" % a.plus())
print("a.minus(4-2)=%d" % a.minus())

# 클래스의 상속
"""
상속(inheritance)이란 "물려받다"라는 뜻이다. 클래스에서는 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것이다.
상속을 이용하여 a^b의 기능을 만들어보자.
클래스를 상속하기 위해서는 클래스 변수 자리에 상속할 클래스명을 입력하면 된다.
"""
class exponential(calculator):
    def pow(self):
        result = self.first ** self.second
        return result
b = exponential(4,2)
print("plus상속: %d" %b.plus())
print("divide상속: %d" %b.divide())
print("pow함수: %d" %b.pow())

# 메소드 오버라이딩
class safeCalculator(calculator):
    def divide(self):
        if self.second == 0:
            return "null"
        else:
            return self.first/self.second
c = safeCalculator(4, 0)
print("메소드오버라이드: %s" % c.divide())
