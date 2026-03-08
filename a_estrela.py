import heapq
import sys
from solucao import No, Problema, carregar_entrada
from utils import salvar_saida, caminho_saida_por_entrada

def executar_a_estrela(problema):
    no_raiz = problema.iniciar()
    no_raiz.heuristica = problema.heuristica(no_raiz)

    fronteira = []
    f_raiz = no_raiz.custo + no_raiz.heuristica
    heapq.heappush(fronteira, (f_raiz, id(no_raiz), no_raiz))

    visitados = {no_raiz.estado: no_raiz.custo}

    total_visitados = 0

    while fronteira:
        f_n, _, no_atual = heapq.heappop(fronteira)
        total_visitados += 1

        if problema.objetivo(no_atual):
            return no_atual, total_visitados
        
        for acao, no_filho in problema.sucessores(no_atual):
            if no_filho.estado not in visitados or no_filho.custo < visitados[no_filho.estado]:
                visitados[no_filho.estado] = no_filho.custo

                no_filho.heuristica = problema.heuristica(no_filho)
                f_filho = no_filho.custo + no_filho.heuristica

                heapq.heappush(fronteira, (f_filho, id(no_filho), no_filho))
        return None, total_visitados
