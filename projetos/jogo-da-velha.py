import os
os.system("cls")

tabuleiro = [ 
  [' ', ' ', ' '],
  [' ', ' ', ' '],
  [' ', ' ', ' '],
]

jogador = 'X'

def exibeTabuleiro():
  print()
  for linha in tabuleiro:
    print('|'.join(linha))
  print()

def jogada(linha, coluna):
  if (
    not 0 <= linha <= 2 or
    not 0 <= coluna <= 2
  ):
    print('\nJogada inválida! Informe um número válido entre 0 e 2.')
    return jogador

  if tabuleiro[linha][coluna] != ' ':
    print('\nJogada inválida! Essa casa já foi escolhida.')
    return jogador
  tabuleiro[linha][coluna] = jogador
  return 'O' if jogador == 'X' else 'X'

def verificaResultado():
  # linhas
  for linha in range(3):
    if (
      tabuleiro[linha][0] ==
      tabuleiro[linha][1] ==
      tabuleiro[linha][2] and
      tabuleiro[linha][0] != ' '
    ):
      return 'vitoria'

  # colunas
  for coluna in range(3):
    if (
      tabuleiro[0][coluna] ==
      tabuleiro[1][coluna] ==
      tabuleiro[2][coluna] and
      tabuleiro[0][coluna] != ' '
    ):
      return 'vitoria'
  
  # diagonais
  if (
    tabuleiro[1][1] != ' ' and
    (
      (
        tabuleiro[0][0] ==
        tabuleiro[1][1] ==
        tabuleiro[2][2]
      ) or
      (
        tabuleiro[0][2] ==
        tabuleiro[1][1] ==
        tabuleiro[2][0]
      )
    )
  ):
    return 'vitoria'
  
  # empate
  for linha in range(3):
    for coluna in range(3):
      if tabuleiro[linha][coluna] == ' ':
        return None
  return 'empate'

print('\nBem vindo ao Jogo da Velha!')

while True:
  print(f'\nO jogador da vez é: {jogador}')
  exibeTabuleiro()
  
  try:
    linha = int(input('Digite a linha: '))
    coluna = int(input('Digite a coluna: '))
    os.system("cls")
    jogador = jogada(linha, coluna)
    resultado = verificaResultado()
  except (ValueError, IndexError):
    os.system("cls")
    print('\nJogada inválida! Informe um número válido entre 0 e 2.')

  if resultado == 'vitoria':
    jogador = 'O' if jogador == 'X' else 'O'
    exibeTabuleiro()
    print(f'Parabéns! O jogador "{jogador}" ganhou o jogo!')
    break

  if resultado == 'empate':
    exibeTabuleiro()
    print(f'Empate! Nenhum jogador conseguiu vencer.')
    break