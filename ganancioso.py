import heapq
import sys
import os
from solucao import No, Problema, carregar_entrada
from utils import salvar_saida, caminho_saida_por_entrada

def executar_ganancioso(problema):
    no_raiz = problema.iniciar()
    no_raiz.heuristica = problema.heuristica(no_raiz)
    
    estados_pendentes = [(no_raiz.heuristica, no_raiz)]
    
    visitados = set()
    estados_contagem = 0

    while estados_pendentes:
        h_atual, no_atual = heapq.heappop(estados_pendentes)
        
        if no_atual.id in visitados:
            continue
            
        visitados.add(no_atual.id)
        estados_contagem += 1

        if problema.testar_objetivo(no_atual):
            return no_atual, estados_contagem

        for sucessor in problema.gerar_sucessores(no_atual):
            if sucessor.id not in visitados:
                sucessor.heuristica = problema.heuristica(sucessor)
                heapq.heappush(estados_pendentes, (sucessor.heuristica, sucessor))

    return None, estados_contagem

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python ganancioso.py grids/entrada8.txt")
        sys.exit(1)

    grid, n, m = carregar_entrada(sys.argv[1])
    if grid:
        prob = Problema(grid, n, m)
        print(f"Buscando solução para {sys.argv[1]} com Ganancioso...")

        no_solucao, total_visitados = executar_ganancioso(prob)

        saida_path = caminho_saida_por_entrada(sys.argv[1], "ganancioso")
        salvar_saida(no_solucao, n, m, saida_path)

        if no_solucao:
            print(f"Sucesso! Estados visitados: {total_visitados}")
            print(f"Resultado salvo em: {saida_path}")
        else:
            print("Não foi possível encontrar uma solução.")


#Executar código:
# python ganancioso.py grids/entrada8.txt

# O objetivo deste algoritmo é encontrar o estado objetivo o mais rápido possível,
# priorizando estados que parecem estar mais "perto" da solução segundo uma heurística.
#
# FUNCIONAMENTO:
# 1. Utiliza uma FILA DE PRIORIDADE (Min-Heap) baseada apenas no valor da 
#    HEURÍSTICA (h). Ele não leva em conta o custo (g) percorrido até aqui.
# 2. HEURÍSTICA (h): É uma função (geralmente Distância de Manhattan) que estima 
#    a distância de cada caixa até o alvo mais próximo.
# 3. COMPORTAMENTO "MÍOPE": O algoritmo é chamado de "ganancioso" porque ele 
#    sempre escolhe o caminho que parece melhor no curto prazo, sem considerar 
#    se aquele movimento foi caro ou se levará a um beco sem saída.
# 4. CONTROLE DE VISITADOS: Utiliza um conjunto (set) de IDs para garantir que 
#    cada configuração do tabuleiro seja explorada apenas uma vez.
# 5. VANTAGEM VS DESVANTAGEM: Geralmente é muito mais rápido e visita menos 
#    estados que o Dijkstra, porém NÃO GARANTE a solução de custo mínimo.