print('Olá, eu sou a sua assistente. O que você gostaria de perguntar?')

comando = input('Digite um comando: ')

match comando:
  case 'Oi' | 'Olá':
    print('Oi, como você está?')
  case 'Tchau' | 'Sair' | 'Fim' | 'Exit':
        print('Tchau, foi bom conversar com você!')
  case 'Piada':
        print('Sabe qual o padroeiro das pessoas que trabalham com TI? O São Login! 😂')
  case 'Clima' | 'Previsão do tempo':
        print('Tá muito quente! Deve ter passado de 40°C! 🥵')
  case _:
        print('Desculpe, não entendi o comando.')