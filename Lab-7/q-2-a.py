N = int(input("Quantos números quer digitar farmador? "))
contador = 1
impares = 0

while contador <= N:
    num = int(input("Digite um número: "))
    if num % 2 != 0:
        impares += 1
    # Explicação: Faltava incrementar o contador para o loop não rodar para sempre
    contador += 1 

print(f"Quantidade de ímpares: {impares}")
