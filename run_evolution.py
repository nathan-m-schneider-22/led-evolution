
from xxlimited import foo

from numpy import average
from critter import Critter
import time
import random
from colorama import Fore, Style

WORLD_SIZE = 100
DELAY = .1


class World:
    def __init__(self, num_critters=5, food_rate=1):
        self.world = [" "] * WORLD_SIZE
        self.food_rate = food_rate
        self.critters = [Critter(self.world) for _ in range(num_critters)]

        self.tick = 0

        self.data_file = open("evo_dat.csv", "w")
        self.data_file.write("tick,population,average_speed\n")

    def loop(self):
        for c in self.critters:
            c.move()
            if self.world[int(c.position)] == "F":
                print("EATEN")
                c.stomach += 1
                self.world[int(c.position)] = " "

            if c.stomach >= 2:
                new_critter = Critter(self.world, parent=c)
                new_critter.position = c.position
                c.stomach -= 1
                self.critters.append(new_critter)

            if c.stomach <= 0:
                self.critters.remove(c)
        if len(self.critters) == 0:
            exit(1)

        if random.random() < self.food_rate:
            i = random.randrange(WORLD_SIZE)
            while self.world[i] != " ":
                i = random.randrange(WORLD_SIZE)
            self.world[i] = 'F'

        self.tick += 1

    def render(self):
        render_array = [d for d in self.world]

        for c in self.critters:
            print(int(c.position))
            render_array[int(c.position)] = 'C'

        # print(chr(27) + "[2J")

        for c in render_array:
            if c == "C":
                print(Fore.CYAN + c + Style.RESET_ALL, end="")
            elif c == "F":
                print(Fore.YELLOW + c + Style.RESET_ALL, end="")
            else:
                print(c, end="")
        print()
        mean_speed = average([c.speed for c in self.critters])

        print("Population: ", len(self.critters))
        print("Mean speed: %.3f" % mean_speed)
        self.data_file.write("%s,%s,%s\n" % (self.tick,
                             len(self.critters), mean_speed))


def main():
    test = World()
    while True:
        test.loop()
        test.render()
        time.sleep(DELAY)


if __name__ == "__main__":
    main()
