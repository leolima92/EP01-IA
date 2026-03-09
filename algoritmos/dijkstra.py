import heapq
import sys
import time
from core.solucao import No, Problema, carregar_entrada
from core.utils import salvar_saida, caminho_saida_por_entrada

def executar_dijkstra(problema):
    no_raiz = problema.iniciar()
    # Fila de prioridade: (custo, nó)
    estados_pendentes = [(0, no_raiz)]
    # Controle de visitados: {id_do_estado: custo_minimo}
    visitados = {no_raiz.id: 0}
    estados_contagem = 0

    while estados_pendentes:
        custo_atual, no_atual = heapq.heappop(estados_pendentes)
        estados_contagem += 1

        if problema.testar_objetivo(no_atual):
            return no_atual, estados_contagem

        if custo_atual > visitados.get(no_atual.id, float('inf')):
            continue

        for sucessor in problema.gerar_sucessores(no_atual):
            if sucessor.id not in visitados or sucessor.custo < visitados[sucessor.id]:
                visitados[sucessor.id] = sucessor.custo
                heapq.heappush(estados_pendentes, (sucessor.custo, sucessor))

    return None, estados_contagem

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python dijkstra.py grids/entrada8.txt")
        sys.exit(1)

    caminho_grid = sys.argv[1]

    grid, n, m = carregar_entrada(caminho_grid)

    if grid:
        prob = Problema(grid, n, m)

        print(f"Buscando solução para {caminho_grid} com Dijkstra...")

        inicio = time.perf_counter()

        no_solucao, total_visitados = executar_dijkstra(prob)

        fim = time.perf_counter()
        tempo_execucao = fim - inicio

        saida_path = caminho_saida_por_entrada(caminho_grid, "dijkstra")

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
            

