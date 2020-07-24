class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    def animal_details(self):
        print("Name:", self.name) 
        print("Sound:", self.sound)


class Dog(Animal):
    def __init__(self,name,sound,family):
        self.family = family
        #initializer using the super() class
        super().__init__(name,sound)

    def animal_details(self):
        super().animal_details() 
        print("Family:", self.family)


class Sheep(Animal):
    def __init__(self,name,sound,color):
        self.color = color
        super().__init__(name,sound)


    def animal_details(self):
        super().animal_details()  
        print("Color:", self.color)

d = Dog("Pongo", "Woof Woof", "Husky")
d.animal_details()
print(" ")
s = Sheep("Billy", "Baaa Baaa", "White")
s.animal_details()