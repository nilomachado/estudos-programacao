import os

os.system ('cls')

notas = []

for i in range (1,4):
  while True:
    try:
      nota = float(input(f'\nDigite a nota {i}: '))

      if 0 <= nota <= 10:
        notas.append(nota)
        break
      
      print('Digite valores entre 0 e 10.')

    except ValueError:
      print('Digite apenas números.')

media = sum(notas) / len(notas)

os.system('cls')

print(f'\nSua média final é: {media:.2f}')

if media >= 6:
  print('\nParabéns, você passou!')

elif media <= 4:
  print('\nQue pena, você foi reprovado!')
  
else:
  print('\nVocê está de recuperação.')