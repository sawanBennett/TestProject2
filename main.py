
class System:
    def __init__(self, ram):
        self.ram = ram
        print("---- inside System ----")

class PC(System):

    def __init__(self, ram):
        super().__init__(ram)
        print("---- inside PC----")

class Laptop(System):

    def __init__(self):
        super().__init__()

class WorkStation(System):

    def __init__(self) -> None:
        super().__init__()



def main():

    c = PC(4)
    print(c.ram)

main()
