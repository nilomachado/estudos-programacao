dados = [ ['Ele gosta de banana?', 'macaco'] ]

print('Bem vindo ao Jogo de Adivinha!')
print('Irei adivinhar o animal que está pensando.')

while True:
  print('Pense em um animal...')

  acertou = False
  for dado in dados:
    resposta = input(f'{dado[0]} (s/n): ')
    if resposta == 's':
      print(f'Você pensou no(a) {dado[1]}!')
      acertou = True
      break

  if not acertou:
    print('Poxa, então eu não sei.')
    animal = input('Em qual animal você estava pensando?: ')
    pergunta = input('Qual pergunta eu teria que fazer para acertar esse animal?: ')
    dados.append([pergunta, animal])

  resposta = input('Quer jogar novamente? (s/n): ')
  if resposta == 'n':
    break

print('Obrigado por jogar. Até a próxima!')