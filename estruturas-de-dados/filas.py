from collections import deque

def criaFila():
  return deque()

def insereNaFila(elemento, fila):
  fila.append(elemento)

def removeDaFila(fila):
  return fila.popleft()

pedidos = criaFila()

print(pedidos)
insereNaFila(1, pedidos)
insereNaFila(2, pedidos)
insereNaFila(3, pedidos)
insereNaFila(4, pedidos)
insereNaFila(5, pedidos)
print(pedidos)
print(f"Removendo da fila: {removeDaFila(pedidos)}")
print(f"Removendo da fila: {removeDaFila(pedidos)}")
print(pedidos)