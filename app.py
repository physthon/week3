from modules.classical import Classical

# a = Classical(speed = 5,force = 10)
# print(a.get_speed())
# print(a.get_force())
# print(a.set_energy(None))
from mechanic.mass import Mass
from mechanic.speed import Speed
from mechanic.momentum import Momentum
from mechanic.kinetic import Kinetic
from mechanic.PPotential.harmonic_oscillation import HarmonicOscillation
from mechanic.hamilton import Hamilton

m = Mass(5)
v = Speed(10)

T = Kinetic(m,v)
U = HarmonicOscillation(10)# Lớp con có thể kế thừa chức năng truyền vào của lớp cha
H = Hamilton(T,U)
print(H.get_())