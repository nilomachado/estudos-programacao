from collections import deque

def criaPilha():
  return deque()

def insereNaPilha(elemento, pilha):
  pilha.append(elemento)

def removeDaPilha(pilha):
  return pilha.pop()

processos = criaPilha()

print(processos)
insereNaPilha(1, processos)
insereNaPilha(2, processos)
insereNaPilha(3, processos)
insereNaPilha(4, processos)
insereNaPilha(5, processos)
print(processos)
print(f"Removendo da pilha: {removeDaPilha(processos)}")
print(f"Removendo da pilha: {removeDaPilha(processos)}")
print(processos)