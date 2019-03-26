from mechanic.mass import Mass
from mechanic.speed import Speed
from env.frame import Frame
class Momentum(Frame):
    def __init__(self,mass = Mass(),speed = Speed()):
        super().__init__()
        self.__momentum = float(mass.get_() * speed.get_())

    def set_(self,mass = Mass(),speed = Speed()):
        self.__momentum = float(mass.get_() * speed.get_())

    def get_(self):
        return self.__momentum