maior = float('-inf') 

contador = 0 

while contador < 10:
    num = int(input("Digite um número: "))
    if num > maior:
        maior = num
    contador += 1 

print('O maior número é', maior)
# Explicação: Este algoritmo descobre qual é o maior número de uma sequência. 
# O truque é começar a variável 'maior' com menos infinito (float('-inf')), 
# garantindo que o primeiro número digitado tome o posto de maior atual. 
# A partir daí, se o próximo número digitado for maior, ele assume o trono.
