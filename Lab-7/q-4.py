import random # essa deve ser a primeira linha do código

numero_secreto = random.randint(1, 10)
chances = 5

while chances > 0:
    palpite = int(input(f"Adivinhe o número de 1 a 10 (Chances: {chances}): "))
    
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número em cheio!")
        break
        
    chances -= 1

if chances == 0:
    print(f"Que pena, suas chances acabaram. O número era {numero_secreto}.")