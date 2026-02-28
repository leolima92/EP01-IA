import heapq
import sys
import os
from solucao import No, Problema, carregar_entrada

def executar_dijkstra(problema):
    no_raiz = problema.iniciar()
    # Fila de prioridade: (custo, nó)
    fronteira = [(0, no_raiz)]
    # Controle de visitados: {id_do_estado: custo_minimo}
    visitados = {no_raiz.id: 0}
    estados_contagem = 0

    while fronteira:
        custo_atual, no_atual = heapq.heappop(fronteira)
        estados_contagem += 1

        if problema.testar_objetivo(no_atual):
            return no_atual, estados_contagem

        if custo_atual > visitados.get(no_atual.id, float('inf')):
            continue

        for sucessor in problema.gerar_sucessores(no_atual):
            if sucessor.id not in visitados or sucessor.custo < visitados[sucessor.id]:
                visitados[sucessor.id] = sucessor.custo
                heapq.heappush(fronteira, (sucessor.custo, sucessor))

    return None, estados_contagem

def formatar_caminho(no):
    setas = []
    atual = no
    while atual and atual.no_pai:
        if atual.aresta:
            setas.append(atual.aresta)
        atual = atual.no_pai
    return "".join(reversed(setas))

def caminho_saida_por_entrada(caminho_entrada: str) -> str:
    """
    Ex.: grids/entrada8.txt -> resultados/dijkstra8.txt
    """
    os.makedirs("resultados", exist_ok=True)

    base = os.path.basename(caminho_entrada)          
    nome, _ext = os.path.splitext(base)              

    # pega só o sufixo numérico se existir (entrada8 = 8)
    sufixo = "".join(ch for ch in nome if ch.isdigit())

    if sufixo:
        saida_nome = f"dijkstra{sufixo}.txt"
    else:
        # fallback: se não tiver número, usa o nome todo
        # ex.: entrada_teste.txt -> dijkstra_entrada_teste.txt
        saida_nome = f"dijkstra_{nome}.txt"

    return os.path.join("resultados", saida_nome)



def salvar_saida(no_final, n, m, caminho_saida):
    with open(caminho_saida, "w", encoding="utf-8") as f:
        if no_final:
            for i in range(n):
                linha = no_final.estado[i*m : (i+1)*m]
                f.write(" ".join(linha) + "\n")

            f.write("Movimentos\n")
            caminho = formatar_caminho(no_final)
            f.write(caminho + "\n")

            f.write("Quantidades de movimentos\n")
            f.write(str(len(caminho)) + "\n")
        else:
            f.write("Sem solução encontrada.\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python dijkstra.py grids/entrada8.txt")
        sys.exit(1)

    grid, n, m = carregar_entrada(sys.argv[1])
    if grid:
        prob = Problema(grid, n, m)
        print(f"Buscando solução para {sys.argv[1]} com Dijkstra...")
        
        no_solucao, total_visitados = executar_dijkstra(prob)

        saida_path = caminho_saida_por_entrada(sys.argv[1])
        salvar_saida(no_solucao, n, m, saida_path)
        
        if no_solucao:
            print(f"Sucesso! Estados visitados: {total_visitados}")
            print(f"Custo total: {no_solucao.custo}")
            print(f"Resultado salvo em: {saida_path}")
        else:
            print("Não foi possível encontrar uma solução.")



# O objetivo deste algoritmo é encontrar o caminho de custo mínimo entre o
# estado inicial e o estado objetivo (todas as caixas nos alvos).
#
# FUNCIONAMENTO:
# 1. Utiliza uma FILA DE PRIORIDADE (Min-Heap) para garantir que o próximo 
#    nó a ser explorado seja sempre o de menor custo acumulado (g).
# 2. O custo é PONDERADO: passos vazios custam 1, enquanto empurrar caixas 
#    adiciona o peso da caixa ao custo do movimento (1 + W).
# 3. CONTROLE DE VISITADOS: Utiliza um dicionário para mapear o ID de cada 
#    estado ao seu menor custo encontrado. Isso evita ciclos e garante que 
#    não processemos o mesmo estado com um custo maior.
# 4. EXTRACAO DE RESULTADO: Ao atingir o objetivo, o algoritmo reconstrói 
#    a sequência de movimentos (setas) retrocedendo pelos nós pais.