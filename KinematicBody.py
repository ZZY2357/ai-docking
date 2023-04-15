from Vector import *

class KinematicBody:
    def __init__(self, x, y, m):
        self.p = Vector(x, y)
        self.v = Vector()
        self.a = Vector()

        self.__r = 0
        self.vr = 0
        self.ar = 0

        self.m = m

    @property
    def r(self):
        return self.__r
    
    @r.setter
    def r(self, v):
        self.__r = v - v // 360

    def apply_force(self, f: Vector):
        self.a.add(f.copy().div(self.m))

    def apply_rotation(self, r):
        self.ar += r / self.m

    def update(self, dt):
        self.v.add(self.a)
        self.p.add(self.v.copy().mult(dt))
        self.a.mult(0)

        self.vr += self.ar
        self.r += self.vr
        self.ar = 0

        self.apply_force(self.v.copy().mult(-0.01))
        self.apply_rotation(self.vr * -0.3)

    def draw(self):
        pass