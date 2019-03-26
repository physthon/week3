from env.frame import Frame

class Speed(Frame):
    def __init__(self,speed = 0):
        super().__init__()
        self.__speed = speed

    def set_fr_coor(self,coor):
        return

    def set_(self,speed):
        if(type(speed) != 'str'):
            self.__speed = speed
        else:
            return self.ERROR()

    def get_(self):
        return self.__speed