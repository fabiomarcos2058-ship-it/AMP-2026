import random

pontos_j1 = 0
pontos_j2 = 0
rodada = 1

while pontos_j1 < 50 and pontos_j2 < 50:
    print(f"\n========= RODADA {rodada} =========")
    palpite_j1 = int(input(f"Jogador 1 ({pontos_j1} pontos): Qual o seu palpite para a soma dos dados? "))
    palpite_j2 = int(input(f"Jogador 2 ({pontos_j2} pontos): Qual o seu palpite para a soma dos dados? "))
    
    print("\n🎲 Rolando os dados...")
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    resultado = dado1 + dado2
    
    print(f"Dado 1: {dado1}")
    print(f"Dado 2: {dado2}")
    print(f"Resultado real da soma: {resultado}")
    
    # Calcula a proximidade (distância absoluta)
    dif_j1 = abs(resultado - palpite_j1)
    dif_j2 = abs(resultado - palpite_j2)
    
    if dif_j1 < dif_j2:
        pontos_j1 += 5
        print("Resultado: Jogador 1 chegou mais perto e ganha 5 pontos!")
    elif dif_j2 < dif_j1:
        pontos_j2 += 5
        print("Resultado: Jogador 2 chegou mais perto e ganha 5 pontos!")
    else:
        pontos_j1 += 2
        pontos_j2 += 2
        print("Resultado: ⚖️ EMPATE! Cada um ganha 2 pontos!")
        
    rodada += 1

print("\n================ FIM DE JOGO ================")
print(f"Pontuação Final -> Jogador 1: {pontos_j1} | Jogador 2: {pontos_j2}")
if pontos_j1 >= 50 and pontos_j2 >= 50:
    print("Tivemos um empate técnico no final do jogo!")
elif pontos_j1 >= 50:
    print("Parabéns Jogador 1! Você é o vencedor!")
else:
    print("Parabéns Jogador 2! Você é o vencedor!")