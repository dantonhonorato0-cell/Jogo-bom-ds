import random  # Permite gerar números aleatórios (sorteio)
# Criação do Personagem
nome = input("Digite seu nome nobre: ")
classe_escolhida = input("Entre com a classe (Mago, Guerreiro, Arqueiro): ").strip().lower()

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

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)
pontos_dados = dado1 + dado2 + dado3

if classe == "Mago":
    vida = 40
    ataque = 5
    magia = 25 + pontos_dados
elif classe == "Guerreiro":
    vida = 80 + pontos_dados
    ataque = 15
    magia = 0
else: 
    vida = 50
    ataque = 18 + pontos_dados
    magia = 5

# inimigo
monstro_nome = "Orc Enfurecido"
monstro_vida = 60
monstro_ataque = 10

print(f"\n de repente, um {monstro_nome} aparece! Preparar para o combate!")

# = COMANDO NOVO: loop 'while' e operador 'and' ===
# O combate continua ENQUANTO a sua vida E a vida do monstro forem maior que 0
while vida > 0 and monstro_vida > 0:
    print(f"\n--- SEU TURNO ---")
    print(f"{nome} (Vida: {vida}) VS {monstro_nome} (Vida: {monstro_vida})")
    
    acao = input("Deseja [1] Atacar ou [2] Usar Magia? ").strip()
    
    # Turno do Jogador
    if acao == "1":
        # COMANDO NOVO: '-=' subtrai o valor do ataque direto da vida do monstro
        monstro_vida -= ataque
        print(f"Você atacou com seu {arma} e causou {ataque} de dano!")
    elif acao == "2":
        if magia >= 10:
            dano_magico = magia // 2  # Divide a magia por 2 para gerar o dano
            monstro_vida -= dano_magico
            print(f"Você lançou um feitiço e causou {dano_magico} de dano mágico!")
        else:
            print("Você não tem energia mágica suficiente! Errou o turno!")
    else:
        print("Você hesitou e perdeu a chance de agir!")

    # Verificação: Se o monstro morreu, o loop quebra aqui
    if monstro_monstro_vida <= 0:
        break

    # Turno do Monstro
    print(f"\n--- TURNO DO {monstro_nome.upper()} ---")
    vida -= monstro_ataque
    print(f"O {monstro_nome} te acertou um golpe! Você perdeu {monstro_ataque} de vida.")

# === FIM DO COMBATE ===
print("\n=========================")
if vida > 0:
    print(f"Vitória! {nome} derrotou o {monstro_nome}!")
else:
    print(f"Derrota... {nome} caiu em combate. Fim de jogo.")
print("=========================")


