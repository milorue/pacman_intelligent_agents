from freegames import floor, vector
from random import choice, randint

class PacmanRandom:
    def __init__(self, vec, direction):
        self.direction = direction
        self.agent = vec
        self.moves = [
            vector(10, 0),
            vector(-10, 0),
            vector(0, 10),
            vector(0, -10)
        ]

    def move(self):
        randomNum = randint(1,10)
        if randomNum >= 5:
            return self.direction
        else:
            self.choose_direction()
            return self.direction

    def choose_direction(self):
        self.direction = choice(self.moves)






