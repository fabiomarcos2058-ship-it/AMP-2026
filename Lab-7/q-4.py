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
    # Explicação: Usando a biblioteca 'random', o código sorteia um número de 1 a 10. 
# O usuário ganha 5 tentativas para acertar. Um loop controla as chances e um 'if' 
# verifica se o palpite bateu em cheio com o número sorteado, usando o 'break' 
# para dar a vitória na hora.
