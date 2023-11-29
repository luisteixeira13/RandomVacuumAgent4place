# agent.py
import random

class Agent:
    ACTIONS = ['UP', 'DOWN', 'LEFT', 'RIGHT', 'SUCK', 'IDLE']

    def __init__(self, zone):
        self.zone = zone

    def random_action(self):
        return random.choice(self.ACTIONS)

    def perspective(self):
        pass

    def think(self):
        return self.random_action()
