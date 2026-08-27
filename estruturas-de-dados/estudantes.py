estudantes = {
    1: { 'nome': 'Joana', 'idade': 45, 'curso': 'Computação' },
    2: { 'nome': 'Ivan', 'idade': 70, 'curso': 'Matemática' },
    3: { 'nome': 'Jaqueline', 'idade': 20, 'curso': 'Computação' }
}

cursos = { 'Computação', 'Matemática', 'Física' }

estudantes_cursos = {
    'Computação': { 1, 3 },
    'Matemática': { 2 }
}

def adicionar_estudante(matricula, nome, idade, curso):
  estudantes[matricula] = {'nome': nome, 'idade': idade, 'curso': curso}
  if curso not in estudantes_cursos:
    estudantes_cursos[curso] = set()
  estudantes_cursos[curso].add(matricula)
  
print(estudantes_cursos)
adicionar_estudante(5, 'João', 50, 'Computação')
print(estudantes_cursos)
adicionar_estudante(6, 'Maria', 60, 'Física')
print(estudantes_cursos)