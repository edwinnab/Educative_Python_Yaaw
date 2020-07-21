#square numbers and return their sum
#initialize a constructor
class Point:
    def __init__(self,num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        #method for square of numbers and sum
    def sqSum(self):
        a = self.num1**2
        b = self.num2**2
        c = self.num3**2
        sum = a + b +c
        return sum
#initialize object
number = Point(3,4,5)
print(number.sqSum())