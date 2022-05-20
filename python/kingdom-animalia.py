class Animal(object):
    
    def __init__(self, name):
        self.name = name

#turunan class animal 
class Vertebrates(Animal):
    pass

class Invertebrates(Animal):
    pass

#turunan class verteberates
class WarmBlooded(Vertebrates):
    pass

class ColdBlooded(Vertebrates):
    pass

#turunan class warmblood
class Mamalia(WarmBlooded):
    def __init__(self, name):
        super().__init__(name)

class Bird(WarmBlooded):
    def __init__(self, name):
        super().__init__(name)
    
#turunan class coldblood
class Fish(ColdBlooded):
    def __init__(self, name):
        super().__init__(name)

class Reptiles(ColdBlooded):
    def __init__(self, name):
        super().__init__(name)

class Amphibians(ColdBlooded):
    def __init__(self, name):
        super().__init__(name)

#turunan class invertebrates
class WithJoinedLegs(Invertebrates):
    pass

class WithoutLegs(Invertebrates):
    pass

#turunan class with joined legs
class With3PairsOfLegs(WithJoinedLegs):
    def __init__(self, name):
        super().__init__(name)

class WithMoreThan3PairsOfLegs(WithJoinedLegs):
    def __init__(self, name):
        super().__init__(name)

#turunan class without legs
class WormLike(WithoutLegs):
    def __init__(self, name):
        super().__init__(name)

class NotWormLike(WithoutLegs):
    def __init__(self, name):
        super().__init__(name)