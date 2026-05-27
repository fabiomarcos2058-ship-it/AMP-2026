import random

numero_secreto = random.randint(1, 10)
chances = 5

while chances > 0:
    palpite = int(input(f"Adivinhe o número de 1 a 10 (Chances: {chances}): "))
    
    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    elif palpite < numero_secreto:
        print("Dica: O número secreto é MAIOR.")
    else:
        print("Dica: O número secreto é MENOR.")
        
    chances -= 1

if chances == 0:
    print(f"Suas chances acabaram! O número secreto era {numero_secreto}.")