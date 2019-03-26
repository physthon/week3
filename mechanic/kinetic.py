from mechanic.mass import Mass
from mechanic.speed import Speed
from env.frame import Frame
class Kinetic(Frame):
    def __init__(self,m = Mass(), v = Speed()):
        super().__init__()
        self.__kinetic = float(1/2 * m.get_() * v.get_()**2)

    def set_(self,m = Mass(), v = Speed()):
        self.__kinetic = float(1/2 * m.get_() * v.get_()**2)

    def get_(self):
        return self.__kinetic