# agent.py
import random

class Agent:
    ACTIONS = ['UP', 'DOWN', 'LEFT', 'RIGHT', 'SUCK']

    def __init__(self, zone):
        self.zone = zone

    def perspective(self):
        pass

    def think(self):
            # Decide a ação com base na presença de sujeira
        if self.zone.maze[self.zone.positionX][self.zone.positionY] == 1:
            self.zone.suck()
            return "SUCK"
        return random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
       
