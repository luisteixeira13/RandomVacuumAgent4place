# main.py
from agent import Agent
from environment import Environment
from evaluator import Evaluator

def main():
    size = 5 # Defina o tamanho do labirinto
    dirty_prob = 0.2  # Defina a probabilidade da sujeira
    steps_between_visualizations = 10  # Defina o número de passos entre visualizações

    # Inicializa o ambiente, agente e avaliador
    env = Environment(size, dirty_prob)
    agent = Agent(env)
    evaluator = Evaluator()

    # Loop principal de simulação
    for step in range(evaluator.LIFE_TIME):
        agent.perspective()  # Atualiza a perspectiva do agente (Não implementado)
        action = agent.think()  # O agente decide a próxima ação com base na perspectiva
        env.accept_action(action)  # O ambiente aceita e processa a ação
        evaluator.evaluate(action, env)  # O avaliador avalia o desempenho do agente

        if step % steps_between_visualizations == 0:
            env.visualize()  # Visualiza o ambiente em tempo real (adicionado)

    # Exibe os resultados da avaliação
    print("Evaluation Results:")
    print(f"Consumed Energy: {evaluator.consumed_energy}")
    print(f"Cleaned Dirty: {evaluator.cleaned_dirty}")
    print(f"Total Dirty: {evaluator.total_dirty}")
    print(f"Dirty Degree: {evaluator.dirty_degree}")

if __name__ == "__main__":
    main()
