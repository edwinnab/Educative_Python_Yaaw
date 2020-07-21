#calculate students Performance
class Student:
    #initialize a constructor
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio
        #method for calculating totalobtained
    def totalobtained(self):
        return (self.phy + self.chem + self.bio)
        #method for calculating percentage
    def percentage(self):
        return((self.totalobtained()/300)*100)
#initialize an object
student_one = Student("Edwinna", 80,90,45)
print(student_one.totalobtained())
print(student_one.percentage())