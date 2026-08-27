import os

tarefas = []

def exibir_tarefas():
  for tarefa in tarefas:
      print(f'{tarefa[0]} - Status: {tarefa[1]}')
    
def adicionar_tarefa(tarefa):
  tarefas.append((tarefa, 'Pendente'))

def remover_tarefa(tarefa):
  global tarefas
  tarefas = [ t for t in tarefas if t[0].lower() != tarefa.lower() ]
  
def concluir_tarefa(tarefa):
  global tarefas
  tarefas = [ (t[0], 'Concluída') if t[0].lower() == tarefa.lower() else t for t in tarefas ]
  
def buscar_tarefa(tarefa):
  encontrado = [ t for t in tarefas if t[0].lower() == tarefa.lower() ]
  if encontrado:
    for titulo, status in encontrado:
      print(f'Tarefa encontrada: {titulo} - Status: {status}')
  else:
      print(f'Tarefa não encontrada: {tarefa}')
    
while True:
  os.system('cls')
  print('Boas vindas ao gerenciador de lista de tarefas!')
  print()
  print('Escolha uma opção:')
  print()
  print('1 - Listar tarefas')
  print('2 - Adicionar tarefa')
  print('3 - Remover tarefa')
  print('4 - Concluir tarefa')
  print('5 - Buscar tarefas')
  print('0 - Sair')
  print()
  opcao = int(input('Digite a opção desejada: '))
  
  match opcao:
    case 1:
      os.system('cls')
      if not tarefas:
        print('A lista de tarefas está vazia.')
      else:
        print('Lista de tarefas:')
        print()
        exibir_tarefas()
      print()
      input('Pressione ENTER para continuar...')
      
    case 2:
      os.system('cls')
      tarefa = input('Digite a tarefa que deseja adicionar: ')
      print()
      adicionar_tarefa(tarefa)
      print(f'Tarefa adicionada.')
      print()
      input('Pressione ENTER para continuar...')
      
    case 3:
      os.system('cls')
      if not tarefas:
        print('Não há tarefas para remover.')
      else:
        tarefa = input('Digite a tarefa que deseja remover: ')
        print()
        remover_tarefa(tarefa)
        print(f'Tarefa removida.')
        print()
      input('Pressione ENTER para continuar...')
      
    case 4:
      os.system('cls')
      if not tarefas:
        print('Não há tarefas para concluir.')
      else:
        tarefa = input('Digite a tarefa que deseja concluir: ')
        print()
        concluir_tarefa(tarefa)
        print(f'Tarefa concluída.')
        print()
      input('Pressione ENTER para continuar...')
      
    case 5:
      os.system('cls')
      if not tarefas:
        print('Não há tarefas para buscar.')
      else:
        tarefa = input('Digite a tarefa que deseja buscar: ')
        print()
        buscar_tarefa(tarefa)
      print()
      input('Pressione ENTER para continuar...')
      
    case 0:
      os.system('cls')
      print('Encerrando o Gerenciador de Tarefas...')
      print()
      print('Programa finalizado com sucesso.')
      print()
      break
    
    case _:
      print('Opção inválida.')
      print()
      input('Pressione ENTER para continuar...')