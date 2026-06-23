import random
import time

print("Prepare-se... O jogo vai começar!")

# 1. Gerar um número N aleatório entre 2 e 10
N = random.randint(2, 10)

# 2. Pausar a execução por N segundos
time.sleep(N)

# 3. Imprimir a palavra "AGORA!"
print("AGORA!")

# 4. Guardar o tempo atual antes do input
tempo0 = time.time()

# 5. Ler uma entrada do usuário (o enter)
input()

# 6. Pegar o tempo atual novamente e subtrair
tempo1 = time.time()
tempo_resposta = tempo1 - tempo0

# 7. Imprimir quanto tempo se passou
print(f"Seu tempo de resposta foi de {tempo_resposta:.4f} segundos.")