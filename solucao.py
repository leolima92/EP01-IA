import sys
import heapq
import math

class No:
    def __init__(self, estado, no_pai=None, aresta=None, custo=0, heuristica=0.0):  
        self.estado = estado
        self.no_pai = no_pai
        self.aresta = aresta
        self.custo = custo
        self.heuristica = heuristica
        self.id = "".join(estado) 
        
    def __lt__(self, outro):
        return (self.custo + self.heuristica) < (outro.custo + outro.heuristica)

class Problema:
    def __init__(self, grid_inicial, N, M):
        self.estado_inicial = grid_inicial
        self.N = N # Altura
        self.M = M # Largura
        self.valor = {
            "1️⃣": 1, "2️⃣": 2, "3️⃣": 3, "4️⃣": 4, "5️⃣": 5,
            "6️⃣": 6, "7️⃣": 7, "8️⃣": 8, "9️⃣": 9
        }
        self.indices_alvos = [i for i, x in enumerate(grid_inicial) if x == "🟢"]
    
    def iniciar(self):
        return No(self.estado_inicial)
    
    def testar_objetivo(self, no):
        for idx in self.indices_alvos:
            if no.estado[idx] not in self.valor:
                return False
        return True
    
    def calcular_passo(self, estado_atual, idx_destino):
        item = estado_atual[idx_destino]
        if item in self.valor:
            return 1 + self.valor[item]
        return 1
    
    def gerar_sucessores(self, no):
        sucessores = []
        try:
            pos_agente = no.estado.index("🙎")
        except ValueError: return []
        
        r, c = pos_agente // self.M, pos_agente % self.M
        movimentos = [(-1, 0, "⬆️"), (1, 0, "⬇️"), (0, -1, "⬅️"), (0, 1, "➡️")]

        for dr, dc, seta in movimentos:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.N and 0 <= nc < self.M:
                idx_frente = nr * self.M + nc
                item_frente = no.estado[idx_frente]
                if item_frente == "⚪️" or item_frente == "🟢":
                    novo_estado = list(no.estado)
                    novo_estado[pos_agente] = "🟢" if pos_agente in self.indices_alvos else "⚪️"
                    novo_estado[idx_frente] = "🙎"
                    
                    custo_total = no.custo + self.calcular_passo(no.estado, idx_frente)
                    sucessores.append(No(novo_estado, no, seta, custo_total))

        
                elif item_frente in self.valor:
                    nnr, nnc = nr + dr, nc + dc
                    if 0 <= nnr < self.N and 0 <= nnc < self.M:
                        idx_tras = nnr * self.M + nnc
                        if no.estado[idx_tras] == "⚪️" or no.estado[idx_tras] == "🟢":
                            novo_estado = list(no.estado)
                            novo_estado[pos_agente] = "🟢" if pos_agente in self.indices_alvos else "⚪️"
                            novo_estado[idx_frente] = "🙎"
                            novo_estado[idx_tras] = item_frente
                            
                            custo_total = no.custo + self.calcular_passo(no.estado, idx_frente)
                            sucessores.append(No(novo_estado, no, seta, custo_total))
                            
        return sucessores


def carregar_entrada(arquivo_path):
    try:
        with open(arquivo_path, 'r', encoding='utf-8') as f:
            linhas = [l.strip() for l in f.readlines() if l.strip()]
        
        if not linhas: return None, 0, 0
        
        M = len(linhas[0].split()) 
        N = len(linhas)            
        grid_flat = []
        for l in linhas:
            grid_flat.extend(l.split())
            
        return grid_flat, N, M
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return None, 0, 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python solucao.py grids/entrada8.txt")
        sys.exit(1)
    
    arquivo_entrada = sys.argv[1]
    grid_inicial, N, M = carregar_entrada(arquivo_entrada)
    
    
    print(arquivo_entrada)
    
    if grid_inicial is None:
        print("Erro ao carregar o grid.")
        sys.exit(1)
    
    print(f"Grid carregado: {N}x{M}")
    problema = Problema(grid_inicial, N, M)
    no_inicial = problema.iniciar()
    print("Estado inicial mapeado")