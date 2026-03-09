#geração dos gráficos de estudo de caso
import matplotlib.pyplot as plt

grids = ['8x8', '16x16', '24x24', '64x64']

# gráfico do tempo de execução vs tamanho ---------------------- 
tempo_dijkstra = [0.0331, 535.2873, None, None]
tempo_ganancioso = [0.0023, 0.0094, 59.9163, 2.5606]
tempo_a_estrela = [0.0050, 0.5819, 1099.8640, None] 

plt.figure(figsize=(10, 6))

plt.plot(grids, tempo_ganancioso, marker='o', label='Ganancioso (Heurística pura)', color='green', linewidth=2)
plt.plot(grids, tempo_a_estrela, marker='s', label='A* (Custo + Heurística)', color='blue', linewidth=2)
plt.plot(grids, tempo_dijkstra, marker='^', label='Dijkstra (Custo real)', color='red', linewidth=2)

plt.title('Estudo de Caso: Tempo de Execução vs Tamanho do Grid', fontsize=14)
plt.xlabel('Tamanho do Grid', fontsize=12)
plt.ylabel('Tempo de Execução (Segundos)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

plt.savefig('grafico_tempo.png', dpi=300) 
plt.show()

# gráfico do custo ---------------------------

custo_dijkstra = [27, 69, None, None]
custo_ganancioso = [49, 69, 161, 377]
custo_a_estrela = [27, 69, 142, None]

plt.figure(figsize=(10, 6))

plt.plot(grids, custo_ganancioso, marker='o', label='Ganancioso (Solução Subótima)', color='green', linewidth=2)
plt.plot(grids, custo_a_estrela, marker='s', label='A* (Solução Ótima)', color='blue', linewidth=2)
plt.plot(grids, custo_dijkstra, marker='^', label='Dijkstra (Solução Ótima)', color='red', linewidth=2, linestyle='--')

plt.title('Estudo de Caso: Qualidade da Solução (Custo do Caminho)', fontsize=14)
plt.xlabel('Tamanho do Grid', fontsize=12)
plt.ylabel('Custo Total', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

plt.savefig('grafico_custo.png', dpi=300)
plt.show()