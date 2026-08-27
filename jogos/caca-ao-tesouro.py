import os


def exibeMapa():
    print()
    for linha in mapa:
        print('|'.join(linha))
    print()


def jogada(linha, coluna):
    if (
        not 0 < linha <= 4 or
        not 0 < coluna <= 4
    ):
        os.system('cls')
        print('⚠️  Coordenadas inválidas!')
        print('\nEscolha valores entre 1 e 4.')
        input('\nPressione Enter para tentar novamente.')
        return 'invalido'

    elif mapa[linha][coluna] == ' ❌ ':
        os.system('cls')
        print('🔁 Você já explorou essa posição!')
        print('\nTente outro local.')
        input('\nPressione Enter para tentar novamente.')
        return 'invalido'

    elif (
        linha == tesouroLinha and
        coluna == tesouroColuna
    ):
        mapa[linha][coluna] = ' 💎 '
        return 'encontrou'

    else:
        mapa[linha][coluna] = ' ❌ '
        os.system('cls')
        print('🌑 Nada encontrado aqui...')
        print('\nA busca continua!')
        print(f'\nTentativas restantes: {4 - tentativas}')
        input('\nPressione Enter para tentar novamente.')


tesouroLinha = 4
tesouroColuna = 4

os.system('cls')
print('🚀 Missão iniciada!')
print('\nVocê pousou em um planeta desconhecido...')
print('Sensores indicam que há um tesouro escondido aqui 💎')
print('\nMas cuidado: você só tem 5 tentativas para encontrá-lo!')
input('\nPressione Enter para começar')

while True:
    mapa = [
        [' 0️⃣  ', ' 1️⃣  ', ' 2️⃣  ', ' 3️⃣  ', ' 4️⃣  '],
        [' 1️⃣  ', ' ⚫ ', ' ⚫ ', ' ⚫ ', ' ⚫ '],
        [' 2️⃣  ', ' ⚫ ', ' ⚫ ', ' ⚫ ', ' ⚫ '],
        [' 3️⃣  ', ' ⚫ ', ' ⚫ ', ' ⚫ ', ' ⚫ '],
        [' 4️⃣  ', ' ⚫ ', ' ⚫ ', ' ⚫ ', ' ⚫ '],
    ]

    resultado = None
    tentativas = 0

    while tentativas < 5:
        os.system('cls')
        print('🪐 O mapa foi carregado!')

        exibeMapa()

        print('Escolha uma linha e uma coluna para explorar.')
        print('(Lembre-se: valores de 1 a 4)')

        try:
            linha = int(input('\nDigite a linha: '))
            coluna = int(input('Digite a coluna: '))
            resultado = jogada(linha, coluna)

        except ValueError:
            os.system('cls')
            print('⚠️  Coordenadas inválidas!')
            print('\nEscolha valores entre 1 e 4.')
            input('\nPressione Enter para tentar novamente.')
            continue

        if resultado != 'invalido':
            tentativas += 1

        if resultado == 'encontrou':
            os.system('cls')
            exibeMapa()
            print('💎 TESOURO ENCONTRADO!')
            print('\nParabéns, explorador!')
            print('Você encontrou o tesouro escondido no planeta 🪐')
            break

    if resultado == 'encontrou':
        break

    else:
        os.system('cls')
        exibeMapa()
        print('\n⛔ Missão encerrada...')
        print('\nVocê usou todas as tentativas!')
        input('\nPressione Enter para continuar.')

    while True:
        os.system('cls')
        jogarNovamente = input('Quer jogar novamente? (s/n): ').lower()

        if jogarNovamente == 's' or jogarNovamente == 'n':
            break

        else:
            print('Digite uma opção válida.')
            input('\nPressione Enter para continuar.')

    if jogarNovamente == 'n':
        print('Obrigado por jogar. Até a próxima aventura!')
        break