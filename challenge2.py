#complete student class
class Student:
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def setRollNumber(self, RollNumber):
        self.__RollNumber = RollNumber
    def getRollNumber(self):
        return self.__RollNumber
std1 = Student()
std1.setName("Eddy")
print(std1.getName())
std1.setRollNumber(12233)
print(std1.getRollNumber())
