import os
os.system('cls')

print('🎯 Bem-vindo ao desafio do Número Secreto!')
print('\nEu pensei em um número...')
print('E quero ver se você consegue descobrir 😏')
input('\nPressione Enter para continuar')

numeroSecreto = 7
tentativas = 0

while True:
  os.system('cls')
  print('🔢 O número está entre 1 e 10.')
  print('Tente adivinhar!')

  try:
    palpite = int(input('\nDigite seu palpite: '))
  except ValueError:
    os.system('cls')
    print('⚠️ Entrada inválida! Digite um número válido.')
    input('\nPressione Enter para tentar novamente.')
    continue

  if not 0 < palpite <= 10:
    os.system('cls')
    print('⚠️ Entrada inválida! Digite um número entre 1 e 10.')
    input('\nPressione Enter para tentar novamente.')
    continue

  tentativas += 1

  if palpite > numeroSecreto:
    os.system('cls')
    print('📉 O número secreto é menor que isso!')
    
  elif palpite < numeroSecreto:
    os.system('cls')
    print('📈 O número secreto é maior que isso!')

  else:
    print('\n🎉 Parabéns! Você acertou o número secreto!')
    print(f'\nVocê descobriu o número secreto em {tentativas} tentativa(s)!')
    break
  
  input('\nPressione Enter para tentar novamente.')