import random
import time

while True:
    deseja_perguntar = input("Você deseja fazer uma pergunta para a Bola Mágica? (sim/não): ")
    if deseja_perguntar.lower() in ['não', 'nao', 'n']:
        break
        
    pergunta = input("Digite a sua pergunta: ")
    
    # Efeito dramático de pensamento
    print("Deixe-me pensar.......")
    time.sleep(2)
    
    # Lógica de aleatoriedade exigida pelo enunciado
    prob = random.randint(1, 10)
    if prob <= 5:
        resposta = 'SIM'
    else:
        resposta = 'NÃO'
        
    print(f"Resposta da Bola Mágica: {resposta}\n")