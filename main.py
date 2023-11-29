# main.py

from agent import Agent
from environment import Environment
from evaluator import Evaluator


def main():
    size = 5
    dirty_prob = 0.2
    steps_between_visualizations = 10  # Defina o número de passos entre visualizações

    env = Environment(size, dirty_prob)
    agent = Agent(env)
    evaluator = Evaluator()

    for step in range(evaluator.LIFE_TIME):
        agent.perspective()
        action = agent.think()
        env.accept_action(action)
        evaluator.evaluate(action, env)

        if step % steps_between_visualizations == 0:
            env.visualize()  # Adicione esta linha para visualizar em tempo real

    print("Evaluation Results:")
    print(f"Consumed Energy: {evaluator.consumed_energy}")
    print(f"Cleaned Dirty: {evaluator.cleaned_dirty}")
    print(f"Total Dirty: {evaluator.total_dirty}")
    print(f"Dirty Degree: {evaluator.dirty_degree}")

if __name__ == "__main__":
    main()
