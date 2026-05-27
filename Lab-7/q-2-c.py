maior = float('-inf') 

contador = 0 

while contador < 10:
    num = int(input("Digite um número: "))
    if num > maior:
        maior = num
    contador += 1 

print('O maior número é', maior)