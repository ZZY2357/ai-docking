import pyglet
import random
from Vector import *
from config import *

def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner

@singleton
class Dock:
    def __init__(self):
        self.p = Vector(DOCK_X, random.randint(0, HEIGHT))

    def random_y(self):
        self.p.y = random.randint(0, HEIGHT)

    def update(self, dt):
        pass

    def draw(self):
        pyglet.shapes.Circle(
            self.p.x, self.p.y, DOCK_RADIUS, color=(255, 0, 0)
        ).draw()
