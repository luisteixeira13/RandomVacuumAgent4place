# RandomVacuumAgent4place

# Alunos: Isaac Orcine e Luis Felipe Costa Teixeira -- Turma 14A

Este é um projeto simples de um aspirador de pó que se move aleatoriamente em um ambiente bidimensional. Esse é um ambiente simulado de um aspirador de pó automático (Random Vacuum Agent). O ambiente é representado por uma grade (matriz) onde o agente (aspirador de pó) se move. O objetivo do agente é limpar as sujeiras presentes na grade. A principio ele vai se mover aleatoriamente até que limpe toda sujeira e assim termina a execução. (Podem ser adicionadas medidas para que ele termine de outra forma ou tenha um tempo de vida)

## Conteúdo

1. [Estrutura do Projeto](#estrutura-do-projeto)
2. [Como Executar](#como-executar)
3. [Módulos](#módulos)
   - [Agent](#agent)
   - [Environment](#environment)
   - [Evaluator](#evaluator)
4. [Uso](#uso)
5. [Próximos Passos](#próximos-passos)

## Estrutura do Projeto

 O projeto está organizado da seguinte forma:

- `agent.py`: Contém a implementação do agente.
- `environment.py`: Contém a implementação do ambiente.
- `evaluator.py`: Contém a implementação do avaliador.
- `main.py`: Arquivo principal para executar a simulação.

## Como Executar

Para executar a simulação, basta rodar o script `main.py`. Certifique-se de ter o Python instalado.

## módulos
## agent

O módulo agent.py contém a implementação do agente. O agente move-se aleatoriamente no ambiente e toma decisões com base nessa movimentação.
## Environment

O módulo environment.py implementa o ambiente bidimensional no qual o agente opera. Inclui a lógica para aceitar ações do agente e gerar sujeira de forma aleatória.
## Evaluator

O módulo evaluator.py implementa o avaliador, que monitora o desempenho do agente ao longo do tempo.

## Uso

Clone o Repositório:

git clone https://github.com/luisteixeira13/random-vacuum-agent.git

Navegue até o Diretório do Projeto:

-- cd random-vacuum-agent

-- Execute o Script Principal:

-- python main.py


## Próximos Passos

    Melhorar a lógica de decisão do agente para torná-lo mais inteligente.
    Adicionar mais recursos ao ambiente, como obstáculos ou múltiplos agentes.
    


