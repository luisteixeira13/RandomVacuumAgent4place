# agent.py

import random


class Agent:
    # Lista de ações possíveis que o agente pode executar
    ACTIONS = ['UP', 'DOWN', 'LEFT', 'RIGHT', 'SUCK']

    def __init__(self, zone):
        # Inicializa o agente com uma referência ao ambiente (zone)
        self.zone = zone

    def perspective(self):
        # Atualiza a perspectiva do agente com base nas condições do ambiente
        pass

    def think(self, has_dirt):
        if has_dirt:
            self.zone.suck()  # Limpa se houver sujeira

        # Em seguida, gera aleatoriamente uma nova ação
        return random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
