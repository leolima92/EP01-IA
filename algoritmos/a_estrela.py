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

        salvar_saida(no_solucao, n, m, saida_path, tempo_execucao, total_visitados)

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

