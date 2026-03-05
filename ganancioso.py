import heapq
import sys
from solucao import No, Problema, carregar_entrada
import os

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


def formatar_caminho(no):
    setas = []
    atual = no
    while atual and atual.no_pai:
        if atual.aresta:
            setas.append(atual.aresta)
        atual = atual.no_pai
    return "".join(reversed(setas))


def caminho_saida_por_entrada(caminho_entrada: str) -> str:
  
    os.makedirs("resultados", exist_ok=True)

    base = os.path.basename(caminho_entrada)
    nome, _ext = os.path.splitext(base)

    sufixo = "".join(ch for ch in nome if ch.isdigit())

    if sufixo:
        saida_nome = f"ganancioso{sufixo}.txt"
    else:
        saida_nome = f"ganancioso_{nome}.txt"

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
        print("Uso: python ganancioso.py grids/entrada8.txt")
        sys.exit(1)

    grid, n, m = carregar_entrada(sys.argv[1])
    if grid:
        prob = Problema(grid, n, m)
        print(f"Buscando solução para {sys.argv[1]} com Ganancioso...")

        no_solucao, total_visitados = executar_ganancioso(prob)

        saida_path = caminho_saida_por_entrada(sys.argv[1])
        salvar_saida(no_solucao, n, m, saida_path)

        if no_solucao:
            print(f"Sucesso! Estados visitados: {total_visitados}")
            print(f"Resultado salvo em: {saida_path}")
        else:
            print("Não foi possível encontrar uma solução.")