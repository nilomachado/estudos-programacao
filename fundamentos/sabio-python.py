import os

os.system ('cls')

def mensagemFinal():
  os.system ('cls')
  print('🔮 O Oráculo se silencia...')

  print('\nPreciso recarregar minhas energias com café ☕')
  print('Volte mais tarde para mais sabedoria!')
  print('\n(ou quando rodar o programa de novo 😏)')

while True:
  os.system ('cls')
  print('🔮 Bem-vindo ao Oráculo da Sabedoria Python...')
  print('\nFaça sua pergunta ou diga um tema da programação...')
  print('E eu tentarei te guiar 👁️')

  print('\nSobre qual tema você deseja conhecimento? ')
  print('(ex: variáveis, loops, funções, listas, condicionais, erros...)')
  tema = input('Tema: ').lower()

  match tema:
    case 'váriaveis' | 'variaveis' | 'váriavel' | 'variavel':
      os.system ('cls')
      print('As variáveis são como caixas mágicas...')
      print('Elas guardam valores que você pode usar quando quiser.')
      print('Sem elas, seu código não tem memória.')

      if input('\nDeseja ver sobre outro tema? (s/n): ').lower() == 'n':
        mensagemFinal()
        break

    case 'loops' | 'loop':
      os.system ('cls')
      print('Loops representam repetição...')
      print('Assim como os ciclos da vida, o código também repete até cumprir seu destino.')
      print('Use com sabedoria, ou ficará preso em um loop infinito 👀')
            
      if input('\nDeseja ver sobre outro tema? (s/n): ').lower() == 'n':
        mensagemFinal()
        break


    case 'funções' | 'funçoes' | 'funcões' | 'funcoes':
      os.system ('cls')
      print('Funções são feitiços reutilizáveis...')
      print('Você escreve uma vez e pode invocar sempre que precisar.')
      print('Domine-as, e seu código se tornará poderoso.')
            
      if input('\nDeseja ver sobre outro tema? (s/n): ').lower() == 'n':
        mensagemFinal()
        break
    
    case 'listas' | 'lista':
      os.system ('cls')
      print('Listas são coleções de elementos...')
      print('Como um inventário de um aventureiro.')
      print('Organize bem seus dados, e encontrará tudo com facilidade.')
            
      if input('\nDeseja ver sobre outro tema? (s/n): ').lower() == 'n':
        mensagemFinal()
        break

    case 'condicionais' | 'condicional':
      os.system ('cls')
      print('As decisões do código vêm das condicionais...')
      print('Se algo for verdadeiro, um caminho se abre.')
      print('Caso contrário, outro destino será seguido.')

      if input('\nDeseja ver sobre outro tema? (s/n): ').lower() == 'n':
        mensagemFinal()
        break

    case 'erros' | 'erro':
      os.system ('cls')
      print('Erros não são falhas...')
      print('São mensagens do código pedindo sua atenção.')
      print('Leia-os com calma, e encontrará a solução.')
            
      if input('\nDeseja ver sobre outro tema? (s/n): ').lower() == 'n':
        mensagemFinal()
        break

    case _:
      os.system ('cls')
      print('Hmm... esse conhecimento ainda não está nos meus pergaminhos...')
      print('Mas continue estudando, jovem programador 🧙‍♂️')
            
      if input('\nDeseja ver sobre outro tema? (s/n): ').lower() == 'n':
        mensagemFinal()
        break