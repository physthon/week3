from mechanic.potential import Potential

class HarmonicOscillation(Potential):
    def __init__(self,potential = 0):
        super().__init__(potential = potential)
        self.__potential = potential

    def get_(self):
        return self.__potential