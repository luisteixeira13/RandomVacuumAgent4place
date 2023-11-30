# evaluator.py

from environment import Environment

class Evaluator:
    def __init__(self) -> None:
        # Inicializa o avaliador com métricas de desempenho
        self.consumed_energy = 0
        self.total_dirty = 0
        self.cleaned_dirty = 0

    def evaluate(self, action: str, env: Environment) -> None:
            # Avalia o desempenho do agente com base na ação tomada e no estado do ambiente
        if action == 'SUCK':
                # Se a ação for aspirar, incrementa a energia consumida (2 unidades)
            self.consumed_energy += 2
        else:
                # Se a ação for qualquer outra, incrementa a energia consumida (1 unidade)
            self.consumed_energy += 1

            # Atualiza as métricas relacionadas à sujeira
        self.cleaned_dirty += env.maze[env.positionX][env.positionY]
        self.total_dirty = sum(sum(row) for row in env.maze)
    
        