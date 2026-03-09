import heapq
import sys
import time
from core.solucao import No, Problema, carregar_entrada
from core.utils import salvar_saida, caminho_saida_por_entrada

def executar_a_estrela(problema):
    no_raiz = problema.iniciar()
    no_raiz.heuristica = problema.heuristica(no_raiz)

    fronteira = []
    f_raiz = no_raiz.custo + no_raiz.heuristica
    heapq.heappush(fronteira, (f_raiz, id(no_raiz), no_raiz))

    visitados = {no_raiz.id: no_raiz.custo}

    total_visitados = 0

    while fronteira:
        f_n, _, no_atual = heapq.heappop(fronteira)
        total_visitados += 1

        if problema.testar_objetivo(no_atual):
            return no_atual, total_visitados
        
        for no_filho in problema.gerar_sucessores(no_atual):
            
            if no_filho.id not in visitados or no_filho.custo < visitados[no_filho.id]:
                visitados[no_filho.id] = no_filho.custo

                no_filho.heuristica = problema.heuristica(no_filho)
                f_filho = no_filho.custo + no_filho.heuristica

                heapq.heappush(fronteira, (f_filho, id(no_filho), no_filho))
                
    return None, total_visitados

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python a_estrela.py grids/entrada8.txt")
        sys.exit(1)

    grid, n, m = carregar_entrada(sys.argv[1])

    if grid:
        prob = Problema(grid, n, m)

        print(f"Buscando solução para {sys.argv[1]} com A*...")

        inicio = time.perf_counter()

        no_solucao, total_visitados = executar_a_estrela(prob)

        fim = time.perf_counter()
        tempo_execucao = fim - inicio
        
        saida_path = caminho_saida_por_entrada(sys.argv[1], "a_estrela")

        salvar_saida(no_solucao, n, m, saida_path, tempo_execucao)

        if no_solucao:
            print("Sucesso!")
            print(f"Estados visitados: {total_visitados}")
            print(f"Custo total: {no_solucao.custo}")
            print(f"Tempo de execução: {tempo_execucao:.4f} segundos")
            print(f"Resultado salvo em: {saida_path}")
        else:
            print("Não foi possível encontrar uma solução.")
            print(f"Tempo de execução: {tempo_execucao:.4f} segundos")
            print(f"Estados visitados: {total_visitados}")

#Executar código:
# python -m algoritmos.a_estrela grids/entrada8.txt

# O objetivo deste algoritmo é encontrar o caminho de custo mínimo de forma 
# inteligente, unindo a precisão do Dijkstra com a velocidade do Ganancioso.
#
# FUNCIONAMENTO:
# 1. Utiliza uma FILA DE PRIORIDADE (Min-Heap) baseada na função de avaliação 
#    f(n) = g(n) + h(n). Ele avalia tanto o custo real acumulado (g) quanto a 
#    estimativa da heurística (h) para o alvo.
# 2. CUSTO E HEURÍSTICA: O custo (g) é PONDERADO (passos vazios = 1; empurrar 
#    caixa = 1 + W). A heurística (h) estima o esforço restante. Como a heurística 
#    é admissível (nunca superestima o custo real), o A* garante a solução ótima.
# 3. CONTROLE DE VISITADOS: Utiliza um dicionário para mapear o ID de cada estado 
#    ao seu menor custo (g) já encontrado. Se o algoritmo esbarrar em um estado 
#    já visitado, mas por um caminho mais barato, ele atualiza esse custo e 
#    reaproveita a rota.
# 4. COMPORTAMENTO: Por olhar o custo real, ele evita as armadilhas do Ganancioso. 
#    Por usar a heurística, ele foca em ir em direção ao alvo, evitando se 
#    espalhar cegamente para todos os lados como o Dijkstra.
# 5. EXTRAÇÃO DE RESULTADO: Ao atingir o objetivo, o algoritmo reconstrói a 
#    sequência de movimentos (setas) retrocedendo pelos nós pais.