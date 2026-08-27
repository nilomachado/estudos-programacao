import os

dados = [
  ['Qual linguagem usa indentação obrigatória?', 'python'],
  ['Qual estrutura usamos para repetição?', 'loop'],
  ['Qual palavra usamos para criar uma função?', 'def'],
  ['Qual tipo guarda vários valores?', 'lista']
  ]

while True:
  acertos = 0
  total = 0

  os.system('cls')
  print('🧠 Bem-vindo ao Desafio do Dev!')
  print('\nResponda as perguntas corretamente para provar que você domina a programação 😏')
  input('\nPressione Enter para começar')
  
  for dado in dados:
    while True:
      os.system('cls')
      resposta = input(f'{dado[0]}: ').lower()

      if resposta == '':
        print('\n⚠️  Jogada inválida! Você precisa responder algo.')
        input('\nPressione Enter para continuar')
        continue

      if resposta == dado[1]:
        acertos += 1
        print('\n✅ Boa! Você acertou!')

      else:
        print('\n❌ Resposta incorreta! Continue tentando!')

      total += 1
      input('\nPressione Enter para continuar.')
      break

  os.system('cls')
  print('🏁 Fim do desafio!')
  print(f'\nVocê acertou {acertos} de {total} perguntas!')
  if input('\nQuer tentar novamente? (s/n): ') == 'n':
    os.system('cls')
    print('Obrigado por jogar. Até a próxima!')
    break