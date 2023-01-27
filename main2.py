class Living_Being:
 
    def __init__(self,x):
        self.x = x
    def breathing(self):
        print("inside breathing method --- (Living_Being class)--")

class Plant(Living_Being):
    def __init__(self):
        super().__init__()

class Human(Living_Being):
    def __init__(self):
        super().__init__()
    def walk(self):
        print("--- inside walk method --- Human Being class----")

class Animal(Living_Being):
    def __init__(self, x):
        super().__init__(x)
        
    def walk(self):
        print("---- inside walk method --- Animal Class ----")

animal = Animal("--")
