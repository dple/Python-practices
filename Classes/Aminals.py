class Animal:
    def __init__(self, name='', legs=0, colour=''):
        self.name = name
        self.legs = legs
        self.colour = colour

    def speak(self):
        pass

class Dog(Animal):

    def speak(self):
        print(self.name, "barks")

if __name__ == '__main__':
    dog = Dog("Collin", 4, "black")
    dog.speak()


