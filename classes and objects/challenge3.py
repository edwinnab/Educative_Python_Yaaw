#Calculator class
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    #addition method
    def addition(self):
        return self.num1 + self.num2
    #subtraction
    def subtraction(self):
        return self.num2 - self.num1
    #multiplication
    def multiplication(self):
        return self.num1 * self.num2
    #division
    def division(self):
        return self.num2 / self.num1
#initialize object
numbers = Calculator(94,10)
print(numbers.addition())
print(numbers.subtraction())
print(numbers.multiplication())
print(numbers.division())
