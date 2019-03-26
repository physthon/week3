from env.frame import Frame

class Mass(Frame):
    def __init__(self,mass = 0):
        super().__init__()
        self.__mass = mass

    def set_(self,mass):
        if(type(mass) != 'str'):
            self.__mass = mass
        else:
            return self.ERROR()

    def get_(self):
        return self.__mass