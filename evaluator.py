# evaluator.py

class Evaluator:
    def __init__(self):
        self.dirty_degree = 0
        self.consumed_energy = 0
        self.total_dirty = 0
        self.cleaned_dirty = 0
        self.new_dirty = 0
        self.LIFE_TIME = 2000

    def evaluate(self, action, env):
        if action == 'SUCK':
            self.consumed_energy += 2
        elif action != 'IDLE':
            self.consumed_energy += 1

        self.cleaned_dirty += env.maze[env.positionX][env.positionY]
        self.new_dirty = env.maze[env.positionX][env.positionY]
        self.total_dirty += self.new_dirty

        self.dirty_degree = sum(sum(row) for row in env.maze)
