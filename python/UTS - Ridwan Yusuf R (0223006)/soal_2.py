
from configparser import LegacyInterpolation


class animal(object):
    def leg (self):
        pass

    def eat(self, food):
        self.food = food
        print(f'Memakan: {self.food}')
    
    def walk(self):
        print(f'berjalan menggunakan : {self.walk}')

class Pet:
    def __init__(self, name):
        self.name = name
        
    def play(self):
        print(f'bermain {self.play}')
        
class Spider(animal):
    def leg(self):
        print('8 kaki')
    
class Fish(animal, Pet):
    def __init__(self, leg, name):
        super().__init__(leg)
        self.name = name
        print("tidak berjalan tetapi berenang")

class Cat(animal, Pet):
    def leg(self):
        return super().leg()
    
    def name(self):
        return super().name()

    def play(self):
        pass

    def eat(self):
        pass
    
class TestAnimal:
    def main(self):
        f = Fish()
        c = Cat("Fluffy")
        a = Fish()
        e = Spider()
                
        f.play()
        c.play()
        e.eat()
        e.walk()
        a.walk()
