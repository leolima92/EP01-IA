import heapq
import sys
import time
from core.solucao import No, Problema, carregar_entrada
from core.utils import salvar_saida, caminho_saida_por_entrada

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

    caminho_grid = sys.argv[1]

    grid, n, m = carregar_entrada(caminho_grid)

    if grid:
        prob = Problema(grid, n, m)

        print(f"Buscando solução para {caminho_grid} com Busca Gananciosa...")

        inicio = time.perf_counter()

        no_solucao, total_visitados = executar_ganancioso(prob)

        fim = time.perf_counter()
        tempo_execucao = fim - inicio

        saida_path = caminho_saida_por_entrada(caminho_grid, "ganancioso")

        salvar_saida(no_solucao, n, m, saida_path, tempo_execucao, total_visitados)

        print(f"Estados visitados: {total_visitados}")

        if no_solucao:
            print(f"Custo total: {no_solucao.custo}")
            print(f"Tempo de execução: {tempo_execucao:.4f} segundos")
            print(f"Resultado salvo em: {saida_path}")
        else:
            print("Não foi possível encontrar uma solução.")
            print(f"Tempo de execução: {tempo_execucao:.4f} segundos")
            print(f"Arquivo de saída gerado em: {saida_path}")

