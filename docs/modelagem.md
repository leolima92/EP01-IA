# Modelagem do Problema

## Visão geral

Este projeto modela um problema de busca em espaço de estados inspirado em Sokoban ponderado. O ambiente é um tabuleiro em grade onde existe um agente, caixas com pesos diferentes, alvos, paredes e espaços livres.

O objetivo é mover todas as caixas até os alvos com o menor custo possível.

---

## Representação dos estados

Um **estado** representa uma configuração completa do tabuleiro em um determinado instante.

Cada estado contém:

- a posição do agente;
- a posição das caixas;
- a posição dos alvos;
- a posição das paredes;
- os espaços livres.

Em outras palavras, um estado é uma fotografia completa do tabuleiro.

Dois estados são diferentes quando a posição do agente ou de qualquer caixa muda.

---

## Ações possíveis

Em cada estado, o agente pode tentar executar quatro ações:

- mover para cima;
- mover para baixo;
- mover para a esquerda;
- mover para a direita.

Essas ações podem resultar em:

- **movimento simples**, quando o agente anda para uma célula livre;
- **movimento com empurrão**, quando o agente empurra uma caixa para uma célula livre;
- **ação inválida**, quando existe parede, limite do mapa ou bloqueio.

---

## Função sucessora

A função sucessora recebe um estado atual e gera todos os estados válidos alcançáveis com uma única ação.

O processo é:

1. localizar o agente;
2. testar as quatro direções;
3. verificar se o movimento é válido;
4. gerar um novo estado quando a ação puder ser executada.

Se a célula à frente estiver livre, o agente apenas se move.  
Se houver uma caixa, o algoritmo verifica se a célula seguinte está livre para permitir o empurrão.  
Caso contrário, a ação é descartada.

---

## Verificação do objetivo

O objetivo do problema é colocar todas as caixas sobre as posições de destino.

Um estado é objetivo quando todos os alvos estão ocupados por caixas.

Assim, o algoritmo verifica se cada posição marcada como alvo contém uma caixa no estado atual.

---

## Função custo

A função custo mede o esforço necessário para executar uma ação.

- Um movimento simples custa **1**.
- Um movimento com empurrão custa **1 + peso da caixa**.

Isso significa que o problema não busca apenas o menor número de passos, mas o menor custo total.

---

## Função heurística

A heurística estima o quanto ainda falta para alcançar o objetivo.

Foi utilizada a soma das distâncias de Manhattan entre cada caixa e o alvo mais próximo.

A distância de Manhattan entre uma caixa na posição \((r_c, c_c)\) e um alvo na posição \((r_a, c_a)\) é dada por:

\[
d = |r_c - r_a| + |c_c - c_a|
\]

Essa heurística ajuda os algoritmos informados a priorizarem estados que parecem mais próximos da solução.

---

## Uso nos algoritmos

Os algoritmos utilizam essas funções de formas diferentes:

- **Dijkstra** usa apenas o custo acumulado \(g(n)\);
- **Ganancioso** usa apenas a heurística \(h(n)\);
- **A\*** usa \(f(n) = g(n) + h(n)\).

---

## Diagrama Mermaid da modelagem

```mermaid
flowchart TD
    A[Estado inicial do tabuleiro] --> B[Representar estado]

    B --> B1[Posição do agente]
    B --> B2[Posição das caixas]
    B --> B3[Posição dos alvos]
    B --> B4[Paredes e células livres]

    B --> C[Gerar ações possíveis]

    C --> C1[Mover para cima]
    C --> C2[Mover para baixo]
    C --> C3[Mover para esquerda]
    C --> C4[Mover para direita]

    C1 --> D[Aplicar função sucessora]
    C2 --> D
    C3 --> D
    C4 --> D

    D --> E{Movimento válido?}

    E -- Não --> F[Descartar ação]
    E -- Sim --> G{Há caixa na direção?}

    G -- Não --> H[Gerar novo estado com movimento simples]
    G -- Sim --> I{Caixa pode ser empurrada?}

    I -- Não --> F
    I -- Sim --> J[Gerar novo estado com empurrão]

    H --> K[Calcular custo g(n)]
    J --> K

    K --> L[Calcular heurística h(n)]
    L --> M[Calcular função de avaliação]

    M --> M1[Dijkstra: f(n) = g(n)]
    M --> M2[Ganancioso: f(n) = h(n)]
    M --> M3[A*: f(n) = g(n) + h(n)]

    M1 --> N[Inserir na fronteira]
    M2 --> N
    M3 --> N

    N --> O[Selecionar próximo estado]
    O --> P{É estado objetivo?}

    P -- Não --> C
    P -- Sim --> Q[Reconstruir caminho solução]
    Q --> R[Exibir ações, custo total e estados visitados]