def torre_de_hanoi(num_discos, origem, auxiliar, destino):
  if num_discos == 1:
    print(f"Mover o disco 1 da torre {origem} para a torre {destino}")
  else:
    torre_de_hanoi(num_discos - 1, origem, destino, auxiliar)
    print(f"Mover o disco {num_discos} da torre {origem} para a torre {destino}")
    torre_de_hanoi(num_discos - 1, auxiliar, origem, destino)
    
num_discos = 10
torre_de_hanoi(num_discos, 'ESQUERDA', 'MEIO', 'DIREITA')