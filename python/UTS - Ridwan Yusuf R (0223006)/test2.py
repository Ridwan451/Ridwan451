from ast import walk
class Animal(object):
    def __init__(self, leg, food):
        self.leg = leg
        self.food = food
    
    def eat(self):
        print(f'Hewan ini memakan {self.food}')
    
    def walk(self):
        print(f'Hewan ini berjalan dengan {self.leg} Kaki')
        
class Spider(Animal):
    def __init__(self, leg, food):
        super().__init__(leg, food) 
        
class Fish(Animal):
    def __init__(self, leg, food, name, playing):
        super().__init__(leg, food)
        self.names = name
        self.playing = playing
    
    def walk(self):
        print("Ikan tidak berjalan tetapi berenang")
        
    def play(self):
        print(f'{self.names} Bermain {self.playing}')
    
    def name(self):
        self.name
        
class Cat(Animal):
    def __init__(self, names, playing, leg, food):
        super().__init__(leg, food)
        self.name = names
        self.playing = playing
        
    def name(self):
        self.name
        
    def play(self):
        print(f'{self.name} Bermain {self.playing}')
        
class TestAnimal:
    def main():
        c = Cat('flully','ball', 4 ,'wiskas')     
        f = Fish(walk, 'Plangkton', 'Nemo','Anemon')
        a = Fish(walk, 'pelet','Kuya','bola')
        e = Spider(8,'Serangga')
                
        f.play()
        c.play()
        a.name()
        e.eat()
        e.walk()
        a.walk()
        c.eat()
        c.walk()

test = TestAnimal
test.main()