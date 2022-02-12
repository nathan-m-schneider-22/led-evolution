import random

SPEED_MOD = .5
STARVE_TIME = 20
MUTATION_SIZE = .1


class Critter:
    def __init__(self, world, parent=None):
        self.world_size = len(world)
        self.world = world
        self.speed = self.generate_stats(parent=parent)
        self.position = random.randrange(self.world_size)

        self.stomach = 1

    def generate_stats(self, parent=None):
        if parent == None:
            return random.random() * SPEED_MOD
        return parent.speed + random.uniform(-1, 1) * MUTATION_SIZE

    def move(self):
        direction = self.choose_direction()
        self.position = (self.position + direction*self.speed) \
            % self.world_size
        self.stomach -= 1/STARVE_TIME

    def choose_direction(self):
        for distance in range(int(self.world_size/2)):
            forward = (int(self.position) + distance) % self.world_size
            if self.world[forward] == 'F':
                return 1

            back = (int(self.position) - distance) % self.world_size
            if self.world[back] == 'F':
                return -1

        return 1
