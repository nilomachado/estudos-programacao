lista = None


def exibeLista():
    if not lista:
        print('A lista está vazia.')
        return

    atual = lista

    while atual != None:
        print(atual['valor'], end=' ')
        atual = atual['proximo']

    print('.')


def adicionaNoFim(elemento):
    global lista
    if not lista:
        lista = {'valor': elemento, 'proximo': None}
        return

    atual = lista

    while atual['proximo']:
        atual = atual['proximo']

    atual['proximo'] = {'valor': elemento, 'proximo': None}


print('Lista inicial:')
exibeLista()

adicionaNoFim(10)
print('Após adicionar 10:')
exibeLista()

adicionaNoFim(20)
print('Após adicionar 20:')
exibeLista()

adicionaNoFim(30)
print('Após adicionar 30:')
exibeLista()
