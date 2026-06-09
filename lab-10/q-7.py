n = int(input())
vitorias = 0
empates = 0
derrotas = 0

for _ in range(n):
    gols_galo = int(input())
    gols_oponente = int(input())
    
    if gols_galo > gols_oponente:
        vitorias += 1
    elif gols_galo == gols_oponente:
        empates += 1
    else:
        derrotas += 1

pontuacao = (vitorias * 3) + (empates * 1)

print(f"Vitórias: {vitorias}")
print(f"Empates: {empates}")
print(f"Derrotas: {derrotas}")
print(f"Pontuação: {pontuacao}")