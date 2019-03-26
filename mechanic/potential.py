from env.frame import Frame
class Potential(Frame):
    def __init__(self,potential = 0):
        self.__potential = potential

    def set_(self,potential = 0):
        self.__potential = potential
        
    def get_(self):
        return self.__potential