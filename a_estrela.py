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
    return