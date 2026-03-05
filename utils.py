import os

def formatar_caminho(no):
    setas = []
    atual = no
    while atual and atual.no_pai:
        if atual.aresta:
            setas.append(atual.aresta)
        atual = atual.no_pai
    return "".join(reversed(setas))

def caminho_saida_por_entrada(caminho_entrada: str, prefixo_algoritmo: str) -> str:
    os.makedirs("resultados", exist_ok=True)
    
    base = os.path.basename(caminho_entrada)
    nome, _ext = os.path.splitext(base)
    
    sufixo = "".join(ch for ch in nome if ch.isdigit())
    
    if sufixo:
        saida_nome = f"{prefixo_algoritmo}{sufixo}.txt"
    else:
        saida_nome = f"{prefixo_algoritmo}_{nome}.txt"
        
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