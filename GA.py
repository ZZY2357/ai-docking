from config import *
from Spaceship import *
import random

class GA:
    def __init__(self):
        self.population = []
        self.mating_pool = []

    def get_best(self):
        m = self.population[0]
        for i in range(1, len(self.population)):
            if self.population[i].fitness() > m.fitness():
                m = self.population[i]
        return m

    def init_population(self):
        for i in range(GA_POPULATION):
            self.population.append(new_initalized_spaceship())

    def cross(self):
        for i in self.population:
            for j in range(int((i.fitness() / self.get_best().fitness()) * 100)):
                self.mating_pool.append(i)

        self.population.clear()
        for i in range(GA_POPULATION):
            c = new_initalized_spaceship()
            c.brain = random.choice(self.mating_pool).brain.breed(
                random.choice(self.mating_pool).brain
            )
            if (random.random() < GA_MUTATING_RATE):
                c.brain.mutate()
            self.population.append(c)

        self.mating_pool.clear()

    def brain_fill(self, wih, who):
        for i in self.population:
            i.brain.wih = wih
            i.brain.who = who

    def next_turn(self, dt):
        best = self.get_best()
        print(best.fitness())
        np.savez('best', best.brain.wih, best.brain.who)
        self.cross()
        Dock().random_y()

    def update(self, dt):
        for i in self.population:
            i.update(dt)

    def draw(self):
        for i in self.population:
            i.draw()
