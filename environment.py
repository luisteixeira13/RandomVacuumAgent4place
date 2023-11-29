# environment.py
import random

OBSTACLE = '-1'
MAP_ROAD = '-'
MAP_OBSTACLE = 'O'
CLEAN_PER_TIME = 10

class Environment:
    def __init__(self, size=5, dirty_prob=0.2):
        self.size = size
        self.positionX = random.randint(0, size - 1)
        self.positionY = random.randint(0, size - 1)
        self.dirty_prob = dirty_prob
        self.maze = [[0 for _ in range(size)] for _ in range(size)]
        self.generate_random_dirt()

    def generate_random_dirt(self):
        for x in range(self.size):
            for y in range(self.size):
                if random.random() < self.dirty_prob:
                    self.maze[x][y] = 1

    def dirt_amount(self, x, y):
        return self.maze[x][y]

    def accept_action(self, action):
        if action == 'UP' and self.positionX > 0:
            self.positionX -= 1
        elif action == 'DOWN' and self.positionX < self.size - 1:
            self.positionX += 1
        elif action == 'LEFT' and self.positionY > 0:
            self.positionY -= 1
        elif action == 'RIGHT' and self.positionY < self.size - 1:
            self.positionY += 1

        if action == 'SUCK' and self.maze[self.positionX][self.positionY] > 0:
            dirt = self.maze[self.positionX][self.positionY]
            if dirt > CLEAN_PER_TIME:
                self.maze[self.positionX][self.positionY] -= CLEAN_PER_TIME
            else:
                self.maze[self.positionX][self.positionY] = 0

    def is_dirty(self):
        return self.maze[self.positionX][self.positionY] > 0

    def is_valid_position(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def print_maze(self):
        for x in range(self.size):
            for y in range(self.size):
                print(f'{self.maze[x][y]:2}', end=' ')
            print()
    def visualize(self):
            for x in range(self.size):
                for y in range(self.size):
                    if self.positionX == x and self.positionY == y:
                        print('A', end=' ')  # Representação do aspirador
                    else:
                        print(f'{self.maze[x][y]:2}', end=' ')
                print()
            print()