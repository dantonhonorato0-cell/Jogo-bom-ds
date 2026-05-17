import random 
# nome do meliante 
nome = input("Digite seu nome nobre: ")
print(f"Olá, {nome}")

classe_escolhida = input("Entre com a classe (Mago, Guerreiro, Arqueiro): ").strip().lower()

# 1Sistema do inventário do abençoado 
if classe_escolhida == "mago":
    classe = "Mago"
    arma = "Cajado de Cristal"
elif classe_escolhida == "guerreiro":
    classe = "Guerreiro"
    arma = "Espada de Ferro"
elif classe_escolhida == "arqueiro":
    classe = "Arqueiro"
    arma = "Arco Curto"
else:
    print("Classe inválida")
    exit()

print(f"\nClasse escolhida: {classe}")
print(f"Item adicionado ao inventário: [{arma}]")

# 2Sistema de Dados (Rolar 3 dados de 6 lados)
print("\nRolando os dados de atributos...")
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)
pontos_dados = dado1 + dado2 + dado3
print(f"Você rolou os dados ({dado1}, {dado2}, {dado3}) e conseguiu {pontos_dados} pontos extras!")

# 3sistema de atributos Base + Bônus dos dados
if classe == "Mago":
    vida = 40
    ataque = 5
    magia = 25 + pontos_dados  # Mago ganha o bônus em Magia
elif classe == "Guerreiro":
    vida = 80 + pontos_dados   # Guerreiro ganha o bônus em Vida
    ataque = 15
    magia = 0
else:  # Arqueiro
    vida = 50
    ataque = 18 + pontos_dados # Arqueiro ganha o bônus em Ataque
    magia = 5
# pra aparecer a Ficha do Personagem
print("\n=== FICHA DO PERSONAGEM ===")
print(f"Nome: {nome}")
print(f"Classe: {classe}")
print(f"Arma: {arma}")
print(f"Vida: {vida}")
print(f"Ataque: {ataque}")
print(f"Magia: {magia}")
print("===========================")

