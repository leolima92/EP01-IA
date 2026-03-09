import os

def formatar_caminho(no):
    setas = []
    atual = no
    while atual and atual.no_pai:
        if atual.aresta:
            setas.append(atual.aresta)
        atual = atual.no_pai
    return "".join(reversed(setas))

def caminho_saida_por_entrada(caminho_entrada: str, algoritmo: str) -> str:
    base = os.path.basename(caminho_entrada)
    nome, _ext = os.path.splitext(base)

    sufixo = "".join(ch for ch in nome if ch.isdigit())

    pasta_algoritmo = os.path.join("resultados", algoritmo)
    os.makedirs(pasta_algoritmo, exist_ok=True)

    saida_nome = f"{algoritmo}{sufixo}.txt"

    return os.path.join(pasta_algoritmo, saida_nome)

def salvar_saida(no_final, n, m, caminho_saida, tempo_execucao=None):
    with open(caminho_saida, "w", encoding="utf-8") as f:
        if no_final:
            for i in range(n):
                linha = no_final.estado[i*m : (i+1)*m]
                f.write(" ".join(linha) + "\n")

            f.write("\nMovimentos\n")
            caminho = formatar_caminho(no_final)
            f.write(caminho + "\n")

            f.write("\nQuantidade de movimentos\n")
            f.write(str(len(caminho)) + "\n")

            f.write("\nCusto total\n")
            f.write(str(no_final.custo) + "\n")

            if tempo_execucao is not None:
                f.write("\nTempo de execução (segundos)\n")
                f.write(f"{tempo_execucao:.4f}\n")
        else:
            f.write("Sem solução encontrada.\n")