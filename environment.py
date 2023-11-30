# environment.py
import random
from typing import List


class Environment:
    def __init__(self, size: int = 3, dirty_prob: float = 0.5) -> None:
        # Inicializa o ambiente com o tamanho especificado e probabilidade de sujeira
        self.size = size
        self.positionX = random.randint(0, size - 1)
        self.positionY = random.randint(0, size - 1)
        self.dirty_prob = dirty_prob
        self.maze = [[0 for _ in range(size)] for _ in range(size)]
        self.generate_random_dirt()
        print("Bem-vindo ao ambiente do aspirador de pó!")
        print("O ambiente é representado por uma grade, onde:")
        print(" - 'A' representa a posição atual do agente.")
        print(" - '1' representa uma sujeira.")
        print(" - '0' representa uma posição limpa.")
        print("\nEstado Inicial do Ambiente:")
        self.visualize()
        print("\nLimpeza:")
    
    def generate_random_dirt(self) -> None:
        # Gera aleatoriamente sujeira no ambiente com base na probabilidade
        for x in range(self.size):
            for y in range(self.size):
                if random.random() < self.dirty_prob:
                    self.maze[x][y] = 1

    def dirt_amount(self, x, y):
        # Retorna a quantidade de sujeira na posição especificada
        return self.maze[x][y]

    def accept_action(self, action):
        # Aceita e processa a ação tomada pelo agente
        if action == 'UP' and self.positionX > 0:
            self.positionX -= 1
        elif action == 'DOWN' and self.positionX < self.size - 1:
            self.positionX += 1
        elif action == 'LEFT' and self.positionY > 0:
            self.positionY -= 1
        elif action == 'RIGHT' and self.positionY < self.size - 1:
            self.positionY += 1

    def suck(self):
        # Realiza a aspiração e remove a sujeira da posição atual
        if self.maze[self.positionX][self.positionY] > 0:
            self.maze[self.positionX][self.positionY] = 0

    def visualize(self, action: str = None) -> None:
        # Visualiza o estado atual do ambiente a cada passo do agente
        print(f"Agent position: ({self.positionX}, {self.positionY})")
        print("Environment:")
        for x in range(self.size):
            row_str = []
            for y in range(self.size):
                if (x, y) == (self.positionX, self.positionY):
                    row_str.append(" A ")
                elif self.maze[x][y] == 1:
                    row_str.append(" 1 ")
                else:
                    row_str.append(" 0 ")
            print(row_str)
        if action:
            print(f"Agent took action: {action}")
        print()

    def has_dirt(self) -> bool:
        # Verifica se há sujeira no ambiente
        return any(any(row) for row in self.maze)

    def visualize_end(self) -> None:
        # Método adicional para visualizar o estado final
        print("Final State:")
        self.visualize()