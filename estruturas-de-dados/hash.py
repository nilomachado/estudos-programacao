texto = 'Aprender programação exige prática, paciência e dedicação. No início, muitos conceitos parecem difíceis, mas o estudo constante ajuda a transformar problemas complexos em tarefas mais simples.  Quando um estudante começa a programar, é comum encontrar erros e não entender imediatamente por que determinado código não funciona. Nesses momentos, observar o comportamento do programa e testar diferentes soluções pode ser uma excelente forma de aprender. \
\
A programação também ensina a organizar ideias. Antes de escrever um código, é importante compreender o problema e pensar em uma maneira lógica de resolvê-lo. Depois, cada etapa pode ser transformada em instruções que o computador consiga executar. Com o tempo, conceitos como variáveis, funções, listas, dicionários e estruturas de repetição passam a fazer parte do raciocínio do estudante. \
\
Estudar tecnologia é um processo contínuo. Novas ferramentas, linguagens e técnicas surgem constantemente, por isso é importante manter a curiosidade e buscar novos conhecimentos. Pequenos projetos podem ajudar bastante nesse processo, pois permitem colocar a teoria em prática e perceber como diferentes conceitos podem trabalhar juntos. \
\
A prática diária também ajuda a desenvolver confiança. Um problema que parecia complicado ontem pode se tornar simples depois de algumas tentativas. Por isso, errar durante o aprendizado não significa fracassar. Cada erro pode mostrar uma nova maneira de pensar e ajudar o estudante a compreender melhor aquilo que está estudando.'

palavras = texto.split()

tabela = {}

for palavra in palavras:
  indice = palavra[0].upper()
  
  if indice not in tabela:
    tabela[indice] = []
  
  tabela[indice].append(palavra)

for chave, valor in sorted(tabela.items()):
  print(f'{chave}: {valor}')
  print(f'Quantidade: {len(valor)}')
  print()