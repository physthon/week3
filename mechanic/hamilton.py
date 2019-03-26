from mechanic.mechanic import Mechanic
from mechanic.kinetic import Kinetic
from mechanic.potential import Potential

class Hamilton():
    def __init__(self,K = Kinetic(), U = Potential()):
        self.__hamiltonian = K.get_() + U.get_()

    def get_(self):
        return self.__hamiltonian