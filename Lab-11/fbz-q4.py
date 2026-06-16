import random

# Gera um número secreto de 3 dígitos (ex: "731") de forma aleatória
# Para garantir que tenha 3 dígitos, sorteamos de 100 a 999
num_secreto = str(random.randint(100, 999))

# Se você quiser testar com um número fixo específico como o do exemplo do enunciado, 
# basta descomentar a linha abaixo:
# num_secreto = "731"

print("Um número secreto de 3 dígitos foi gerado. Você tem até 10 chances para adivinhar!")

for chance in range(1, 11):
    print(f"\n==== Chance {chance} ====")
    
    # Recebe o palpite do usuário separado por espaços ou direto, e limpa os espaços
    palpite_cru = input("Palpite: ")
    palpite = palpite_cru.replace(" ", "")
    
    # Validação simples para evitar quebras se o usuário digitar errado
    if len(palpite) != 3:
        print("Por favor, digite um palpite válido com 3 dígitos.")
        continue
        
    saida = ""
    
    for i in range(3):
        if palpite[i] == num_secreto[i]:
            saida += "+"  # Dígito certo na posição correta
        elif palpite[i] in num_secreto:
            saida += "!"  # Dígito existe no número secreto, mas está na posição errada
        else:
            saida += "_"  # Dígito não está presente no número secreto
            
    print(f"Saída: {saida}")
    
    if palpite == num_secreto:
        print("Parabéns! Você acertou!")
        break
else:
    print(f"\nFim de jogo! Você usou as 10 chances. O número secreto era {num_secreto}.")