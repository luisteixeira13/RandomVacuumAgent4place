# main.py
from agent import Agent
from environment import Environment
from evaluator import Evaluator

def main():
    size = 3  # Defina o tamanho do labirinto
    dirty_prob = 0.5  # Defina a probabilidade da sujeira

    # Inicializa o ambiente, agente e avaliador
    env = Environment(size, dirty_prob)
    agent = Agent(env)
    evaluator = Evaluator()

    # Loop principal de simulação
    while env.has_dirt():  # Continue enquanto houver sujeira
        #agent.perspective()
        action = agent.think(env.has_dirt)
        env.accept_action(action)
        evaluator.evaluate(action, env)

        env.visualize()  # Visualize o ambiente a cada passo

    # Exibe os resultados da avaliação
    print("Evaluation Results:")
    print(f"Consumed Energy: {evaluator.consumed_energy}")
    print(f"Cleaned Dirty: {evaluator.cleaned_dirty}")
    print(f"Total Dirty: {evaluator.total_dirty}")
   

if __name__ == "__main__":
    main()
