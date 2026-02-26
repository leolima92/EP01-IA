tamanho = 64
with open("entrada64.txt", "w", encoding="utf-8") as f:
    for r in range(tamanho):
        linha = []
        for c in range(tamanho):
            if r == 0 or r == tamanho-1 or c == 0 or c == tamanho-1:
                linha.append("🧱")
            elif r == 5 and c == 5: linha.append("🙎")
            elif r == 10 and c == 10: linha.append("1️⃣")
            elif r == 10 and c == 50: linha.append("🟢")
            elif r == 50 and c == 10: linha.append("2️⃣")
            elif r == 50 and c == 50: linha.append("🟢")
            else: linha.append("⚪️")
        f.write(" ".join(linha) + "\n")
print("entrada64.txt gerado")