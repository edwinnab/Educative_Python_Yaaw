#implement a rectangle class using encapsulation
class Rectangle:
    #make properties private
    def __init__(self,length,width):
        self.__length = length
        self.__width = width
    def area(self):
        return self.__length * self.__width
    def perimeter(self):
        return (self.__width + self.__length)*2
values = Rectangle(4,5)
print(values.area())
print(values.perimeter())