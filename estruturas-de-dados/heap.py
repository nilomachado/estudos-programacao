from heapq import *

fila_prioridade = []

heappush(fila_prioridade, (3, "Instalar impressora"))
heappush(fila_prioridade, (1, "Servidor fora do ar"))
heappush(fila_prioridade, (2, "Computador não liga"))
heappush(fila_prioridade, (1, "Sistema da empresa fora do ar"))

while fila_prioridade:
  prioridade, tarefa = heappop(fila_prioridade)
  print(f"Executando: {tarefa} | Prioridade: {prioridade}")