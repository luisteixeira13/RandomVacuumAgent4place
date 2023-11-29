# evaluator.py
from environment import Environment

class Evaluator:
    def __init__(self) -> None:
        # Inicializa o avaliador com métricas de desempenho
        self.dirty_degree = 0
        self.consumed_energy = 0
        self.total_dirty = 0
        self.cleaned_dirty = 0
        self.new_dirty = 0
        self.LIFE_TIME = 2000

    def evaluate(self, action: str, env: Environment) -> None:
        # Avalia o desempenho do agente com base na ação tomada e no estado do ambiente
        if action == 'SUCK':
            # Se a ação for aspirar, incrementa a energia consumida (2 unidades)
            self.consumed_energy += 2
        elif action != 'IDLE':
            # Se a ação for qualquer outra que não seja IDLE, incrementa a energia consumida (1 unidade)
            self.consumed_energy += 1

        # Atualiza as métricas relacionadas à sujeira
        self.cleaned_dirty += env.maze[env.positionX][env.positionY]
        self.new_dirty = env.maze[env.positionX][env.positionY]
        self.total_dirty += self.new_dirty

        # Calcula o grau total de sujeira no ambiente
        self.dirty_degree = sum(sum(row) for row in env.maze)
