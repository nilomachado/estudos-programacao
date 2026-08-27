frase = "O curso de Lógica de Programação é supimpa!"
frase_suja = " O curso de Lógica de Programação é supimpa! "

def analisador_de_texto(texto):
  palavras = texto.split()
  num_palavras = len(palavras)
  num_caracteres = len(texto)
  num_caracteres_sem_espacos = num_caracteres - texto.count(" ")

  return num_palavras, num_caracteres, num_caracteres_sem_espacos

num_p, num_c, num_cse = analisador_de_texto(frase)

print("=" * 50)
print("INFORMAÇÕES DA STRING")
print("=" * 50)

print(f"Primeira letra: {frase[0]}")
print(f"Última letra: {frase[-1]}")
print(f"Tamanho da frase: {len(frase)} caracteres")

print("\n" + "=" * 50)
print("TRANSFORMAÇÕES")
print("=" * 50)

print(f"Maiúsculas: {frase.upper()}")
print(f"Minúsculas: {frase.lower()}")

print("\n" + "=" * 50)
print("FATIAMENTO")
print("=" * 50)

print(f"Split padrão: {frase.split()}")
print(f"Split usando 'a': {frase.split('a')}")

print("\n" + "=" * 50)
print("REMOÇÃO DE ESPAÇOS")
print("=" * 50)

print(f"Frase suja: '{frase_suja}'")
print(f"Frase limpa: '{frase_suja.strip()}'")
print(f"Tamanho da string limpa: {len(frase.strip())}")

print("\n" + "=" * 50)
print("ANÁLISE DO TEXTO")
print("=" * 50)

print(f"Número de palavras: {num_p}")
print(f"Número de caracteres: {num_c}")
print(f"Número de caracteres sem espaços: {num_cse}")