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

    def fill_mating_pool(self):
        fitness_l = np.array([i.fitness() for i in self.population])
        fitness_l += np.abs(fitness_l.min()) + 1
        fitness_l = list(fitness_l)
        s = sum(fitness_l)

        for i in range(len(fitness_l)):
            for j in range(int(fitness_l[i] / s * 100)):
                self.mating_pool.append(self.population[i])

    def cross(self):
        best = self.get_best().brain
        self.fill_mating_pool()

        self.population.clear()
        for i in range(GA_POPULATION):
            c = new_initalized_spaceship()
            c.brain = random.choice(self.mating_pool).brain.breed(
                random.choice(self.mating_pool).brain
            )
            if (random.random() < GA_MUTATING_RATE):
                c.brain.mutate()
            self.population.append(c)

        for i in range(3):
            b = new_initalized_spaceship()
            b.color = (0, 0, 255)
            b.brain = best
            self.population.append(b)

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
