# Projeto de Busca: Agente e Caixas (Sokoban Ponderado)
O projeto implementa algoritmos de busca para resolver um quebra-cabeça onde um agente deve empurrar caixas numeradas até áreas específicas. O diferencial deste modelo é que cada caixa possui um "peso" que influencia o custo do movimento.

### 1. Função Sucessora (`gerar_sucessores`)

A função sucessora é responsável por determinar quais estados podem ser alcançados a partir do estado atual.

* **Mecânica:** O algoritmo localiza o agente (`🙎`) e testa movimentos para as quatro direções cardinais.
* **Movimento Simples:** O agente se move para uma célula vizinha se ela for um espaço vazio (`⚪️`) ou um alvo (`🟢`).
* **Movimento de Empurrar:** Se o agente encontrar uma caixa (`1️⃣`, `2️⃣`, etc.), o algoritmo verifica a célula seguinte na mesma direção. Se estiver livre, o agente "empurra" a caixa, resultando em um novo estado onde tanto o agente quanto a caixa mudaram de posição.
* **Bloqueios:** Paredes (`🧱`) e o limite do mapa impedem a geração de sucessores naquela direção.

### 2. Função Objetivo (`testar_objetivo`)

A função objetivo define quando o problema foi resolvido.

* Ela armazena os índices originais de todos os alvos (`🟢`) no início da execução.
* A cada novo estado, ela verifica se **todos** esses índices agora contêm uma caixa (qualquer valor numérico).
* O objetivo é satisfeito apenas quando não resta nenhum alvo vazio.

### 3. Calcular Custo (`calcular_passo`)

Diferente de buscas uniformes, aqui cada ação possui um custo específico baseado no esforço:

* **Custo Base:** Qualquer movimento do agente tem um custo base de **1**.
* **Custo de Empuxo:** Se o agente empurrar uma caixa, o custo desse passo é somado ao valor numérico daquela caixa.
* **Fórmula:** $Custo = 1 + Valor\_da\_Caixa$.
* *Exemplo:* Empurrar a caixa `8️⃣` custa **9**, enquanto empurrar a caixa `1️⃣` custa **2**.



### 4. Função Heurística (`heuristica`)

A heurística estima a distância que falta para atingir o objetivo. Utilizamos a **Soma das Distâncias de Manhattan**.

* Para cada caixa no mapa, calculamos a distância entre sua posição atual $(linha_c, coluna_c)$ e a posição do alvo mais próximo $(linha_a, coluna_a)$:

$$h(n) = |linha_c - linha_a| + |coluna_c - coluna_a|$$


* A heurística total é a soma dessas distâncias para todas as caixas. Isso fornece ao algoritmo uma "bússola" de qual estado parece estar mais perto da vitória.

### 5. Representação Interna de Estados

Para garantir eficiência e evitar loops infinitos, o estado é tratado da seguinte forma:

* **Estrutura:** O grid é convertido em uma **lista flat** (unidimensional) de strings. Isso facilita a cópia de estados e a busca de índices.
* **Identificador (ID):** Criamos uma string única para cada estado usando `"".join(estado)`.
* **Memória de Busca:**
* No **Dijkstra**, usamos um dicionário `visitados = {id: custo}` para garantir que só re-exploremos um estado se encontrarmos um caminho mais barato.
* No **Ganancioso**, usamos um `set()` apenas para evitar repetir estados, já que ele não foca no custo acumulado.
* (falta o estrela)



### 6. Por que a Heurística é Admissível?

Uma heurística é **admissível** se ela nunca superestima o custo real: $$h(n) \leq h^*(n)$$

* **Prova de Admissibilidade:** A distância de Manhattan assume um mundo perfeito sem paredes, onde as caixas vão direto ao alvo.
* No nosso problema, o custo real sempre será igual ou maior que a distância de Manhattan, pois:
1. O custo de mover uma caixa é sempre $\ge 2$ (1 do passo + pelo menos 1 do peso da caixa).
2. A distância de Manhattan conta apenas os passos, e cada passo no nosso código custa no mínimo 1.
3. Paredes e manobras do agente para se posicionar atrás da caixa adicionam custos extras que a heurística ignora.


* Portanto, $h(n)$ sempre será uma estimativa "otimista", o que garante que, ao usar o A*, encontraremos a solução ótima.
