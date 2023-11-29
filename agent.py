# agent.py
import random

class Agent:
    # Lista de ações possíveis que o agente pode executar
    ACTIONS = ['UP', 'DOWN', 'LEFT', 'RIGHT', 'SUCK', 'IDLE']

    def __init__(self, zone):
        # Inicializa o agente com uma referência ao ambiente (zone)
        self.zone = zone

    def random_action(self):
        # Gera aleatoriamente e retorna uma ação da lista de ações possíveis
        return random.choice(self.ACTIONS)

    def perspective(self):
        def perspective(self):
        # Atualiza a perspectiva do agente com base nas condições do ambiente
            #self.bump = self.zone.is_bump()
            #self.dirty = self.zone.is_dirty()
            #self.positionX, self.positionY = self.zone.positionX, self.zone.positionY
            pass

    def think(self):
        # Método que representa a lógica de tomada de decisão do agente.
        # Atualmente, retorna uma ação aleatória, mas pode ser expandido
        # para uma lógica mais inteligente com base nas condições do ambiente.
        return self.random_action()
