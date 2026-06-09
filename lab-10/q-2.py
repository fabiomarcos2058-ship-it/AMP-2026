# questao_02.py

# 1) range(10)
# inicio=0, fim=10, pulo=1
# Resultado da execução:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
print("--- Resultado de range(10) ---")
for variavel in range(10):
    print(variavel)


# 2) range(1, 5)
# inicio=1, fim=5, pulo=1
# Resultado da execução:
# 1
# 2
# 3
# 4
print("\n--- Resultado de range(1, 5) ---")
for variavel in range(1, 5):
    print(variavel)


# 3) range(0, 10, 2)
# inicio=0, fim=10, pulo=2
# Resultado da execução:
# 0
# 2
# 4
# 6
# 8
print("\n--- Resultado de range(0, 10, 2) ---")
for variavel in range(0, 10, 2):
    print(variavel)


# 4) range(10, 0, -1)
# inicio=10, fim=0, pulo=-1
# Resultado da execução:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
print("\n--- Resultado de range(10, 0, -1) ---")
for variavel in range(10, 0, -1):
    print(variavel)