import random
import time

# Sorteando o número misterioso N entre 0 e 10
N = random.randint(0, 10)
print(f"(O número misterioso sorteado foi N = {N})")

# Repetindo N vezes
for i in range(N):
    # i começa em 0, então adicionamos 1 para mostrar "Volta 1", "Volta 2"...
    print(f"Volta {i + 1}: Mais uma volta!")
    time.sleep(1) # Aguarda 1 segundo