import pyglet
from Dock import *
from GA import *
from Spaceship import *
from config import *
import os

window = pyglet.window.Window(WIDTH, HEIGHT)

dock = Dock()

ga = GA()
ga.init_population()
if os.path.exists('best.npz'):
    to_load = 'best.npz'
else:
    to_load = 'init_best.npz'
wih = np.load(to_load)['arr_0']
who = np.load(to_load)['arr_1']
ga.brain_fill(wih, who)

def update(dt):
    ga.update(dt)

@window.event
def on_draw():
    window.clear()
    ga.draw()
    dock.draw()

pyglet.clock.schedule_interval(update, 1 / 30)
pyglet.clock.schedule_interval(ga.next_turn, GA_ROUND_TIME)

pyglet.app.run()
