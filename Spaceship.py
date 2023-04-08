import pyglet
from Brain import *
from Dock import *
from KinematicBody import *
from Vector import *
from config import *
import math

def new_initalized_spaceship():
    return Spaceship(40, HEIGHT / 2, 1)

class Spaceship(KinematicBody):
    def __init__(self, x, y, m):
        super().__init__(x, y, m)
        self.__throttle = 0 # -1 ~ 1
        self.__roll = 0 # -1 ~ 1

        self.fuel_uesd = 0

        self.brain = Brain(
            7, # x, y, vx, vy, r, vr, dock_y
            20,
            2 # throttle, roll
        )

    @property
    def throttle(self):
        return self.__throttle

    @throttle.setter
    def throttle(self, v):
        if v != 0:
            self.__throttle = v / abs(v)
        else:
            self.__throttle = 0

    @property
    def roll(self):
        return self.__roll

    @roll.setter
    def roll(self, v):
        if v != 0:
            self.__roll = v / abs(v)
        else:
            self.__roll = 0

    def detect_collision(self, dock_pos):
        return self.get_dock_pos().distance_to(dock_pos) < DOCK_RADIUS * 2

    def think(self):
        output = self.brain.predict(np.array([
            self.p.x,
            self.p.y,
            self.v.x,
            self.v.y,
            self.r,
            self.vr,
            Dock().p.y
        ]).T)
        self.throttle = output[0][0]
        self.roll = output[1][0]

    def get_dock_pos(self):
        return Vector(
            self.p.x - math.cos(math.radians(self.r)) * SPACESHIP_WIDTH / 2,
            self.p.y - math.sin(math.radians(self.r)) * SPACESHIP_WIDTH / 2
        )

    def move(self):
        self.apply_force(
            Vector(
                math.cos(math.radians(self.r)),
                math.sin(math.radians(self.r))
            ).mult(THROTTLE_FORCE * self.throttle)
        )

        self.apply_rotation(ROLL_FORCE * self.roll)

        self.fuel_uesd += abs(self.throttle) * 0.1 + abs(self.roll) * 0.4

    def fitness(self):
        dock = Dock()
        return \
            80000 - self.fuel_uesd * 1 \
            - self.get_dock_pos().distance_to(Vector(dock.p.x, dock.p.y)) * 30

    def update(self, dt):
        super().update(dt)
        self.think()
        self.move()
        self.v.limit(MAX_SPEED)
        if abs(self.vr) > MAX_ROLL:
            self.vr = self.vr / abs(self.vr) * MAX_ROLL

    def draw(self):
        body = pyglet.shapes.Rectangle(
            self.p.x, self.p.y,
            SPACESHIP_WIDTH, SPACESHIP_HEIGHT,
            (255, 0, 0)
        )
        body.anchor_position = (SPACESHIP_WIDTH / 2, SPACESHIP_HEIGHT / 2)
        body.rotation = -self.r
        body.draw()

        dock = pyglet.shapes.Circle(
            self.get_dock_pos().x,
            self.get_dock_pos().y,
            DOCK_RADIUS,
            color=(0, 255, 0)
        )
        dock.draw()

        return super().draw()
