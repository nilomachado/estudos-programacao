import time
print("INICIALIZANDO O LOVE SCAN")
print("-------------------------")
time.sleep(2)
nome = input("Digite o nome para calcular a compatibilidade: ")

print(f"\nCalculando afinidade para: {nome}...")
time.sleep(2)

if nome == "Ash":
  print("\n[!] RESULTADO ENCONTRADO [!]")
  print("✨ Nível de Amor: IMENSURÁVEL")
  print("✨ Status: Completamente apaixonado.")
  print("✨ Nota: Vocês foram feitos um para o outro! ❤️")
else:
  print("\n[!] ALERTA DE INCOMPATIBILIDADE [!]")
  print("⚠️  Nível de Amor: INEXISTENTE")
  print("⚠️  Motivo: O coração deste usuário já tem dona.")
  print('⚠️  Dica: Começa com "A" e termina com "Ash".')

print("\nEscaneamento finalizado.")